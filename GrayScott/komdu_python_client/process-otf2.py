#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import otf2
import numpy as np
import argparse
import logging
from tqdm import tqdm
import sys
import _otf2
from intervaltree import Interval, IntervalTree

## Credit: https://github.com/score-p/otf2_python_scripts/blob/master/otf2_iostats/otf2_iostats.py
class ClockConverter:
    """
    clock_properties: otf2.definitions.ClockProperties
    """
    def __init__(self, clock_properties):
        self.properties = clock_properties

    """
    ticks: int
    return: float
    """
    def to_usec(self, ticks):
        return float(ticks / (self.properties.timer_resolution / 1000000))

    def to_sec(self, ticks):
        return float(ticks / self.properties.timer_resolution)

    """
    secs: float
    return: int
    """
    def to_ticks(self, secs):
        return secs * self.properties.timer_resolution

class ThroughputStat:
    def __init__(self):
        self.count = 0
        self.throughput = 0

    def inc_count(self, count):
        self.count += count

    def inc_throughput(self, throughput):
        self.throughput += throughput

    def __str__(self):
        return "count: {}, throughput: {}".format(self.count, self.throughput)

"""
trace: otf2.reader.Reader
clock: ClockConverter
length: int
return: tuple
"""
def generate_intervals(trace, clock, length):
    start = clock.properties.global_offset
    end = start + clock.properties.trace_length
    for loc_group in trace.definitions.location_groups:
        if loc_group.location_group_type == otf2.enums.LocationGroupType.PROCESS:
            yield (loc_group.name, IntervalTree(Interval(i, i + length, ThroughputStat()) for i in range(start, end, length)))

"""
timestamp: int
tree: IntervalTree
return: Interval
"""
def get_interval(timestamp, tree):
    result = sorted(tree.search(timestamp, strict=True))
    assert(len(result) == 1)
    return result[0]

def print_tree(tree):
    for i in sorted(tree):
        print("{}:{} -> {}".format(i.begin, i.end, i.data))

## src send data to dst
## type: 0 (collective), 1 (p2p)
def message_sent(src, dst, count, message_size, type=0):
    #print ('%d => %d: %d %d %d'%(src, dst, count, message_size, type))
    if type == 0:
        SC0[src, dst] += count
        SV0[src, dst] += message_size
    else:
        SC1[src, dst] += count
        SV1[src, dst] += message_size
    return

## dst receive data from src
## type: 0 (collective), 1 (p2p)
def message_received(dst, src, count, message_size, type=0):
    #print ('%d <= %d: %d %d'%(dst, src, count, message_size, type))
    if type == 0:
        RC0[dst, src] += count
        RV0[dst, src] += message_size
    else:
        RC1[dst, src] += count
        RV1[dst, src] += message_size
    return

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input otf2", default="traces.otf2")
parser.add_argument("-o", "--outfile", help="output npy", default="comm-volumn.npy")
parser.add_argument("--nompi", help="no MPI", action="store_true")
parser.add_argument("-l", "--locations", nargs='*', help="locations", type=int)
parser.add_argument("-i", "--interval_length", help="Specifies the length of an interval in seconds(float).", type=float, default=0.1)
parser.add_argument("-b", "--batch_events", help="batch size", type=float, default=100)
parser.add_argument("--progress2", help="show event progress", action="store_true")
args = parser.parse_args()

comm = None
comm_size = 1
comm_rank = 0
if not args.nompi:
    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    comm_size = comm.size
    comm_rank = comm.rank
else:
    MPI = None
    comm_size = 1
    comm_rank = 0    

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(message)s')

NP = 0
with otf2.reader.open(args.input) as trace:
    wcomm = trace.definitions.comms[0]
    assert(wcomm.name == 'MPI_COMM_WORLD')
    NP = len(wcomm.group.members)
    locations = [x._ref for x in trace.definitions.locations]
    clock_offset = trace.definitions.clock_properties.global_offset

    clock = ClockConverter(trace.definitions.clock_properties)
    length = int(clock.to_ticks(args.interval_length))
    step_count = int(clock.properties.trace_length / length)
    stats = {proc: interval for (proc, interval) in generate_intervals(trace, clock, length)}

## wcomm needs to be re-opened
del wcomm
if comm_rank == 0:
    print("NP: %d"%(NP))
    print("Num. of locations: %d"%(len(locations)))
    print("Created {} intervals of length {} secs".format(step_count, clock.to_sec(length)))

if args.locations is not None:
    locations = args.locations
