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

package edu.indiana.d2i.komadu.ingest;

import org.apache.log4j.Logger;

import java.util.ArrayList;
import java.util.List;

public class AsyncRawNotificationProcessor implements Runnable {
    public static final long PROCESS_DELAY_IN_MS = 1000;
    public static final long MAX_PROCESS_DELAY_IN_MS = 32000L;
    private static List<AsyncRawNotificationProcessor> instances = null;
    private static NotificationIngester ingester = null;
    private volatile static boolean stopProcessing;
    private static Object lock;
    private static Logger log = Logger.getLogger(AsyncRawNotificationProcessor.class);
    private volatile boolean stopped;
    private String id;

    private AsyncRawNotificationProcessor(NotificationIngester ingester, String id) {
        AsyncRawNotificationProcessor.ingester = ingester;
        stopped = true;
        this.id = id;
    }

    public static void initialize(int processorCount, NotificationIngester ingester) {
        if (instances == null) {
            stopProcessing = false;
            lock = new Object();
            instances = new ArrayList<AsyncRawNotificationProcessor>();
            for (int i = 0; i < processorCount; i++) {
                AsyncRawNotificationProcessor processor = new AsyncRawNotificationProcessor(ingester, "AsynProc-" + i);
                instances.add(processor);
                Thread thread = new Thread(processor, processor.getID());
                thread.start();
            }
            log.debug("async processor threads started");
        }
    }

    public static AsyncRawNotificationProcessor getInstance(int index) {
        assert (instances != null) && (index < instances.size());
        log.debug("returning async processor instance " + index);
        return instances.get(index);
    }

    public static void stop() {
        synchronized(lock) {
            stopProcessing = true;
        }
        for (AsyncRawNotificationProcessor processor : instances) {
            while (!processor.isStopped()) {
                if (log.isDebugEnabled()) log.debug(processor.getID() + " not stopped");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    log.warn("Interrupted");
                }
            }
            if (log.isDebugEnabled()) log.debug(processor.getID() + " is stopped");
        }
        instances = null;

    }

    public boolean isStopped() {
        return stopped;
    }

    public String getID() {
        return id;
    }

    public void run() {
        stopped = false;
        int rawCount = 0;
        long sleepLength = PROCESS_DELAY_IN_MS;

        log.debug("Async processor " + id + " started");
        while (!stopProcessing) {
            try {
                rawCount = ingester.processNotifications();
                //log.debug("rawCount: " + rawCount);
                if (rawCount == 0) {
                    try {
                        sleepLength = sleepLength >= MAX_PROCESS_DELAY_IN_MS ? MAX_PROCESS_DELAY_IN_MS : sleepLength * 2;
                        Thread.sleep(PROCESS_DELAY_IN_MS);
                    } catch (InterruptedException e) {
                        log.warn("Interrupted: ", e);
                    }
                }
            } catch (Exception e) {
                log.error("", e);
            }
        }
        log.debug("Async processor " + id + " received stop signal");
        stopped = true;
    }

}
