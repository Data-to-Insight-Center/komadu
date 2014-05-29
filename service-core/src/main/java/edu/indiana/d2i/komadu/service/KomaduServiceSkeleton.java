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

package edu.indiana.d2i.komadu.service;

import edu.indiana.d2i.komadu.ingest.IngestException;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.query.*;
import edu.indiana.d2i.komadu.util.ServiceLauncher;
import org.apache.axis2.AxisFault;
import org.apache.axis2.context.ServiceContext;
import org.apache.axis2.description.AxisService;
import org.apache.axis2.service.Lifecycle;
import org.apache.log4j.Logger;

/**
 * KomaduServiceSkeleton java skeleton for the Komadu Axis2 Service
 */
public class KomaduServiceSkeleton implements KomaduServiceSkeletonInterface, Lifecycle {

    private static Logger log;

    private static NotificationIngester ingester;

    private static QueryImplementer querier;

    private static Boolean initialized = Boolean.FALSE;


    public void init(ServiceContext serviceContext) throws AxisFault {
        if (!initialized) {
            // first initialize the logger
            log = Logger.getLogger(KomaduServiceSkeleton.class);

            if (log.isDebugEnabled())
                log.debug("in init");

            // try load the komadu properties file through a service parameter
            AxisService axisService = serviceContext.getAxisService();
            String propertiesPath = (String) axisService
                    .getParameterValue("komadu.properties.file.path");

            if (propertiesPath != null) {
                // remove potential whitespace introduced in komadu.properties
                propertiesPath = propertiesPath.trim();
                ServiceLauncher.start(propertiesPath);

                ingester = ServiceLauncher.getIngester();
                querier = ServiceLauncher.getQuerier();

                try {
                    ingester.resetUnfinishedNotifications();
                } catch (IngestException e) {
                    log.error("Error resetting unfinished notifications", e);
                }
                initialized = Boolean.TRUE;
            } else {
                log.error("Couldn't initialize Komadu Service, Komadu properties file not found.");
            }
        }
    }

    /**
     * A relationship between 2 Activities
     * Ex : WasInformedBy
     *
     * @param activityActivityRelationship - XMLBean representing the incoming XML
     */
    public void addActivityActivityRelationship(AddActivityActivityRelationshipDocument
                                                        activityActivityRelationship) {
        if (log.isDebugEnabled())
            log.debug(activityActivityRelationship);

        try {
            ingester.ingestActivityActivityRelationship(activityActivityRelationship);
            log.info("Activity-Activity Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Activity-Activity Relationship", ie);
        }

    }

    /**
     * A relationship between an Agent and an Entity
     * Ex : WasAttributedTo
     *
     * @param agentEntityRelationship - XMLBean representing the incoming XML
     */
    public void addAgentEntityRelationship(AddAgentEntityRelationshipDocument
                                                   agentEntityRelationship) {
        if (log.isDebugEnabled())
            log.debug(agentEntityRelationship);
        try {
            ingester.ingestAgentEntityRelationship(agentEntityRelationship);
            log.info("Agent-Entity Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Agent-Entity Relationship", ie);
        }
    }

    /**
     * A relationship between an Agent and an Activity
     * Ex : WasAssociatedWith
     *
     * @param agentActivityRelationship - XMLBean representing the incoming XML
     */
    public void addAgentActivityRelationship(AddAgentActivityRelationshipDocument
                                                     agentActivityRelationship) {
        if (log.isDebugEnabled())
            log.debug(agentActivityRelationship);

        try {
            ingester.ingestAgentActivityRelationship(agentActivityRelationship);
            log.info("Agent-Activity Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Agent-Activity Relationship", ie);
        }
    }

    /**
     * A relationship between two Agents
     * Ex : ActedOnBehalfOf
     *
     * @param agentAgentRelationship - XMLBean representing the incoming XML
     */
    public void addAgentAgentRelationship(AddAgentAgentRelationshipDocument
                                                  agentAgentRelationship) {
        if (log.isDebugEnabled())
            log.debug(agentAgentRelationship);

        try {
            ingester.ingestAgentAgentRelationship(agentAgentRelationship);
            log.info("Agent-Agent Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Agent-Agent Relationship", ie);
        }
    }