else:
    locations = locations[comm_rank::comm_size]


# Sent Count/Volume
SC0 = np.zeros((NP, NP), dtype=np.int64)
SV0 = np.zeros((NP, NP), dtype=np.int64)
SC1 = np.zeros((NP, NP), dtype=np.int64)
SV1 = np.zeros((NP, NP), dtype=np.int64)
# Recv Count/Volume
RC0 = np.zeros((NP, NP), dtype=np.int64)
RV0 = np.zeros((NP, NP), dtype=np.int64)
RC1 = np.zeros((NP, NP), dtype=np.int64)
RV1 = np.zeros((NP, NP), dtype=np.int64)

ISEND = np.zeros(NP, dtype=np.int64)
ISENDCOMP = np.zeros(NP, dtype=np.int64)
IRECV = np.zeros(NP, dtype=np.int64)
IRECVRQST = np.zeros(NP, dtype=np.int64)

## checking level
## level 0 (element-wise): SV == RV.T
## level 1a (column-sum-wise): colsum(RV) == colsum(RV.T)
## level 1b (row-sum-wise): rowsum(RV) == rowsum(RV.T)
## level 2 (total sum): np.sum(SV) == np.sum(RV)
## should match column-sum if no_more_sym1a=True
## should match row-sum if no_more_sym1b=True
no_more_sym1a = False
no_more_sym1b = False
no_more_sym2 = False

