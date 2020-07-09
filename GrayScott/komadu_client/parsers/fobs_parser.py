import json, os
from datetime import datetime

from komadu_client.util.util import get_experiment_info, get_workflow_name, get_attributes, get_node_id, \
    get_workflow_version, get_experiment_info, get_cascaded_id
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_VERSION
from komadu_client.models.model_creator import create_workflow_activity
from datetime import datetime
from komadu_client.models.ingest_models import activityActivityType, communicationType
from komadu_client.graphdb.queries import INIT_SWEEP, SINGLE_FOBS_RELATIONSHIP


def parse_fobs_json(filename, workflow_name_main):
    """
    This function passes the fobs.json file and creates the workflow in Komadu.
    :param filename:
    :return:
    """
    with open(filename) as file:
        fobs = json.load(file)

    # file timestamp
    modified_time = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%dT%H:%M:%S')

    print("filename: {}\t time: {}".format(filename, modified_time))

    # extracting the meta information from the filepath
    experiment_id, codesign_name, campaign_name, username, sweepGroup, sweep = get_experiment_info(filename)

    # extracting workflow information
    machine = fobs["machine_name"]
    workflow_name = get_workflow_name(filename)
    if not workflow_name:
        workflow_name = workflow_name_main
    runs = fobs["runs"]
    workflow_node_ids = list(range(len(runs)))

    # Creating the Komadu provenance graph
    komadu_activity_activity_type = create_provenance_graph(experiment_id, fobs, machine, runs, workflow_name,
                                                            workflow_node_ids)
    # creating the
    graph_query = create_meta_graph(username, campaign_name, campaign_name, sweepGroup, sweep, modified_time, machine)
    print(graph_query)

    return komadu_activity_activity_type, graph_query


def create_meta_graph(username, codesign_name, campaign_name, sweepGroup, sweep, modified_time, machine):
    """
    Creates the graph query for the given fobs.json information
    :param username:
    :param codesign_name:parse_fobs_json
    :param campaign_name:
    :param sweepGroup:
    :param sweep:
    :return:
    """
    codesign_id = username + "-" + codesign_name
    campaign_id = codesign_id + "-" + campaign_name
    sweep_group_id = campaign_id + "-" + sweepGroup
    sweep_id = sweep_group_id + "-" + sweep

    # graph_query = "MERGE (user:User{{name:{0} }}) ".format(username)
    graph_query = INIT_SWEEP.format(username, codesign_id, codesign_id, campaign_id, campaign_name, sweep_group_id, sweepGroup, modified_time, machine, sweep_id, sweep, modified_time) + " " + SINGLE_FOBS_RELATIONSHIP

    return graph_query


def create_provenance_graph(experiment_id, fobs, machine, runs, workflow_name, workflow_node_ids):
    """
    Creates the Komadu activity activity graph for the given sweep
    :param experiment_id:
    :param fobs:
    :param machine:
    :param runs:
    :param workflow_name:
    :param workflow_node_ids:
    :return:
    """
    for i in workflow_node_ids:
        if runs[i]["name"] == "simulation":
            simulation_index = i
            workflow_node_ids.remove(i)
            break
    simulation = runs[simulation_index]
    workflow_attributes = {
        "node_layout": flatten_node_layout(fobs["node_layout"]),
        "nprocs": simulation["nprocs"],
        "total_nodes": fobs["total_nodes"],
        "launch_mode": fobs["launch_mode"]
    }
    simulation_name = simulation["name"]
    workflow_version = get_workflow_version(workflow_name)
    simulation_node = create_workflow_activity(experiment_id, get_node_id(experiment_id, simulation_name),
                                               get_node_id(experiment_id, simulation_name),
                                               workflow_name, workflow_version, datetime.now(),
                                               machine, attributes=get_attributes(workflow_attributes))
    # todo: support more than two nodes
    analysis = runs[workflow_node_ids[0]]
    analysis_name = analysis["name"]
    analysis_node = create_workflow_activity(experiment_id, get_node_id(experiment_id, analysis_name),
                                             get_node_id(experiment_id, analysis_name), workflow_name,
                                             workflow_version, datetime.now(), machine)
    komadu_activity_activity_type = get_activity_activity_type(simulation_node, analysis_node)
    return komadu_activity_activity_type


def flatten_node_layout(node_layout):
    final_map = {}
    for i in node_layout:
        final_map.update(i)
    return ', '.join("{!s}={!r}".format(key, val) for (key, val) in final_map.items())


def get_activity_activity_type(node1, node2):
    model = activityActivityType()
    model.activity1 = node1
    model.activity2 = node2
    comm = communicationType()
    comm.informantActivityID = node1.serviceInformation.serviceID
    comm.informedActivityID = node2.serviceInformation.serviceID
    model.communication = comm
    return model
