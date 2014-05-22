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

package edu.indiana.d2i.komadu.query.db;

import edu.indiana.d2i.komadu.ingest.db.DBConnectionPool;
import edu.indiana.d2i.komadu.query.*;
import edu.indiana.d2i.komadu.query.graph.*;
import edu.indiana.d2i.komadu.service.AttributesType;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.xmlbeans.XmlString;
import org.w3.www.ns.prov.Document;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class BaseDBQuerier implements QueryImplementer {

    public BaseDBQuerier(long cacheExpiration) {
        this.cacheExpiration = cacheExpiration;
    }

    public static final Log l = LogFactory.getLog(BaseDBQuerier.class);
    private long cacheExpiration = 0;

    public FindServiceResponseDocument findService(FindServiceRequestDocument findServiceRequest)
            throws QueryException {
        Connection connection = DBConnectionPool.getInstance().getEntry();
        FindServiceResponseDocument response = null;
        try {
            response = findService(connection, findServiceRequest.getFindServiceRequest());
        } catch (SQLException e) {
            l.error("Error while executing findService()", e);
        }
        return response;
    }

    public GetContextWorkflowGraphResponseDocument getContextWorkflowGraph(
            GetContextWorkflowGraphRequestDocument getWorkflowGraphRequest) throws QueryException {
        l.debug("Entering getContextWorkflowGraph()");
        Connection connection = null;

        GetContextWorkflowGraphRequestType getWorkflowGraphRequestType = getWorkflowGraphRequest
                .getGetContextWorkflowGraphRequest();
        String workflowID = getWorkflowGraphRequestType.getContextWorkflowURI();
        DetailEnumType.Enum informationDetailLevel;

        GetContextWorkflowGraphResponseDocument getWorkflowGraphResponseDocument =
                GetContextWorkflowGraphResponseDocument.Factory.newInstance();
        GetContextWorkflowGraphResponseType getWorkflowGraphResponseType =
                getWorkflowGraphResponseDocument.addNewGetContextWorkflowGraphResponse();

        if (!getWorkflowGraphRequestType.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = getWorkflowGraphRequestType.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new ContextGraphGenerator();
            Document graph = generator.getProvGraph(connection, workflowID, informationDetailLevel,
                    QueryConstants.CONTEXT_GRAPH_CACHE_PREFIX, cacheExpiration);
            getWorkflowGraphResponseType.setDocument(graph);

//            if (format.equals(FormatEnumType.RDF)) {
//                RdfType rdf = null;
//                getWorkflowGraphResponseType.setRDF(rdf);
//            }
//            l.debug("getWorkflowGraphResponseDocument validation: "
//                    + getWorkflowGraphResponseDocument.validate());

            l.debug("Completed getContextWorkflowGraph()");
        } catch (Exception e) {
            l.error("Failed to query getContextWorkflowGraph()", e);
        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getWorkflowGraphResponseDocument;
    }

    @Override
    public GetEntityGraphResponseDocument getEntityGraph(
            GetEntityGraphRequestDocument getEntityGraphRequest) throws QueryException {
        l.debug("Entering getEntityGraph()");
        Connection connection = null;

        GetEntityGraphRequestType entityGraphRequest = getEntityGraphRequest
                .getGetEntityGraphRequest();
        String entityURI = entityGraphRequest.getEntityURI();
        DetailEnumType.Enum informationDetailLevel;

        GetEntityGraphResponseDocument getEntityGraphResponseDocument =
                GetEntityGraphResponseDocument.Factory.newInstance();
        GetEntityGraphResponseType getEntityGraphResponseType =
                getEntityGraphResponseDocument.addNewGetEntityGraphResponse();

        if (!entityGraphRequest.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = entityGraphRequest.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new EntityGraphGenerator(entityGraphRequest.getEntityType());
            Document graph = generator.getProvGraph(connection, entityURI, informationDetailLevel,
                    QueryConstants.ENTITY_GRAPH_CACHE_PREFIX, cacheExpiration);
            getEntityGraphResponseType.setDocument(graph);

            l.debug("Completed getEntityGraph()");
        } catch (Exception e) {
            l.error("Failed to query getEntityGraph()", e);

        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getEntityGraphResponseDocument;
    }

    @Override
    public GetActivityGraphResponseDocument getActivityGraph(
            GetActivityGraphRequestDocument getActivityGraphRequest) throws QueryException {
        l.debug("Entering getActivityGraph()");
        Connection connection = null;

        GetActivityGraphRequestType getWorkflowGraphRequestType = getActivityGraphRequest
                .getGetActivityGraphRequest();
        String activityURI = getWorkflowGraphRequestType.getActivityURI();
        DetailEnumType.Enum informationDetailLevel;

        GetActivityGraphResponseDocument getWorkflowGraphResponseDocument =
                GetActivityGraphResponseDocument.Factory.newInstance();
        GetActivityGraphResponseType getWorkflowGraphResponseType =
                getWorkflowGraphResponseDocument.addNewGetActivityGraphResponse();

        if (!getWorkflowGraphRequestType.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = getWorkflowGraphRequestType.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new ActivityGraphGenerator();
            Document graph = generator.getProvGraph(connection, activityURI, informationDetailLevel,
                    QueryConstants.ACTIVITY_GRAPH_CACHE_PREFIX, cacheExpiration);
            getWorkflowGraphResponseType.setDocument(graph);

            l.debug("Completed getActivityGraph()");
        } catch (Exception e) {
            l.error("Failed to query getActivityGraph()", e);

        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getWorkflowGraphResponseDocument;
    }

    @Override
    public GetAgentGraphResponseDocument getAgentGraph(GetAgentGraphRequestDocument getAgentGraphRequest)
            throws QueryException {
        l.debug("Entering getAgentGraph()");
        Connection connection = null;

        GetAgentGraphRequestType agentGraphRequest = getAgentGraphRequest
                .getGetAgentGraphRequest();
        String agentURI = agentGraphRequest.getAgentID();
        DetailEnumType.Enum informationDetailLevel;

        GetAgentGraphResponseDocument getAgentGraphResponseDocument =
                GetAgentGraphResponseDocument.Factory.newInstance();
        GetAgentGraphResponseType getAgentGraphResponseType =
                getAgentGraphResponseDocument.addNewGetAgentGraphResponse();

        if (!agentGraphRequest.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = agentGraphRequest.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new AgentGraphGenerator();
            Document graph = generator.getProvGraph(connection, agentURI, informationDetailLevel,
                    QueryConstants.AGENT_GRAPH_CACHE_PREFIX, cacheExpiration);
            getAgentGraphResponseType.setDocument(graph);

            l.debug("Completed getAgentGraph()");
        } catch (Exception e) {
            l.error("Failed to query getAgentGraph()", e);

        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getAgentGraphResponseDocument;
    }

    public FindServiceResponseDocument findService(Connection connection, FindServiceRequestType
            findServiceRequestType) throws QueryException, SQLException {

        l.debug("Entering findService()");
        assert (connection != null);
        assert (findServiceRequestType != null);

        PreparedStatement findServiceStmt = null;
        ResultSet res = null;

        FindServiceResponseDocument findServiceResponseDocument = FindServiceResponseDocument.Factory
                .newInstance();
        FindServiceResponseType findServiceResponseType = findServiceResponseDocument
                .addNewFindServiceResponse();
        ServiceIDListType serviceNameList = findServiceResponseType.addNewServiceIDList();

        try {
            StringBuilder query = new StringBuilder();
            if (findServiceRequestType.isSetAttributeList()) {
                query.append(PROVSqlQuery.FIND_SERVICE_ATTRIBUTE);
            } else {
                query.append(PROVSqlQuery.FIND_SERVICE);
            }

            String nextService = findServiceRequestType.getNextServiceID();
            String nextServiceID;
            if (nextService != null) {
                PreparedStatement findNextServiceStmt;
                if (nextService.startsWith(QueryConstants.ACTIVITY_IDENTIFIER)) {
                    // if the service id is provided
                    nextService = nextService.replace(QueryConstants.ACTIVITY_IDENTIFIER, "");
                    findNextServiceStmt = connection.prepareStatement(PROVSqlQuery.GET_SERVICE_BY_ID);
                } else {
                    // there the uri is provided
                    findNextServiceStmt = connection.prepareStatement(PROVSqlQuery.GET_SERVICE_BY_URI);
                }
                findNextServiceStmt.setString(1, nextService);
                ResultSet nextServiceRes = findNextServiceStmt.executeQuery();

                int nextServiceCount = 0;
                if (nextServiceRes.next()) {
                    nextServiceID = nextServiceRes.getString(1);
                    query.append("AND c.informed_id LIKE ").append(nextServiceID).append(" ");
                    nextServiceCount++;
                }

                nextServiceRes.close();
                findNextServiceStmt.close();

                if (nextServiceCount == 0) {
                    l.info("No service with specified next service found.");
                    l.debug("Exiting findService() with success.");
                    return findServiceResponseDocument;
                }
            }

            String architecture = findServiceRequestType.getArchitecture();
            String hostName = findServiceRequestType.getHostName();
            String name = findServiceRequestType.getName();
            String workflowID = findServiceRequestType.getWorkflowID();
            String subServiceID = findServiceRequestType.getSubServiceID();
//            Calendar initializationTime = findServiceRequestType.getInitializationTime();
//            Calendar terminationTime = findServiceRequestType.getTerminationTime();
//            boolean isSuccess = findServiceRequestType.getIsSuccess();
            AttributesType attributeList = findServiceRequestType.getAttributeList();

            if (findServiceRequestType.isSetArchitecture())
                query.append("AND a.activity_uri LIKE '%").append(architecture).append("%' ");
            if (findServiceRequestType.isSetHostName())
                query.append("AND a.activity_uri LIKE '%").append(hostName).append("%' ");
            if (findServiceRequestType.isSetName())
                query.append("AND a.activity_uri LIKE '%").append(name).append("%' ");
            if (findServiceRequestType.isSetWorkflowID())
                query.append("AND a.context_workflow_uri LIKE '%").append(workflowID).append("%' ");
            if (findServiceRequestType.isSetSubServiceID())
                query.append("AND a.context_service_uri LIKE '%").append(subServiceID).append("%' ");
            // TODO : Add invocation time, termination time and status into communication?
//            if (findServiceRequestType.isSetInitializationTime())
//                query.append("AND i.invocation_start_time LIKE '%").append(initializationTime).append("%' ");
//            if (findServiceRequestType.isSetTerminationTime())
//                query.append("AND i.execution_end_time LIKE '%").append(terminationTime).append("%' ");
//
//            // default to SUCCESS if not specified
//            l.debug("isSetIsSuccess: " + findServiceRequestType.isSetIsSuccess());
//            if (!findServiceRequestType.isSetIsSuccess())
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.SUCCESS.toString() + "' ");
//            else if (isSuccess)
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.SUCCESS.toString() + "' ");
//            else
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.FAILED.toString() + "' ");

            if (findServiceRequestType.isSetAttributeList()) {
                for (int i = 0; i < attributeList.sizeOfAttributeArray(); i++) {
                    query.append(PROVSqlQuery.ATTRIBUTE_COMPARISON);
                }
            }

            findServiceStmt = connection.prepareStatement(query.toString());
            l.debug("findServiceStmt: " + findServiceStmt);

            if (findServiceRequestType.isSetAttributeList()) {
                for (int i = 1; i <= attributeList.sizeOfAttributeArray(); i++) {
                    findServiceStmt.setString(i, '%' + findServiceRequestType
                            .getAttributeList().getAttributeArray(i).getValue() + '%');
                }
            }
            res = findServiceStmt.executeQuery();
            while (res.next()) {
                XmlString serviceName = serviceNameList.addNewServiceID();
                serviceName.setStringValue(res.getString("activity_uri"));
            }
            res.close();
            findServiceStmt.close();
        } catch (SQLException e) {
            l.error("Exiting findService() with SQL errors.");
            l.error(e.toString());
            return null;
        } finally {
            if (findServiceStmt != null) {
                findServiceStmt.close();
            }
            if (res != null) {
                res.close();
            }
        }
        l.debug("Response: " + findServiceResponseDocument);
        l.debug("Exiting findService() with success.");
        return findServiceResponseDocument;
    }

}
