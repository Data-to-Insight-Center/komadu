package edu.indiana.d2i.komadu.messaging;

import edu.indiana.d2i.komadu.query.*;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.xmlbeans.XmlException;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;

import edu.indiana.d2i.komadu.ingest.IngestException;
import edu.indiana.d2i.komadu.ingest.NotificationIngester;
import edu.indiana.d2i.komadu.ingest.NotificationSummary;
import edu.indiana.d2i.komadu.query.QuerySummary.QueryTypeEnum;
import edu.indiana.d2i.komadu.service.AddActivityActivityRelationshipDocument;
import edu.indiana.d2i.komadu.service.AddActivityEntityRelationshipDocument;
import edu.indiana.d2i.komadu.service.AddAgentActivityRelationshipDocument;
import edu.indiana.d2i.komadu.service.AddAgentAgentRelationshipDocument;
import edu.indiana.d2i.komadu.service.AddAgentEntityRelationshipDocument;
import edu.indiana.d2i.komadu.service.AddAttributesDocument;
import edu.indiana.d2i.komadu.service.AddEntityEntityRelationshipDocument;

/**
 * @author Quan Zhou (quzhou@indiana.edu)
 */

public class KomaduOperations {
    public static final Log l = LogFactory.getLog(KomaduOperations.class);
    public static final String ERROR_STRING = "SERVER ERROR";

    public static void storeNotification(NotificationIngester ingester, NotificationSummary.NotificationTypeEnum
            notificationType, String notification) {

        try {
            switch (notificationType) {
                case ADD_ACTIVITY_ACTIVITY_RELATION:
                    ingester.ingestActivityActivityRelationship(
                            AddActivityActivityRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_AGENT_ACTIVITY_RELATION:
                    ingester.ingestAgentActivityRelationship(
                            AddAgentActivityRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_AGENT_AGENT_RELATION:
                    ingester.ingestAgentAgentRelationship(
                            AddAgentAgentRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_ENTITY_ENTITY_RELATION:
                    ingester.ingestEntityEntityRelationship(
                            AddEntityEntityRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_ACTIVITY_ENTITY_RELATION:
                    ingester.ingestActivityEntityRelationship(
                            AddActivityEntityRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_AGENT_ENTITY_RELATION:
                    ingester.ingestAgentEntityRelationship(
                            AddAgentEntityRelationshipDocument.Factory.parse(notification));
                    return;
                case ADD_ATTRIBUTES:
                    ingester.ingestAddAttributes(
                            AddAttributesDocument.Factory.parse(notification));
                    return;
                case UNKNOWN_TYPES:
                    return;
                default:
            }
        } catch (IngestException e1) {
            e1.printStackTrace();
            l.error("Ingest Exception.");
            l.error(e1.getStackTrace());
        } catch (XmlException e) {
            l.error("XML Exception.");
            l.error(e.getStackTrace());
        }
    }

    public static String queryProvenance(QueryImplementer querier, XmlObject query) {
        try {
            QueryTypeEnum QueryType = QueryTypeEnum.determineQueryTypeFromXmlBeansDocument(query);
            switch (QueryType) {
                case FIND_ACTIVITY:
                    FindActivityResponseDocument findActivityResponseDocument;
                    try {
                        findActivityResponseDocument = querier.findActivity((FindActivityRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findServiceRequest().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return findActivityResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_ACTIVITY_DETAIL:
                    GetActivityDetailResponseDocument getActivityDetailResponseDocument;
                    try {
                        getActivityDetailResponseDocument = querier.getActivityDetail((GetActivityDetailRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findServiceRequest().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getActivityDetailResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case FIND_ENTITY:
                    FindEntityResponseDocument findEntityResponseDocument;
                    try {
                        findEntityResponseDocument = querier.findEntity((FindEntityRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findServiceRequest().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return findEntityResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_ENTITY_DETAIL:
                    GetEntityDetailResponseDocument getEntityDetailResponseDocument;
                    try {
                        getEntityDetailResponseDocument = querier.getEntityDetail((GetEntityDetailRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findServiceRequest().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getEntityDetailResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_CONTEXT_WORKFLOW_GRAPH:
                    GetContextWorkflowGraphResponseDocument getContextWorkflowGraphResponseDocument;
                    try {
                        getContextWorkflowGraphResponseDocument = querier.getContextWorkflowGraph((GetContextWorkflowGraphRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findAbstractDataProduct().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getContextWorkflowGraphResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_ENTITY_GRAPH:
                    GetEntityGraphResponseDocument getEntityGraphResponseDocument;
                    try {
                        getEntityGraphResponseDocument = querier.getEntityGraph((GetEntityGraphRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findAbstractMethod().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getEntityGraphResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_ACTIVITY_GRAPH:
                    GetActivityGraphResponseDocument getActivityGraphResponseDocument;
                    try {
                        getActivityGraphResponseDocument = querier.getActivityGraph((GetActivityGraphRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findAbstractService().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getActivityGraphResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case GET_AGENT_GRAPH:
                    GetAgentGraphResponseDocument getAgentGraphResponseDocument;
                    try {
                        getAgentGraphResponseDocument = querier.getAgentGraph((GetAgentGraphRequestDocument) query);
                    } catch (QueryException qe) {
                        l.error("Error in findDataProduct().");
                        l.error(qe.getMessage());
                        return ERROR_STRING + ": " + qe.getMessage();
                    }
                    return getAgentGraphResponseDocument.xmlText(new XmlOptions().setSavePrettyPrint());
                case UNKNOWN_TYPES:
                    l.error("Unknown query type.");
                    return "Unknown Query";
                default:
                    l.error("Unknown query type.");
                    return "Unknown Query";
            }
        } catch (Exception e) {
            l.error("Error while Querying.", e);
            return "[Exception in queryProvenance]" + e.getMessage();
        }
    }
}