for ldx in tqdm(locations):
    with otf2.reader.open(args.input, batch_events=args.batch_events) as trace:
        stack = list()
        ## Cannot handle individual error (10/27/2018)
        try:
            for location, event in tqdm(trace.events(trace.definitions.locations[ldx]), disable=(not args.progress2)):
                event_name = type(event).__name__
                
                wcomm = trace.definitions.comms[0]
                assert(wcomm.name == 'MPI_COMM_WORLD')
                mype = wcomm.rank(location)

                lcomm = None
                if hasattr(event, 'communicator'):
                    lcomm = event.communicator
                
                if hasattr(event, 'region'):
                    #print (ldx, mype, event_name, lcomm, event.time, event.region, event)
                    pass
                else:
                    #print (ldx, mype, event_name, lcomm, event.time, event)
                    pass

                ## Region Enter
                if event_name == 'Enter':
                    stack.append(event)
                    #if event.region.name.startswith('MPI'):
                    #    import ipdb; ipdb.set_trace()
                    continue
                ## Region Leave
                elif event_name == 'Leave':
                    collective_op = stack.pop()
                    if hasattr(collective_op, 'data_size_received'):
                        dt = collective_op.data_time_received - collective_op.time
                        throughput = collective_op.data_size_received/dt
                        count = 1.0/dt
                        tree = stats[location.group.name]
                        start = int((collective_op.time-clock.properties.global_offset)/length)*length+clock.properties.global_offset
                        for i in range(start, collective_op.data_time_received, length):
                            interval = get_interval(i, tree)
                            x = max(i, collective_op.time)
                            #print (i, x, count*(min(event.time, interval.end) -x))
                            interval.data.inc_count(count*(min(collective_op.data_time_received, interval.end) -x))
                            interval.data.inc_throughput(throughput)
                    continue
                elif event_name == 'Metric':
                    ## event.value
                    ## x = trace.definitions.metric_members[0]
                    ## x.name, x.description, x.exponent
                    continue
                ## MpiCollective Begin
                elif event_name == 'MpiCollectiveBegin':
                    #import ipdb; ipdb.set_trace()
                    continue
                ## MpiCollective End
                elif event_name == 'MpiCollectiveEnd':
                    if len(lcomm.group.members) == 0:
                        continue

                    ## for througput stat
                    if hasattr(event, 'size_received'): 
                        stack[-1].data_size_received = event.size_received
                        stack[-1].data_time_received = event.time

                    ## MPI_Bcast (all-to-one)
                    if event.collective_op == event.collective_op.BCAST:
                        root = wcomm.rank(lcomm.location(event.root))
                        message_received(mype, root, 1, event.size_received)
                        if (mype == root):
                            for member in lcomm.group.members:
                                peer = wcomm.rank(member)
                                message_sent(root, peer, 1, event.size_sent/len(lcomm.group.members))
                    elif event.collective_op == event.collective_op.SCATTER:
                        root = wcomm.rank(lcomm.location(event.root))
                        message_received(mype, root, 1, event.size_received)
                        if (mype == root):
                            for member in lcomm.group.members:
                                peer = wcomm.rank(member)
                                if event.size_received == 0:
                                    if (peer == root):
                                        message_sent(root, peer, 1, 0)
                                    else:
                                        message_sent(root, peer, 1, event.size_sent/(len(lcomm.group.members)-1))
                                else:
                                    message_sent(root, peer, 1, event.size_sent/len(lcomm.group.members))
                    ## MPI_Gather (all-to-one)
                    ## MPI_Reduce (all-to-one)
                    elif event.collective_op == event.collective_op.GATHER or \
                        event.collective_op == event.collective_op.REDUCE:
                        root = wcomm.rank(lcomm.location(event.root))
                        message_sent(mype, root, 1, event.size_sent)
                        if (mype == root):
                            for member in lcomm.group.members:
                                peer = wcomm.rank(member)
                                message_received(root, peer, 1, event.size_received/len(lcomm.group.members))
                    ## MPI_Allgather (all-to-all)
                    ## MPI_Allreduce (all-to-all)
                    elif event.collective_op == event.collective_op.ALLGATHER or \
                        event.collective_op == event.collective_op.ALLREDUCE or \
                        event.collective_op == event.collective_op.ALLTOALL:
                        for member in lcomm.group.members:
                            peer = wcomm.rank(member)
                            message_sent(mype, peer, 1, event.size_sent/len(lcomm.group.members))
                            message_received(mype, peer, 1, event.size_received/len(lcomm.group.members))
                    elif event.collective_op == event.collective_op.GATHERV:
                        no_more_sym1a = True
                        root = wcomm.rank(lcomm.location(event.root))
                        message_sent(mype, root, 1, event.size_sent)
                        if (mype == root):
                            ## Cannot figure out received data size per peer
                            message_received(root, mype, len(lcomm.group.members), event.size_received)
                    elif event.collective_op == event.collective_op.ALLGATHERV:
                        no_more_sym1a = True
                        for member in lcomm.group.members:
                            peer = wcomm.rank(member)
                            message_sent(mype, peer, 1, event.size_sent/len(lcomm.group.members))

                        ## Cannot figure out received data size per peer
                        message_received(mype, mype, len(lcomm.group.members), event.size_received)
                    ## MPI_Scatterv
                    elif event.collective_op == event.collective_op.SCATTERV:
                        no_more_sym1b = True
                        root = wcomm.rank(lcomm.location(event.root))
                        ## Cannot figure out sent data size per peer
                        ## Instead we use the following:
                        """
                        RC[mype, root] += 1
                        RV[mype, root] += event.size_received
                        if (mype == root):
                            SC[root, mype] += len(lcomm.group.members)
                            SV[root, mype] += event.size_sent
                        """
                        message_sent(root, mype, 1, event.size_received)
                        if (mype == root):
                            message_received(mype, root, len(lcomm.group.members), event.size_sent)
                    ## MPI_Alltoallv
                    elif event.collective_op == event.collective_op.ALLTOALLV:
                        no_more_sym2 = True
                        message_sent(mype, mype, len(lcomm.group.members), event.size_sent)
                        message_received(mype, mype, len(lcomm.group.members), event.size_received)
                    ## MPI_Scan
                    elif event.collective_op == event.collective_op.SCAN:
                        myrank = lcomm.rank(location)

                        peers = range(myrank, len(lcomm.group.members))
                        for i in peers:
                            peer = wcomm.rank(lcomm.location(i))
                            message_sent(mype, peer, 1, event.size_sent/len(peers))

                        peers = range(0, myrank+1)
                        for i in peers:
                            peer = wcomm.rank(lcomm.location(i))
                            message_received(mype, peer, 1, event.size_received/len(peers))
                    ## MPI_Exscan
                    elif event.collective_op == event.collective_op.EXSCAN:
                        myrank = lcomm.rank(location)

                        peers = range(myrank+1, len(lcomm.group.members))
                        for i in peers:
                            peer = wcomm.rank(lcomm.location(i))
                            message_sent(mype, peer, 1, event.size_sent/len(peers))

                        peers = range(0, myrank)
                        for i in peers:
                            peer = wcomm.rank(lcomm.location(i))
                            message_received(mype, peer, 1, event.size_received/len(peers))
                    ## MPI_Reduce_scatter 
                    elif event.collective_op == event.collective_op.REDUCE_SCATTER:
                        no_more_sym1b = True
                        message_sent(mype, mype, len(lcomm.group.members), event.size_sent)
                        for member in lcomm.group.members:
                            peer = wcomm.rank(member)
                            message_received(mype, peer, 1, event.size_received/len(lcomm.group.members))
                    ## MPI_Reduce_scatter_block 
                    elif event.collective_op == event.collective_op.REDUCE_SCATTER_BLOCK:
                        for member in lcomm.group.members:
                            peer = wcomm.rank(member)
                            message_sent(mype, peer, 1, event.size_sent/len(lcomm.group.members))
                        for member in lcomm.group.members:
                            peer = wcomm.rank(member)
                            message_received(mype, peer, 1, event.size_received/len(lcomm.group.members))
                    ## MPI_Barrier
                    elif event.collective_op == event.collective_op.BARRIER:
                        continue
                    else:
                        logging.warn("Unhandled op: %s"%(event))
                ## MpiSend
                elif event_name == 'MpiSend':
                    dst = wcomm.rank(lcomm.location(event.receiver))
                    message_sent(mype, dst, 1, event.msg_length, 1)
                ## MpiRecv
                elif event_name == 'MpiRecv':
                    src = wcomm.rank(lcomm.location(event.sender))
                    message_received(mype, src, 1, event.msg_length, 1)
                ## MpiIsend
                elif event_name == 'MpiIsend':
                    dst = wcomm.rank(lcomm.location(event.receiver))
                    message_sent(mype, dst, 1, event.msg_length, 1)
                    ISEND[mype] += 1
                ## MpiIsendComplete
                elif event_name == 'MpiIsendComplete':
                    ISENDCOMP[mype] += 1
                ## MpiIsend
                elif event_name == 'MpiIrecv':
                    src = wcomm.rank(lcomm.location(event.sender))
                    message_received(mype, src, 1, event.msg_length, 1)
                    IRECV[mype] += 1
                ## MpiIsendComplete
                elif event_name == 'MpiIrecvRequest':
                    IRECVRQST[mype] += 1
                elif event_name == 'MpiRequestTest':
                    continue
                else:
                    logging.warn("Unhandled: %s (%s)"%(event_name, event))
        except _otf2.ErrorCodes.Error as e:
            print ("==> Error:", ldx, type(e).__name__, e)
            continue

