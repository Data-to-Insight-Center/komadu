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

package edu.indiana.d2i.komadu.util;

import java.io.IOException;

import edu.indiana.d2i.komadu.ingest.AsyncRawNotificationProcessor;
import edu.indiana.d2i.komadu.ingest.IngesterImplementer;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.ingest.db.AttributeFactory;
import edu.indiana.d2i.komadu.ingest.db.AttributeFactory.AttributeDefinitionScopeEnum;
import edu.indiana.d2i.komadu.ingest.db.BaseDBIngester;
import edu.indiana.d2i.komadu.ingest.db.BaseDBIngesterImplementer;
import edu.indiana.d2i.komadu.ingest.db.DBConnectionPool;
import edu.indiana.d2i.komadu.query.QueryImplementer;
import edu.indiana.d2i.komadu.query.db.BaseDBQuerier;
import edu.indiana.d2i.komadu.messaging.MessageConfig;
import edu.indiana.d2i.komadu.messaging.MessageDaemons;
import edu.indiana.d2i.komadu.messaging.MessageDaemonsConfig;

import org.apache.log4j.Logger;
import org.apache.log4j.PropertyConfigurator;

public class ServiceLauncher {

    private static boolean initialized = false;
    private static PropertyReader propertyReader = null;
    private static NotificationIngester ingester = null;
    private static QueryImplementer querier = null;
    private static final Logger log = Logger.getLogger(ServiceLauncher.class);

    public static void start(String propertiesPath) {
        if (!initialized) {
            propertyReader = PropertyReader.getInstance(propertiesPath);
            PropertyConfigurator.configure(propertyReader.getProperty("log4j.properties.path"));

            try {
                populateAttributeScopeDictionary();
                if (log.isDebugEnabled()) log.debug("populated attribute scope dictionary");
                startConnectionPool();
                if (log.isDebugEnabled()) log.debug("started database connection pool");
                createIngester();
                if (log.isDebugEnabled()) log.debug("ingester created");
                startAsyncRawNotificationProcessors();
                if (log.isDebugEnabled()) log.debug("asynchronous raw notification processors started");
                createQuerier();
                if (log.isDebugEnabled()) log.debug("querier created");
                initialized = true;
            } catch (ClassNotFoundException cnfe) {
                log.fatal("FATAL ERROR launching service... exit.", cnfe);
            }

        }
    }

    public static void shutdown() {
        if (initialized) {
            if (log.isDebugEnabled()) log.debug("attempt to shutdown initialized service");
            AsyncRawNotificationProcessor.stop();
            if (log.isDebugEnabled()) log.debug("asynchoronous raw notification processors signaled to stop");
            DBConnectionPool.stop();
            if (log.isDebugEnabled()) log.debug("database connection pool signaled to stop");
            initialized = false;
        }

    }

    public static NotificationIngester getIngester() {
        return ingester;
    }

    public static QueryImplementer getQuerier() {
        return querier;
    }

    public static boolean startMessageReceiverDaemon() {

        String MessagingUsername= propertyReader.getProperty("messaging.username");

        String MessagingPassword= propertyReader.getProperty("messaging.password");

        String MessagingHostname= propertyReader.getProperty("messaging.hostname");

        int MessagingHostPort= Integer.parseInt(propertyReader.getProperty("messaging.hostport"));

        String MessagingVirtualHost= propertyReader.getProperty("messaging.virtualhost");

        String MessagingExchangeName= propertyReader.getProperty("messaging.exchangename")==null? "KarmaExchange": propertyReader.getProperty("messaging.exchangename");

        String MessagingQueueName= propertyReader.getProperty("messaging.queuename")==null? "KarmaQueue": propertyReader.getProperty("messaging.queuename");

        String MessagingRoutingKey= propertyReader.getProperty("messaging.routingkey")==null? "KarmaKey": propertyReader.getProperty("messaging.routingkey");
        
        int MessagingRetryInterval= Integer.parseInt(propertyReader.getProperty("messaging.retry.interval")==null? "5": propertyReader.getProperty("messaging.retry.interval"));
        
        int MessagingRetryThreshold= Integer.parseInt(propertyReader.getProperty("messaging.retry.threshold")==null? "5": propertyReader.getProperty("messaging.retry.threshold"));

        MessageDaemonsConfig msgdmconf=new MessageDaemonsConfig();
        
        msgdmconf.setNumberOfNotificationDaemons(Integer.parseInt(propertyReader.getProperty("messaging.daemon.notification")==null? "1": propertyReader.getProperty("messaging.daemon.notification")));
        
        msgdmconf.setNumberOfQueryDaemons(Integer.parseInt(propertyReader.getProperty("messaging.daemon.query")==null? "1": propertyReader.getProperty("messaging.daemon.query")));
        
        MessageDaemons msgrd;

        MessageConfig msgconf;

        try {

            msgconf=new MessageConfig(MessagingUsername, MessagingPassword, MessagingHostname, MessagingHostPort, MessagingVirtualHost, MessagingExchangeName, MessagingQueueName, MessagingRoutingKey, MessagingRetryInterval, MessagingRetryThreshold);

            msgrd = new MessageDaemons(msgdmconf, msgconf, ingester, querier);

            msgrd.start();

        } catch (IOException e) {

            e.printStackTrace();
            return false;

        } 
        return true;

    }

