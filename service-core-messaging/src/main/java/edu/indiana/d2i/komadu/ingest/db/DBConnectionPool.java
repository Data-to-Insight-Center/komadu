/*
#
# Copyright 2014 The Trustees of Indiana University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
*/

package edu.indiana.d2i.komadu.ingest.db;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import edu.indiana.d2i.komadu.common.ObjectPool;
import org.apache.log4j.Logger;

/**
 * @author Yiming Sun
 *
 */
public class DBConnectionPool implements ObjectPool<Connection>, Runnable {

    static class TimedDBConnection {
        private long expireTimestamp = 0L;
        private Connection connection = null;

        TimedDBConnection(String dbLocation, String dbUsername, String dbPassword, long timeToLive) throws SQLException {
            connection = DriverManager.getConnection(dbLocation, dbUsername, dbPassword);
            expireTimestamp = System.currentTimeMillis() + timeToLive;
        }
        long getExpireTimestamp() {
            return expireTimestamp;
        }

        Connection getConnection() {
            return connection;
        }
    }

    static class ExpirationManager implements Runnable {
        private HashMap<Connection, TimedDBConnection> connectionTimeMap;
        private List<Connection> expiredQueue;
        private volatile boolean stopped = true;
        private static Logger log = Logger.getLogger(ExpirationManager.class);
        private static Logger slog = Logger.getLogger("sync.trace");
        private long totalReceived = 0;
        private long totalClosed = 0;
        private long totalNull = 0;

        ExpirationManager(HashMap<Connection, TimedDBConnection> connectionTimeMap, List<Connection> expiredQueue) {
            this.connectionTimeMap = connectionTimeMap;
            this.expiredQueue = expiredQueue;
            totalReceived = 0;
            totalClosed = 0;
            totalNull = 0;
        }

        void stop() {
            stopped = true;
        }

        public void run() {
            log.debug("ExpireMan thread started");
            stopped = false;
            int queueSize = 0;
            Connection connection = null;

            while (!stopped || queueSize > 0) {
                if (queueSize == 0 && !stopped) {
                    if (slog.isTraceEnabled()) slog.trace("ACQing xQ run 1");
                    synchronized(expiredQueue) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed xQ run 1");
                        try {
                            if (slog.isTraceEnabled()) slog.trace("WAIT xQ run 1");
                            expiredQueue.wait();
                            if (slog.isTraceEnabled())slog.trace("OUT xQ run 1");

                        } catch (InterruptedException e) {
                            log.warn("Interrupted", e);
                        }
                        if (slog.isTraceEnabled()) slog.trace("RLS xQ run 1");

                    }

                } else {
                    if (slog.isTraceEnabled()) slog.trace("ACQing xQ run 2");

                    synchronized(expiredQueue) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed xQ run 2");

                        connection = expiredQueue.remove(0);
                        if (slog.isTraceEnabled()) slog.trace("RLS xQ run 2");

                    }

                    if (connection != null) {
                        totalReceived++;
                        if (slog.isTraceEnabled()) slog.trace("ACQing tM run");

                        synchronized(connectionTimeMap) {
                            if (slog.isTraceEnabled()) slog.trace("ACQed tM run");
                            connectionTimeMap.remove(connection);
                            if (slog.isTraceEnabled()) slog.trace("RLS tM run");

                        }

                        try {
                            connection.close();
                            totalClosed++;
                            if (log.isTraceEnabled()) log.trace("1 entry expired and closed");
                        } catch (SQLException e) {
                            log.warn("Unable to close expired connection", e);
                        }
                    } else {
                        totalNull++;
                    }
                }
                if (slog.isTraceEnabled()) slog.trace("ACQing xQ run 3");