start = clock.properties.global_offset
end = start + clock.properties.trace_length
stats_single = IntervalTree(Interval(i, i + length, ThroughputStat()) for i in range(start, end, length))
for group_name in stats.keys():
    tree = stats[group_name]
    for i in tree:
        interval = get_interval(i.begin, stats_single)
        interval.data.inc_count(i.data.count)
        interval.data.inc_throughput(i.data.throughput)

SC0_all = np.zeros_like(SC0)
SV0_all = np.zeros_like(SV0)
RC0_all = np.zeros_like(RC0)
RV0_all = np.zeros_like(RV0)
SC1_all = np.zeros_like(SC1)
SV1_all = np.zeros_like(SV1)
RC1_all = np.zeros_like(RC1)
RV1_all = np.zeros_like(RV1)
ISEND_all = np.zeros_like(ISEND)
ISENDCOMP_all = np.zeros_like(ISENDCOMP)
IRECV_all = np.zeros_like(IRECV)
IRECVRQST_all = np.zeros_like(IRECVRQST)

TP = np.array([ x.data.throughput for x in stats_single ])/clock.to_sec(1)/NP
TP_all = np.zeros_like(TP)

if MPI:
    comm.Reduce(SC0, SC0_all, root=0, op=MPI.SUM)
    comm.Reduce(SV0, SV0_all, root=0, op=MPI.SUM)
    comm.Reduce(RC0, RC0_all, root=0, op=MPI.SUM)
    comm.Reduce(RV0, RV0_all, root=0, op=MPI.SUM)
    comm.Reduce(SC1, SC1_all, root=0, op=MPI.SUM)
    comm.Reduce(SV1, SV1_all, root=0, op=MPI.SUM)
    comm.Reduce(RC1, RC1_all, root=0, op=MPI.SUM)
    comm.Reduce(RV1, RV1_all, root=0, op=MPI.SUM)
    comm.Reduce(ISEND, ISEND_all, root=0, op=MPI.SUM)
    comm.Reduce(IRECV, IRECV_all, root=0, op=MPI.SUM)
    comm.Reduce(ISENDCOMP, ISENDCOMP_all, root=0, op=MPI.SUM)
    comm.Reduce(IRECVRQST, IRECVRQST_all, root=0, op=MPI.SUM)
    comm.Reduce(TP, TP_all, root=0, op=MPI.SUM)