    /**
     * A relationship between two Entities
     * Ex : WasDerivedFrom
     *
     * @param entityEntityRelationship - XMLBean representing the incoming XML
     */
    public void addEntityEntityRelationship(AddEntityEntityRelationshipDocument
                                                    entityEntityRelationship) {
        if (log.isDebugEnabled())
            log.debug(entityEntityRelationship);

        try {
            ingester.ingestEntityEntityRelationship(entityEntityRelationship);
            log.info("Entity-Entity Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Entity-Entity Relationship", ie);
        }
    }

    /**
     * A relationship between an Activity and an Entity
     * Ex : Used
     *
     * @param activityEntityRelationship - XMLBean representing the incoming XML
     */
    public void addActivityEntityRelationship(AddActivityEntityRelationshipDocument
                                                      activityEntityRelationship) {
        if (log.isDebugEnabled())
            log.debug(activityEntityRelationship);

        try {
            ingester.ingestActivityEntityRelationship(activityEntityRelationship);
            log.info("Activity-Entity Relationship Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest Activity-Entity Relationship", ie);
        }
    }

    public void addAttributes(AddAttributesDocument addAttributes) {
        if (log.isDebugEnabled())
            log.debug(addAttributes);

        try {
            ingester.ingestAddAttributes(addAttributes);
            log.info("New Attributes Added..");
        } catch (IngestException ie) {
            log.error("Failed to ingest new Attributes", ie);
        }
    }

//    @Override
//    public GetAbstractMethodDetailResponseDocument getAbstractMethodDetail(
//            GetAbstractMethodDetailRequestDocument getAbstractMethodDetailRequest) {
//        if (log.isDebugEnabled())
//            log.debug(getAbstractMethodDetailRequest);
//
//        log.error("Operation not implemented..");
//        return null;
//    }
//
//    @Override
//    public FindAbstractEntityResponseDocument findAbstractEntity(
//            FindAbstractEntityRequestDocument findAbstractEntityRequest) {
//        return null;
//    }
//
//    @Override
//    public FindAbstractServiceResponseDocument findAbstractService(
//            FindAbstractServiceRequestDocument findAbstractServiceRequest) {
//        if (log.isDebugEnabled())
//            log.debug(findAbstractServiceRequest);
//
//        log.error("Operation not implemented..");
//        return null;
//    }