    private static void startConnectionPool() throws ClassNotFoundException {
        String databaseLocation = propertyReader.getProperty("database.location");
        String databaseUsername = propertyReader.getProperty("database.username");
        String databasePassword = propertyReader.getProperty("database.password");
        int connPoolInitSize = Integer.parseInt(propertyReader.getProperty("conn.pool.init.size"));
        int connPoolMaxSize = Integer.parseInt(propertyReader.getProperty("conn.pool.max.size"));
        long connTimeToLive = Long.parseLong(propertyReader.getProperty("conn.time.to.live.ms"));

        DBConnectionPool.init(databaseLocation, databaseUsername, databasePassword, connPoolInitSize, connPoolMaxSize, connTimeToLive);
        DBConnectionPool.launch();

    }

    private static NotificationIngester createIngester() {
        int processingBatchSize = Integer.parseInt(propertyReader.getProperty("raw.notif.process.batch.size"));

        ingester = new BaseDBIngester(createImplementer(), processingBatchSize);

        return ingester;

    }

    private static QueryImplementer createQuerier() {
        long cacheExpiration = Long.parseLong(propertyReader.getProperty("cache.expiration")) * 60 * 1000; // convert to milliseconds;

        querier = new BaseDBQuerier(cacheExpiration);

        return querier;

    }

    private static IngesterImplementer<Long, String> createImplementer() {
        int rawNotifCacheSize = Integer.parseInt(propertyReader.getProperty("raw.notif.cache.size"));

        IngesterImplementer<Long, String> implementer = new BaseDBIngesterImplementer(rawNotifCacheSize);
        return implementer;
    }

    private static void startAsyncRawNotificationProcessors() {
        int asyncProcessorCount = Integer.parseInt(propertyReader.getProperty("async.processor.thread.count"));
        AsyncRawNotificationProcessor.initialize(asyncProcessorCount, ingester);
    }

    private static void populateAttributeScopeDictionary() {
        int definitionCount = Integer.parseInt(propertyReader.getProperty("attribute.definition.scope.count"));
        for (int i = 0; i < definitionCount; i++) {
            String property = propertyReader.getProperty("attribute.definition.property." + (i + 1));
            String scopeString = propertyReader.getProperty("attribute.definition.scope." + (i + 1));
            AttributeDefinitionScopeEnum scope = AttributeDefinitionScopeEnum.valueOf(scopeString);
            AttributeFactory.addScopeDefinition(property, scope);
        }
    }

    public static void main(String[] args) {
        try {

            if (args.length < 1) {
                System.err.println("ERROR: properties file not specified");
                System.err.println("Usage:  ServiceLauncher <propertiesFilePath>");
                throw new Exception("ERROR: properties file not specified");
            }
            String propertiesFilePath = args[0];
            ServiceLauncher.start(propertiesFilePath);
            if(!ServiceLauncher.startMessageReceiverDaemon()){
            	//If MessageReceiverDaemon can't be started, shall we shutdown the whole Karma Server? If yes, add the code here.
            	shutdown();
            }

        } catch (Throwable e) {
            log.fatal("Unable to launch service", e);
            shutdown();
        }
    }



}