else:
    SC0_all = SC0
    SV0_all = SV0
    RC0_all = RC0
    RV0_all = RV0
    SC1_all = SC1
    SV1_all = SV1
    RC1_all = RC1
    RV1_all = RV1
    ISEND_all = ISEND
    IRECV_all = IRECV
    ISENDCOMP_all = ISENDCOMP
    IRECVRQST_all = IRECVRQST
    TP_all = TP

SC_all = SC0_all + SC1_all
SV_all = SV0_all + SV1_all
RC_all = RC0_all + RC1_all
RV_all = RV0_all + RV1_all

if comm_rank == 0:
    #for i in range(NP+1): print("")
    np.save(args.outfile, SV_all)
    np.save('SC1.npy', SC1_all)
    np.save('SV1.npy', SV1_all)
    np.save('RC1.npy', RC1_all)
    np.save('RV1.npy', RV1_all)
    np.save('SC.npy', SC_all)
    np.save('SV.npy', SV_all)
    np.save('RC.npy', RC_all)
    np.save('RV.npy', RV_all)
    np.save('ISEND.npy', ISEND_all)
    np.save('ISENDCOMP.npy', ISENDCOMP_all)
    np.save('TP.npy', TP_all)
    print('Saved: %s'%(args.outfile))

    if not no_more_sym1a and not no_more_sym1b and not no_more_sym2:
        logging.info('Verifying ... level 0')
        if not np.array_equal(RV_all.T, SV_all):
            logging.warn("Assertion failed; SV")
        if not np.array_equal(RC_all.T, SC_all):
            logging.warn("Assertion failed: SC")
        if not np.array_equal(RV0_all.T, SV0_all):
            logging.warn("Assertion failed; SV0")
        if not np.array_equal(RC0_all.T, SC0_all):
            logging.warn("Assertion failed: SC0")
    elif no_more_sym1a and not no_more_sym1b and not no_more_sym2:
        logging.info('Verying ... level 1a')
        if not np.array_equal(np.sum(SV_all, 0), np.sum(RV_all.T, 0)):
            logging.warn("Assertion failed; SV")
        if not np.array_equal(np.sum(SC_all, 0), np.sum(RC_all.T, 0)):
            logging.warn("Assertion failed; SC")
        if not np.array_equal(np.sum(SV0_all,0 ), np.sum(RV0_all.T, 0)):
            logging.warn("Assertion failed; SV0")
        if not np.array_equal(np.sum(SC0_all,0 ), np.sum(RC0_all.T, 0)):
            logging.warn("Assertion failed; SC0")
    elif not no_more_sym1a and no_more_sym1b and not no_more_sym2:
        logging.info('Verying ... level 1b')
        if not np.array_equal(np.sum(SV_all, 1), np.sum(RV_all.T, 1)):
            logging.warn("Assertion failed; SV")
        if not np.array_equal(np.sum(SC_all, 1), np.sum(RC_all.T, 1)):
            logging.warn("Assertion failed; SC")
        if not np.array_equal(np.sum(SV0_all, 1), np.sum(RV0_all.T, 1)):
            logging.warn("Assertion failed; SV0")
        if not np.array_equal(np.sum(SC0_all, 1), np.sum(RC0_all.T, 1)):
            logging.warn("Assertion failed; SC0")
    else:
        logging.info('Verying ... level 2')
        if np.sum(SV_all) != np.sum(RV_all.T):
            logging.warn("Assertion failed; SV")
        if np.sum(SC_all) != np.sum(RC_all.T):
            logging.warn("Assertion failed; SC")
    if not np.array_equal(ISEND_all, ISENDCOMP_all):
            logging.warn("Assertion failed; ISEND")
    if not np.array_equal(IRECV_all, IRECVRQST_all):
            logging.warn("Assertion failed; IRECV")

    print(">>> SV_all:\n", SV_all)
    print(">>> RV_all:\n", RV_all)
    print(">>> SV1_all:\n", SV1_all)
    print(">>> colsum:\n", np.sum(SV_all, 0))
    print(">>> rowsum:\n", np.sum(SV_all, 1))
    print(">>> sum:\n", np.sum(SV_all))
    print(">>> diff:\n", np.sum(SV_all) - np.sum(RV_all.T))
    print(">>> where:\n", np.where(sum(SV_all) - sum(RV_all.T) != 0))
    print(">>> Collective ratio (%):\n", np.sum(SV0_all)/np.sum(SV_all)*100.0)
    print('Done.')