    @Override
    public GetEntityDetailResponseDocument getEntityDetail(
            GetEntityDetailRequestDocument getEntityDetailRequest) {
        if (log.isDebugEnabled())
            log.debug(getEntityDetailRequest);

        GetEntityDetailResponseDocument getEntityDetailResponseDocument = null;
        try {
            getEntityDetailResponseDocument = querier.getEntityDetail(getEntityDetailRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getEntityDetail");
        }
        return getEntityDetailResponseDocument;
    }

//    @Override
//    public GetAbstractEntityDetailResponseDocument getAbstractEntityDetail(
//            GetAbstractEntityDetailRequestDocument getAbstractEntityDetailRequest) {
//        if (log.isDebugEnabled())
//            log.debug(getAbstractEntityDetailRequest);
//
//        log.error("Operation not implemented..");
//        return null;
//    }
//
//    @Override
//    public FindAbstractMethodResponseDocument findAbstractMethod(
//            FindAbstractMethodRequestDocument findAbstractMethodRequest) {
//        if (log.isDebugEnabled())
//            log.debug(findAbstractMethodRequest);
//
//        log.error("Operation not implemented..");
//        return null;
//    }

    @Override
    public GetActivityDetailResponseDocument getActivityDetail(
            GetActivityDetailRequestDocument getActivityDetailRequest) {
        if (log.isDebugEnabled())
            log.debug(getActivityDetailRequest);

        GetActivityDetailResponseDocument getActivityDetailResponseDocument = null;
        try {
            getActivityDetailResponseDocument = querier.getActivityDetail(getActivityDetailRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getActivityDetail");
        }
        return getActivityDetailResponseDocument;
    }

//    @Override
//    public GetAbstractServiceDetailResponseDocument getAbstractServiceDetail(
//            GetAbstractServiceDetailRequestDocument getAbstractServiceDetailRequest) {
//        if (log.isDebugEnabled())
//            log.debug(getAbstractServiceDetailRequest);
//
//        log.error("Operation not implemented..");
//        return null;
//    }

    @Override
    public FindEntityResponseDocument findEntity(FindEntityRequestDocument findEntityRequest) {
        if (log.isDebugEnabled())
            log.debug(findEntityRequest);

        FindEntityResponseDocument findEntityResponseDocument = null;
        try {
            findEntityResponseDocument = querier.findEntity(findEntityRequest);
        } catch (QueryException qe) {
            log.error("Failed to query findEntity");
        }
        return findEntityResponseDocument;
    }

    @Override
    public FindActivityResponseDocument findActivity(FindActivityRequestDocument findActivityRequest) {
        if (log.isDebugEnabled())
            log.debug(findActivityRequest);
        
        FindActivityResponseDocument findActivityResponseDocument = null;
        try {
            findActivityResponseDocument = querier.findActivity(findActivityRequest);
        } catch (QueryException qe) {
            log.error("Failed to query findActivity");
        }
        return findActivityResponseDocument;
    }

    @Override
    public GetContextWorkflowGraphResponseDocument getContextWorkflowGraph(
            GetContextWorkflowGraphRequestDocument getWorkflowGraphRequest) {
        if (log.isDebugEnabled())
            log.debug(getWorkflowGraphRequest);
        
        GetContextWorkflowGraphResponseDocument getContextWorkflowGraphResponseDocument = null;

        try {
            getContextWorkflowGraphResponseDocument = querier
                    .getContextWorkflowGraph(getWorkflowGraphRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getContextWorkflowGraph");
        }

        return getContextWorkflowGraphResponseDocument;
    }

    @Override
    public GetEntityGraphResponseDocument getEntityGraph(
            GetEntityGraphRequestDocument getEntityGraphRequest) {
        if (log.isDebugEnabled())
            log.debug(getEntityGraphRequest);
        
        GetEntityGraphResponseDocument getEntityGraphResponseDocument = null;

        try {
            getEntityGraphResponseDocument = querier.getEntityGraph(getEntityGraphRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getEntityGraph");
        }

        return getEntityGraphResponseDocument;
    }

    @Override
    public GetAgentGraphResponseDocument getAgentGraph(
            GetAgentGraphRequestDocument getAgentGraphRequest) {
        if (log.isDebugEnabled())
            log.debug(getAgentGraphRequest);
        
        GetAgentGraphResponseDocument getAgentGraphResponseDocument = null;

        try {
            getAgentGraphResponseDocument = querier.getAgentGraph(getAgentGraphRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getAgentGraph");
        }

        return getAgentGraphResponseDocument;
    }

    @Override
    public GetActivityGraphResponseDocument getActivityGraph(
            GetActivityGraphRequestDocument getActivityGraphRequest) {
        if (log.isDebugEnabled())
            log.debug(getActivityGraphRequest);
        
        GetActivityGraphResponseDocument getActivityGraphResponseDocument = null;

        try {
            getActivityGraphResponseDocument = querier
                    .getActivityGraph(getActivityGraphRequest);
        } catch (QueryException qe) {
            log.error("Failed to query getContextWorkflowGraph");
        }

        return getActivityGraphResponseDocument;
    }

    public void destroy(ServiceContext serviceContext) {
        log.info("Destroying Komadu Service");
        initialized = Boolean.FALSE;
        ServiceLauncher.shutdown();
    }
}