                synchronized(expiredQueue) {
                    if (slog.isTraceEnabled()) slog.trace("ACQed xQ run 3");

                    queueSize = expiredQueue.size();
                    if (slog.isTraceEnabled()) slog.trace("RLS tM run 3");

                }


            }
            log.debug("Connections received: " + totalReceived + " Connections Closed: " + totalClosed + " Nulls received: " + totalNull);
            log.debug("Expiration manager stopped");
        }
    }

    public static final int DEFAULT_INIT_POOL_SIZE = 6;
    public static final int DEFAULT_MAX_POOL_SIZE = 10;
    public static final long DEFAULT_TIME_TO_LIVE = 1800000L; // 30 minutes = 1,800,000 ms

    private static Logger log = Logger.getLogger(DBConnectionPool.class);
    private static Logger slog = Logger.getLogger("sync.trace");

    private static int initialPoolSize;
    private static int maxPoolSize;
    private static long timeToLive;
    private static String dbLocation;
    private static String dbUsername;
    private static String dbPassword;

    private static DBConnectionPool instance = null;
    private static ExpirationManager expireManager = null;

    private static boolean initialized = false;

    private static volatile boolean stopped = true;

    private List<TimedDBConnection> freeQueue;
    private List<TimedDBConnection> busyQueue;

    private List<Connection> expiredQueue;
    private HashMap<Connection, TimedDBConnection> connectionTimeMap;
    private List<Object> lockList;
    private Object queueLock;

    private int busyEntryCount = 0;
    private int freeEntryCount = 0;
    private int assignedEntryCount = 0;

    private long totalCreated = 0;
    private long totalDiscarded = 0;
    private long totalNull = 0;

    private DBConnectionPool() {
        assert(initialized);
        boolean success = false;

        freeQueue = new ArrayList<TimedDBConnection>();
        busyQueue = new ArrayList<TimedDBConnection>();
        expiredQueue = new ArrayList<Connection>();

        connectionTimeMap = new HashMap<Connection, TimedDBConnection>();
        lockList = new ArrayList<Object>();
        queueLock = new Object();

        totalCreated = 0;
        totalDiscarded = 0;
        totalNull = 0;

        expireManager = new ExpirationManager(connectionTimeMap, expiredQueue);

        busyEntryCount = 0;
        assignedEntryCount = 0;
        freeEntryCount = 0;

        try {
            for (int i = 0; i < initialPoolSize; i++) {
                replenishPool();
            }
            success = true;
        } catch (SQLException e) {
            log.error("Unable to create pool with given size.", e);
        } finally {
            if (!success) {
                for (TimedDBConnection timedDBConnection : freeQueue) {
                    try {
                        timedDBConnection.getConnection().close();
                    } catch (SQLException e) {
                        log.warn("Unable to close connection.", e);
                    }
                }
            }
        }
    }

    private void replenishPool() throws SQLException {


        TimedDBConnection timedDBConnection = new TimedDBConnection(dbLocation, dbUsername, dbPassword, timeToLive);
        freeQueue.add(timedDBConnection);
        addToConnectionTimeMap(timedDBConnection);
        freeEntryCount++;
        totalCreated++;

    }

    private Connection replenishBusyPool() throws SQLException {


        TimedDBConnection timedDBConnection = new TimedDBConnection(dbLocation, dbUsername, dbPassword, timeToLive);
        busyQueue.add(timedDBConnection);
        addToConnectionTimeMap(timedDBConnection);
        busyEntryCount++;
        totalCreated++;
        return timedDBConnection.getConnection();
    }


    private void addToExpiredQueue(Connection connection) {

        if (slog.isTraceEnabled()) slog.trace("ACQing xQ addxQ");
        synchronized(expiredQueue){
            if (slog.isTraceEnabled()) slog.trace("ACQed xQ addxQ");
            if (connection == null) {
                log.warn("A null added to expire row");
                totalNull++;
            }
            totalDiscarded++;
            expiredQueue.add(connection);

            expiredQueue.notify();
            if (slog.isTraceEnabled()) slog.trace("NFYed xQ addxQ");
            if (slog.isTraceEnabled()) slog.trace("RLS xQ addxQ");
        }

    }


    private void addToConnectionTimeMap(TimedDBConnection timedDBConnection) {
        if (slog.isTraceEnabled()) slog.trace("ACQing tM addtM");

        synchronized(connectionTimeMap) {
            if (slog.isTraceEnabled()) slog.trace("ACQed tM addtM");
            connectionTimeMap.put(timedDBConnection.getConnection(), timedDBConnection);
            if (slog.isTraceEnabled()) slog.trace("RLS tM addtM");

        }
    }

    private TimedDBConnection resolveFromConnectionTimeMap(Connection connection) {
        TimedDBConnection timedDBConnection = null;
        if (slog.isTraceEnabled()) slog.trace("ACQing tM rslvtM");
        synchronized(connectionTimeMap) {
            if (slog.isTraceEnabled()) slog.trace("ACQed tM rslvtM");
            timedDBConnection = connectionTimeMap.get(connection);
            if (slog.isTraceEnabled()) slog.trace("RLS tM rslvtM");

        }

        return timedDBConnection;
    }

    protected Connection checkAndGetConnection() throws SQLException {

        Connection connection = null;

        TimedDBConnection timedDBConnection = freeQueue.remove(0);
        assignedEntryCount--;
        if (System.currentTimeMillis() >= timedDBConnection.getExpireTimestamp()) {
            connection = timedDBConnection.getConnection();
            addToExpiredQueue(connection);
            connection = replenishBusyPool();
        } else {
            connection = timedDBConnection.getConnection();
            if (slog.isTraceEnabled()) slog.trace("ACQing qL cag");

            synchronized(queueLock) {
                if (slog.isTraceEnabled()) slog.trace("ACQed qL cag");

                busyQueue.add(timedDBConnection);
                busyEntryCount++;
                if (slog.isTraceEnabled()) slog.trace("RLS qL cag");

            }

        }

        return connection;
    }

    public static void init(String dbLocation, String dbUsername, String dbPassword, int initialPoolSize, int maxPoolSize, long timeToLive) throws ClassNotFoundException {
        if (!initialized) {
            DBConnectionPool.dbLocation = dbLocation;
            DBConnectionPool.dbUsername = dbUsername;
            DBConnectionPool.dbPassword = dbPassword;
            DBConnectionPool.initialPoolSize = initialPoolSize > 0 ? initialPoolSize : DEFAULT_INIT_POOL_SIZE;
            DBConnectionPool.maxPoolSize = maxPoolSize >= DBConnectionPool.initialPoolSize ? maxPoolSize : (DEFAULT_MAX_POOL_SIZE > DBConnectionPool.initialPoolSize ? DEFAULT_MAX_POOL_SIZE : DBConnectionPool.initialPoolSize);
            DBConnectionPool.timeToLive = timeToLive > 0 ? timeToLive : DEFAULT_TIME_TO_LIVE;

            Class.forName("com.mysql.jdbc.Driver");

            initialized = true;
        }
    }

    public static ObjectPool<Connection> getInstance() {
        if (instance == null) {
            instance = new DBConnectionPool();
        }
        return instance;
    }

    public static void launch() {
        if (instance == null) {
            instance = new DBConnectionPool();
        }
        Thread expThread = new Thread(expireManager, "ExpireMan");
        expThread.start();

        Thread thread = new Thread(instance, "ConnPool");
        thread.start();
    }

    /**
     * @see edu.indiana.d2i.komadu.common.ObjectPool#getEntry()
     */
    public Connection getEntry() {
        Object newLock = new Object();
        Connection connection = null;
        boolean enqueued = false;
        do {
            if (slog.isTraceEnabled()) slog.trace("ACQing tL get");
            synchronized(newLock) {
                if (slog.isTraceEnabled()) slog.trace("ACQed tL get");
                if (!enqueued) {
                    if (slog.isTraceEnabled()) slog.trace("ACQing lL in tL get");

                    synchronized(lockList) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed lL in tL get");
                        lockList.add(newLock);
                        enqueued = true;
                        lockList.notify();
                        if (slog.isTraceEnabled()) slog.trace("NFYed lL in tL get");
                        if (slog.isTraceEnabled()) slog.trace("RLS lL in tL get");

                    }

                }
                try {
                    if (slog.isTraceEnabled()) slog.trace("WAIT tL get");
                    newLock.wait();
                    if (slog.isTraceEnabled()) slog.trace("OUT tL get");
                } catch (InterruptedException e) {
                    log.warn("Interrupted", e);
                }
                if (slog.isTraceEnabled()) slog.trace("RLS tL get");

            }

            if (slog.isTraceEnabled()) slog.trace("ACQing qL get");

            synchronized(queueLock) {
                if (slog.isTraceEnabled()) slog.trace("ACQed qL get");
                try {
                    connection = checkAndGetConnection();
                } catch (SQLException e) {
                    log.warn("Unable to create new connection", e);
                }
                if (slog.isTraceEnabled()) slog.trace("RLS qL get");

            }

        } while (connection == null);


        return connection;
    }

    /**
     * @see edu.indiana.d2i.komadu.common.ObjectPool#releaseEntry(Object)
     */
    public void releaseEntry(Connection entry) {
        if (entry != null) {
            TimedDBConnection timedDBConnection = resolveFromConnectionTimeMap(entry);
            if (timedDBConnection != null) {
                if (System.currentTimeMillis() >= timedDBConnection.getExpireTimestamp()) {
                    addToExpiredQueue(entry);

                    if (slog.isTraceEnabled()) slog.trace("ACQing qL rel 1");

                    synchronized(queueLock) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed qL rel 1");
                        if (busyEntryCount + assignedEntryCount + freeEntryCount > initialPoolSize) {
                            busyQueue.remove(timedDBConnection);
                            busyEntryCount--;
                        } else {
                            busyQueue.remove(timedDBConnection);
                            busyEntryCount--;
                            try {
                                replenishPool();
                                queueLock.notify();
                                if (slog.isTraceEnabled()) slog.trace("NFYed qL rel 1");
                            } catch (SQLException e) {
                                log.error("Unable to create connection. Pool below initial pool size", e);
                            }
                        }
                        if (slog.isTraceEnabled()) slog.trace("RLS qL rel 1");

                    }
                } else {
                    if (slog.isTraceEnabled()) slog.trace("ACQing qL rel 2");

                    synchronized(queueLock) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed qL rel 2");

                        busyQueue.remove(timedDBConnection);
                        busyEntryCount--;
                        freeQueue.add(timedDBConnection);
                        freeEntryCount++;
                        queueLock.notify();
                        if (slog.isTraceEnabled()) slog.trace("NFYed qL rel 2");
                        if (slog.isTraceEnabled()) slog.trace("RLS qL rel 2");
                    }

                }
            } else {
                log.warn("entry resolved to null");
            }
        }
    }

    public static void stop() {
        stopped = true;
        instance.notifyControlLoop();
    }

    private void notifyControlLoop() {
        if (slog.isTraceEnabled()) slog.trace("ACQing lL ncl");

        synchronized(lockList) {
            if (slog.isTraceEnabled()) slog.trace("ACQed lL ncl");
            lockList.notify();
            if (slog.isTraceEnabled()) slog.trace("NFYed lL ncl");
            if (slog.isTraceEnabled()) slog.trace("RLS lL ncl");
        }

        if (slog.isTraceEnabled()) slog.trace("ACQing qL ncl");

        synchronized(queueLock) {
            if (slog.isTraceEnabled()) slog.trace("ACQed qL ncl");
            queueLock.notify();
            if (slog.isTraceEnabled()) slog.trace("NFYed qL ncl");
            if (slog.isTraceEnabled()) slog.trace("RLS qL ncl");

        }

    }

    /**
     * @see java.lang.Runnable#run()
     */
    public void run() {
        stopped = false;
        log.debug("ConnPool control thread started");

        int threadCount = 0;
        int roomToMax = 0;
        int newDemand = 0;

        while (!stopped) {
            if (slog.isTraceEnabled()) slog.trace("ACQing lL pRun");

            synchronized(lockList) {
                if (slog.isTraceEnabled()) slog.trace("ACQed lL pRun");
                threadCount = lockList.size();
                if (threadCount == 0) {
                    try {
                        if (slog.isTraceEnabled()) slog.trace("WAIT lL pRun");
                        lockList.wait();
                        if (slog.isTraceEnabled()) slog.trace("OUT lL pRun");

                        threadCount = lockList.size();
                    } catch (InterruptedException e) {
                        log.warn("Interrupted", e);
                    }
                }
                if (slog.isTraceEnabled()) slog.trace("RLS lL pRun");

            }

            if (slog.isTraceEnabled()) slog.trace("ACQing qL pRun");
            synchronized(queueLock) {
                if (slog.isTraceEnabled()) slog.trace("ACQed qL pRun");

                if (freeEntryCount <= 0) {
                    if (freeEntryCount < 0) log.warn("freeEntryCount subzero: " + freeEntryCount + " assignedEntryCount: " + assignedEntryCount + " busyEntryCount: " + busyEntryCount);

                    if (busyEntryCount + freeEntryCount + assignedEntryCount >= maxPoolSize) {
                        try {
                            if (slog.isTraceEnabled()) slog.trace("WAIT qL pRun");
                            queueLock.wait();
                            if (slog.isTraceEnabled()) slog.trace("OUT qL pRun");

                        } catch (InterruptedException e) {
                            log.warn("Interrupted", e);
                        }
                    } else {
                        roomToMax = maxPoolSize - busyEntryCount - freeEntryCount - assignedEntryCount;
                        newDemand = threadCount - (freeEntryCount);

                        int loop = (newDemand <= roomToMax ? newDemand : roomToMax);

                        if (slog.isTraceEnabled()) slog.trace("thd: " + threadCount + " bsy: " + busyEntryCount + " fre: " + freeEntryCount + " ass: " + assignedEntryCount + " bQ: " + busyQueue.size() + " fQ: " + freeQueue.size() + " rep: " + loop);
                        try {
                            for (int i = 0; i < loop; i++) {
                                replenishPool();
                            }
                        } catch (SQLException e) {
                            log.warn("Unable to create new connection", e);
                        }
                    }
                }


                int loop = (threadCount < freeEntryCount ? threadCount : freeEntryCount);
                if (slog.isTraceEnabled()) slog.trace("thd: " + threadCount + " bsy: " + busyEntryCount + " fre: " + freeEntryCount + " ass: " + assignedEntryCount + " bQ: " + busyQueue.size() + " fQ: " + freeQueue.size() + " rls: " + loop);

                for (int i = 0; i < loop; i++) {
                    Object threadLock = null;
                    if (slog.isTraceEnabled()) slog.trace("ACQing lL in qL pRun");
                    synchronized(lockList) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed lL in qL pRun");
                        threadLock = lockList.remove(0);
                        if (slog.isTraceEnabled()) slog.trace("RLS iL in qL pRun");

                    }

                    if (slog.isTraceEnabled()) slog.trace("ACQing tL in qL pRun");
                    synchronized(threadLock) {
                        if (slog.isTraceEnabled()) slog.trace("ACQed tL in qL pRun");
                        threadLock.notify();
                        if (slog.isTraceEnabled()) slog.trace("NFYed tL in qL pRun");
                        if (slog.isTraceEnabled()) slog.trace("RLS tL in qL pRun");

                    }
                    freeEntryCount--;
                    assignedEntryCount++;

                }
                if (slog.isTraceEnabled()) slog.trace("RLS qL pRun");

            }
        }
        log.debug("Stop signal received");
        int busyCount = 0;
        do {
            if (slog.isTraceEnabled()) slog.trace("ACQing qL pRun 2");

            synchronized(queueLock) {
                if (slog.isTraceEnabled()) slog.trace("ACQed qL pRun 2");
                busyCount = busyQueue.size();
                if (slog.isTraceEnabled()) slog.trace("RLS qL pRun 2");

            }

        } while (busyCount > 0);
        log.debug("No outstanding busy connections");

        if (slog.isTraceEnabled()) slog.trace("ACQing qL pRun 3");

        synchronized(queueLock) {
            if (slog.isTraceEnabled()) slog.trace("ACQed qL pRun 3");

            for (TimedDBConnection timedDBConnection : freeQueue) {
                addToExpiredQueue(timedDBConnection.getConnection());
            }
            if (slog.isTraceEnabled()) slog.trace("RLS qL pRun 3");

        }

        log.debug("All open connections on expire row");
        expireManager.stop();
        log.debug("Connections Created: " + totalCreated +  " Connections Discarded: " + totalDiscarded + " Null sent to expire row: " + totalNull);
        log.debug("ConnPool thread stopped");
    }

}


