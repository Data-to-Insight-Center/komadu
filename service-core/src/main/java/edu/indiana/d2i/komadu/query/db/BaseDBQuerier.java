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
import edu.indiana.d2i.komadu.util.KomaduUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.xmlbeans.XmlString;
import org.w3.www.ns.prov.Document;

import java.sql.*;
import java.util.Calendar;


public class BaseDBQuerier implements QueryImplementer {

    public BaseDBQuerier(long cacheExpiration) {
        this.cacheExpiration = cacheExpiration;
    }

    public static final Log l = LogFactory.getLog(BaseDBQuerier.class);
    private long cacheExpiration = 0;

    public FindActivityResponseDocument findActivity(FindActivityRequestDocument findActivityRequest)
            throws QueryException {
        Connection connection = DBConnectionPool.getInstance().getEntry();
        FindActivityResponseDocument response = null;
        try {
            response = findActivity(connection, findActivityRequest.getFindActivityRequest());
        } catch (SQLException e) {
            l.error("Error while executing findActivity()", e);
        }
        return response;
    }

    @Override
    public FindEntityResponseDocument findEntity(FindEntityRequestDocument findEntityRequest)
            throws QueryException {
        Connection connection = DBConnectionPool.getInstance().getEntry();
        FindEntityResponseDocument response = null;
        try {
            response = findEntity(connection, findEntityRequest.getFindEntityRequest());
        } catch (SQLException e) {
            l.error("Error while executing findEntity()", e);
        }
        return response;
    }

    @Override
    public GetActivityDetailResponseDocument getActivityDetail(
            GetActivityDetailRequestDocument getActivityDetailRequest) throws QueryException {
        Connection connection = DBConnectionPool.getInstance().getEntry();
        GetActivityDetailResponseDocument response = null;
        try {
            response = getActivityDetail(connection, getActivityDetailRequest.getGetActivityDetailRequest());
        } catch (SQLException e) {
            l.error("Error while executing getActivityDetail()", e);
        }
        return response;
    }

    @Override
    public GetEntityDetailResponseDocument getEntityDetail(
            GetEntityDetailRequestDocument getEntityDetailRequest) throws QueryException {
        Connection connection = DBConnectionPool.getInstance().getEntry();
        GetEntityDetailResponseDocument response = null;
        try {
            response = getEntityDetail(connection,
                    getEntityDetailRequest.getGetEntityDetailRequest().getEntityIDList());
        } catch (SQLException e) {
            l.error("Error while executing getEntityDetail()", e);
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
    public GetEntityForwardGraphResponseDocument getEntityForwardGraph(
            GetEntityForwardGraphRequestDocument getEntityForwardGraphRequest) throws QueryException {
        l.debug("Entering getEntityForwardGraph()");
        Connection connection = null;

        GetEntityGraphRequestType entityGraphRequest = getEntityForwardGraphRequest
                .getGetEntityForwardGraphRequest();
        String entityURI = entityGraphRequest.getEntityURI();
        DetailEnumType.Enum informationDetailLevel;

        GetEntityForwardGraphResponseDocument getEntityForwardGraphResponseDocument =
                GetEntityForwardGraphResponseDocument.Factory.newInstance();
        GetEntityGraphResponseType getEntityGraphResponseType =
                getEntityForwardGraphResponseDocument.addNewGetEntityForwardGraphResponse();

        if (!entityGraphRequest.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = entityGraphRequest.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new EntityForwardProvGenerator(entityGraphRequest.getEntityType());
            Document graph = generator.getProvGraph(connection, entityURI, informationDetailLevel,
                    QueryConstants.ENTITY_GRAPH_CACHE_PREFIX, cacheExpiration);
            getEntityGraphResponseType.setDocument(graph);

            l.debug("Completed getEntityForwardGraph()");
        } catch (Exception e) {
            l.error("Failed to query getEntityForwardGraph()", e);

        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getEntityForwardGraphResponseDocument;
    }

    @Override
    public GetEntityBackwardGraphResponseDocument getEntityBackwardGraph(
            GetEntityBackwardGraphRequestDocument getEntityBackwardGraphRequest) throws QueryException {
        l.debug("Entering getEntityBackwardGraph()");
        Connection connection = null;

        GetEntityGraphRequestType entityGraphRequest = getEntityBackwardGraphRequest
                .getGetEntityBackwardGraphRequest();
        String entityURI = entityGraphRequest.getEntityURI();
        DetailEnumType.Enum informationDetailLevel;

        GetEntityBackwardGraphResponseDocument getEntityBackwardGraphResponseDocument =
                GetEntityBackwardGraphResponseDocument.Factory.newInstance();
        GetEntityGraphResponseType getEntityGraphResponseType =
                getEntityBackwardGraphResponseDocument.addNewGetEntityBackwardGraphResponse();

        if (!entityGraphRequest.isSetInformationDetailLevel()) {
            informationDetailLevel = DetailEnumType.COARSE;
        } else {
            informationDetailLevel = entityGraphRequest.getInformationDetailLevel();
        }

        try {
            connection = DBConnectionPool.getInstance().getEntry();
            GraphGenerator generator = new EntityBackwardProvGenerator(entityGraphRequest.getEntityType());
            Document graph = generator.getProvGraph(connection, entityURI, informationDetailLevel,
                    QueryConstants.ENTITY_GRAPH_CACHE_PREFIX, cacheExpiration);
            getEntityGraphResponseType.setDocument(graph);

            l.debug("Completed getEntityBackwardGraph()");
        } catch (Exception e) {
            l.error("Failed to query getEntityBackwardGraph()", e);

        } finally {
            if (connection != null) {
                DBConnectionPool.getInstance().releaseEntry(connection);
            }
        }

        return getEntityBackwardGraphResponseDocument;
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

    public FindActivityResponseDocument findActivity(Connection connection, FindActivityRequestType
            findActivityRequestType) throws QueryException, SQLException {

        l.debug("Entering findActivity()");
        assert (connection != null);
        assert (findActivityRequestType != null);

        PreparedStatement findActivityStmt = null;
        ResultSet res = null;

        FindActivityResponseDocument findActivityResponseDocument = FindActivityResponseDocument.Factory
                .newInstance();
        FindActivityResponseType findActivityResponseType = findActivityResponseDocument
                .addNewFindActivityResponse();
        ActivityIDListType activityIDListType = findActivityResponseType.addNewActivityIDList();

        try {
            StringBuilder query = new StringBuilder();
            if (findActivityRequestType.isSetAttributeList()) {
                if (findActivityRequestType.isSetNextActivityID())
                    query.append(PROVSqlQuery.FIND_ACTIVITY_ATTRIBUTE_COMM);
                else
                    query.append(PROVSqlQuery.FIND_ACTIVITY_ATTRIBUTE);
            } else {
                if (findActivityRequestType.isSetNextActivityID())
                    query.append(PROVSqlQuery.FIND_ACTIVITY_COMM);
                else
                    query.append(PROVSqlQuery.FIND_ACTIVITY);
            }

            String nextActivity = findActivityRequestType.getNextActivityID();
            String nextActivityID;
            if (nextActivity != null) {
                PreparedStatement findNextActivityStmt;
                if (nextActivity.startsWith(QueryConstants.ACTIVITY_IDENTIFIER)) {
                    // if the activity id is provided
                    nextActivity = nextActivity.replace(QueryConstants.ACTIVITY_IDENTIFIER, "");
                    findNextActivityStmt = connection.prepareStatement(PROVSqlQuery.GET_ACTIVITY_BY_ID);
                } else {
                    // there the uri is provided
                    findNextActivityStmt = connection.prepareStatement(PROVSqlQuery.GET_ACTIVITY_BY_URI);
                }
                findNextActivityStmt.setString(1, nextActivity);
                ResultSet nextActivityRes = findNextActivityStmt.executeQuery();

                int nextActivityCount = 0;
                if (nextActivityRes.next()) {
                    nextActivityID = nextActivityRes.getString(1);
                    query.append("AND c.informed_id = '").append(nextActivityID).append("' ");
                    nextActivityCount++;
                }

                nextActivityRes.close();
                findNextActivityStmt.close();

                if (nextActivityCount == 0) {
                    l.info("No activity with specified next activity found.");
                    l.debug("Exiting findActivity() with success.");
                    return findActivityResponseDocument;
                }
            }

            String architecture = findActivityRequestType.getArchitecture();
            String hostName = findActivityRequestType.getHostName();
            String name = findActivityRequestType.getName();
            String workflowID = findActivityRequestType.getWorkflowID();
            String serviceID = findActivityRequestType.getServiceID();
//            Calendar initializationTime = findActivityRequestType.getInitializationTime();
//            Calendar terminationTime = findActivityRequestType.getTerminationTime();
//            boolean isSuccess = findActivityRequestType.getIsSuccess();
            AttributesType attributeList = findActivityRequestType.getAttributeList();

            if (findActivityRequestType.isSetArchitecture())
                query.append("AND a.activity_uri LIKE '%").append(architecture).append("%' ");
            if (findActivityRequestType.isSetHostName())
                query.append("AND a.activity_uri LIKE '%").append(hostName).append("%' ");
            if (findActivityRequestType.isSetName())
                query.append("AND a.activity_uri LIKE '%").append(name).append("%' ");
            if (findActivityRequestType.isSetWorkflowID())
                query.append("AND a.context_workflow_uri LIKE '%").append(workflowID).append("%' ");
            if (findActivityRequestType.isSetServiceID())
                query.append("AND a.context_service_uri LIKE '%").append(serviceID).append("%' ");
            // TODO : Add invocation time, termination time and status into communication?
//            if (findActivityRequestType.isSetInitializationTime())
//                query.append("AND i.invocation_start_time LIKE '%").append(initializationTime).append("%' ");
//            if (findActivityRequestType.isSetTerminationTime())
//                query.append("AND i.execution_end_time LIKE '%").append(terminationTime).append("%' ");
//
//            // default to SUCCESS if not specified
//            l.debug("isSetIsSuccess: " + findActivityRequestType.isSetIsSuccess());
//            if (!findActivityRequestType.isSetIsSuccess())
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.SUCCESS.toString() + "' ");
//            else if (isSuccess)
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.SUCCESS.toString() + "' ");
//            else
//                query.append("AND i.execution_status = '"
//                        + StatusEnum.FAILED.toString() + "' ");

            if (findActivityRequestType.isSetAttributeList()) {
                for (int i = 0; i < attributeList.sizeOfAttributeArray(); i++) {
                    query.append(PROVSqlQuery.ATTRIBUTE_COMPARISON);
                }
            }

            findActivityStmt = connection.prepareStatement(query.toString());
            l.debug("findActivityStmt: " + findActivityStmt);

            if (findActivityRequestType.isSetAttributeList()) {
                for (int i = 0; i < attributeList.sizeOfAttributeArray(); i++) {
                    findActivityStmt.setString(i + 1, '%' + findActivityRequestType.getAttributeList().getAttributeArray(i).getValue() + '%');
                }
            }
            res = findActivityStmt.executeQuery();
            while (res.next()) {
                XmlString activityID = activityIDListType.addNewActivityID();
                activityID.setStringValue(res.getString("activity_uri"));
            }
            res.close();
            findActivityStmt.close();
        } catch (SQLException e) {
            l.error("Exiting findActivity() with SQL errors.");
            l.error(e.toString());
            return null;
        } finally {
            if (findActivityStmt != null) {
                findActivityStmt.close();
            }
            if (res != null) {
                res.close();
            }
        }
        l.debug("Response: " + findActivityResponseDocument);
        l.debug("Exiting findActivity() with success.");
        return findActivityResponseDocument;
    }

    public GetActivityDetailResponseDocument getActivityDetail(
            Connection connection, GetActivityDetailRequestType activityDetailRequestType)
            throws QueryException, SQLException {
        l.debug("Entering getActivityDetail()");
        assert (connection != null);
        assert (activityDetailRequestType != null);

        PreparedStatement activityDetailStmt = null;
        ResultSet res = null;

        GetActivityDetailResponseDocument getActivityDetailResponseDocument =
                GetActivityDetailResponseDocument.Factory.newInstance();
        GetActivityDetailResponseType getActivityDetailResponseType = getActivityDetailResponseDocument
                .addNewGetActivityDetailResponse();
        ActivityDetailListType activityDetailList = getActivityDetailResponseType
                .addNewActivityDetailList();

        if (activityDetailRequestType.getUniqueURIList() != null) {
            for (String uri : activityDetailRequestType.getUniqueURIList().getUniqueURIArray()) {
                try {
                    activityDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_ACTIVITY_DETAIL_BY_URI);
                    activityDetailStmt.setString(1, uri);
                    res = activityDetailStmt.executeQuery();
                    if (res.next()) {
                        ActivityDetail activityDetail = activityDetailList.addNewActivityDetail();
                        activityDetail.setId(uri);
                        populateActivityDetails(res, activityDetail);
                    }
                } catch (SQLException e) {
                    l.error("Exiting getActivityDetail() with SQL errors.", e);
                    return null;
                } finally {
                    if (activityDetailStmt != null) {
                        activityDetailStmt.close();
                        activityDetailStmt = null;
                    }
                    if (res != null) {
                        res.close();
                        res = null;
                    }
                }
            }
        } else {
            for (String id : activityDetailRequestType.getUniqueIDList().getUniqueIDArray()) {
                try {
                    activityDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_ACTIVITY_DETAIL_BY_ID);
                    activityDetailStmt.setString(1, id.replace(QueryConstants.ACTIVITY_IDENTIFIER, ""));
                    res = activityDetailStmt.executeQuery();
                    if (res.next()) {
                        if (res.next()) {
                            ActivityDetail activityDetail = activityDetailList.addNewActivityDetail();
                            activityDetail.setId(id);
                            populateActivityDetails(res, activityDetail);
                        }
                    }
                } catch (SQLException e) {
                    l.error("Exiting getActivityDetail() with SQL errors.", e);
                    return null;
                } finally {
                    if (activityDetailStmt != null) {
                        activityDetailStmt.close();
                        activityDetailStmt = null;
                    }
                    if (res != null) {
                        res.close();
                        res = null;
                    }
                }
            }
        }

        l.debug("Response: " + getActivityDetailResponseDocument);
        l.debug("Exiting getActivityDetail() with success.");
        return getActivityDetailResponseDocument;
    }

    public FindEntityResponseDocument findEntity(Connection connection,
            FindEntityRequestType findEntityRequestType) throws QueryException, SQLException {
        l.debug("Entering findEntity()");
        assert (connection != null);
        assert (findEntityRequestType != null);

        PreparedStatement findEntityStmt = null;
        ResultSet resultSet = null;

        FindEntityResponseDocument findEntityResponseDocument = FindEntityResponseDocument.Factory.newInstance();
        FindEntityResponseType findEntityResponseType = findEntityResponseDocument
                .addNewFindEntityResponse();
        // block related properties
        String blockName = findEntityRequestType.getBlockName();
        String blockContent = findEntityRequestType.getBlockContent();
        long blockSize = findEntityRequestType.getBlockSize();
        String blockMD5 = findEntityRequestType.getBlockMD5Checksum();
        // file related properties
        Calendar creationDate = findEntityRequestType.getFileCreationDate();
        String fileName = findEntityRequestType.getFileName();
        String fileURI = findEntityRequestType.getFileURI();
        String ownerID = findEntityRequestType.getFileOwnerID();
        long fileSize = findEntityRequestType.getFileSize();
        String fileMD5 = findEntityRequestType.getFileMD5Checksum();

        StringBuilder queryString = new StringBuilder("SELECT * FROM exe_entity e ");
        boolean isBlock = false, isFile = false;
        if (findEntityRequestType.isSetBlockName()
                || findEntityRequestType.isSetBlockContent()
                || findEntityRequestType.isSetBlockMD5Checksum()
                || findEntityRequestType.isSetBlockSize()) {
            isBlock = true;
            queryString.append(", exe_block b ");
            queryString.append("WHERE e.entity_id = b.block_id AND e.entity_type = 'BLOCK'");

            if (findEntityRequestType.isSetBlockName())
                queryString.append(" AND b.block_id = '").append(blockName
                        .replace(QueryConstants.BLOCK_IDENTIFIER, "")).append("'");
            if (findEntityRequestType.isSetBlockContent())
                queryString.append(" AND b.block_content LIKE '%").append(blockContent).append("%'");
            if (findEntityRequestType.isSetBlockMD5Checksum())
                queryString.append(" AND b.md5_checksum = '").append(blockMD5).append("'");
            if (findEntityRequestType.isSetBlockSize())
                queryString.append(" AND b.size = '").append(blockSize).append("'");

        } else if (findEntityRequestType.isSetFileName()
                || findEntityRequestType.isSetFileURI()
                || findEntityRequestType.isSetFileOwnerID()
                || findEntityRequestType.isSetFileCreationDate()
                || findEntityRequestType.isSetFileMD5Checksum()
                || findEntityRequestType.isSetFileSize()) {
            isFile = true;
            queryString.append(", exe_file f ");
            if (findEntityRequestType.isSetFileOwnerID())
                queryString.append(", reg_agent ag ");

            queryString.append("WHERE e.entity_id = f.file_id AND e.entity_type = 'FILE'");

            if (findEntityRequestType.isSetFileName())
                queryString.append(" AND f.file_name LIKE '%").append(fileName).append("%'");
            if (findEntityRequestType.isSetFileURI())
                queryString.append(" AND f.file_uri LIKE '%").append(fileURI).append("%'");
            if (findEntityRequestType.isSetFileOwnerID())
                queryString.append(" AND f.owner_id = ag.agent_id AND ag.agent_uri LIKE '%").append(ownerID).append("%'");
            if (findEntityRequestType.isSetFileCreationDate())
                queryString.append(" AND f.creation_date = '").append(creationDate).append("'");
            if (findEntityRequestType.isSetFileMD5Checksum())
                queryString.append(" AND f.md5_checksum = '").append(fileMD5).append("'");
            if (findEntityRequestType.isSetFileSize())
                queryString.append(" AND f.size = '").append(fileSize).append("'");
        }

        try {
            l.debug("findEntityStmt: " + queryString.toString());
            findEntityStmt = connection.prepareStatement(queryString.toString());
            resultSet = findEntityStmt.executeQuery();

            if (isBlock) {
                UniqueIDListType uniqueBlockIDList = findEntityResponseType.addNewUniqueBlockIDList();
                while (resultSet.next()) {
                    uniqueBlockIDList.addUniqueID(QueryConstants.BLOCK_IDENTIFIER +
                            resultSet.getString("block_id"));
                }
            } else if (isFile) {
                UniqueFileListType uniqueFileURIList = findEntityResponseType.addNewUniqueFileURIList();
                while (resultSet.next()) {
                    FileURIDetailsType fileURIDetailsType = uniqueFileURIList.addNewFileURIDetailsType();
                    fileURIDetailsType.setFileURI(resultSet.getString("file_uri"));
                    fileURIDetailsType.setFileID(QueryConstants.FILE_IDENTIFIER +
                            resultSet.getString("file_id"));
                    Timestamp creation_date = resultSet.getTimestamp("creation_date");
                    if (creation_date != null)
                        fileURIDetailsType.setCreationDate(KomaduUtils.getCalendarFromTimeStamp(creation_date));
                }
            } else {
                l.error("Block specific or file specific attributes not found");
            }

            resultSet.close();
            findEntityStmt.close();

        } catch (SQLException e) {
            l.error("Exiting findEntity() with SQL errors.", e);
            return null;
        } finally {
            if (findEntityStmt != null) {
                findEntityStmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }

        l.debug("Response: " + findEntityResponseDocument);
        l.debug("Exiting findEntity() with success.");
        return findEntityResponseDocument;
    }

    public GetEntityDetailResponseDocument getEntityDetail(
            Connection connection, EntityIDListType entityIDType) 
            throws QueryException, SQLException {
        l.debug("Entering getEntityDetail()");
        assert (connection != null);
        assert (entityIDType != null);

        PreparedStatement entityDetailStmt = null;
        PreparedStatement membershipDetailStmt = null;
        ResultSet res = null;
        ResultSet membershipRes = null;

        GetEntityDetailResponseDocument getEntityDetailResponseDocument =
                GetEntityDetailResponseDocument.Factory.newInstance();
        GetEntityDetailResponseType getEntityDetailResponseType = getEntityDetailResponseDocument
                .addNewGetEntityDetailResponse();
        EntityDetailListType entityDetailList = getEntityDetailResponseType
                .addNewEntityDetailList();

        for (String entityID : entityIDType.getEntityIDArray()) {
            try {
                if (entityID.startsWith(QueryConstants.FILE_IDENTIFIER)) {
                    entityDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_FILE);
                    entityDetailStmt.setString(1, entityID.replace(QueryConstants.FILE_IDENTIFIER, ""));
                    l.debug("entityDetailStmt: " + entityDetailStmt);

                    res = entityDetailStmt.executeQuery();
                    if (res.next()) {
                        EntityDetail newEntityDetail = entityDetailList.addNewEntityDetail();
                        newEntityDetail.setId(entityID);
                        String file_uri = res.getString("file_uri");
                        String owner_id = res.getString("owner_id");
                        Timestamp creation_date = res.getTimestamp("creation_date");
                        long size = res.getLong("size");
                        String md5 = res.getString("md5_checksum");
                        String file_name = res.getString("file_name");

                        newEntityDetail.setFileURI(file_uri);
                        if (owner_id != null)
                            newEntityDetail.setOwner(owner_id);
                        if (creation_date != null)
                            newEntityDetail.setCreationDate(KomaduUtils.getCalendarFromTimeStamp(creation_date));
                        if (size > 0)
                            newEntityDetail.setSize(size);
                        if (md5 != null)
                            newEntityDetail.setMd5(md5);
                        if (file_name != null)
                            newEntityDetail.setFileName(file_name);
                    }
                } else if (entityID.startsWith(QueryConstants.BLOCK_IDENTIFIER)) {
                    entityDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_BLOCK);
                    entityDetailStmt.setString(1, entityID.replace(QueryConstants.BLOCK_IDENTIFIER, ""));
                    l.debug("entityDetailStmt: " + entityDetailStmt);

                    res = entityDetailStmt.executeQuery();
                    if (res.next()) {
                        EntityDetail newEntityDetail = entityDetailList.addNewEntityDetail();
                        newEntityDetail.setId(entityID);
                        String block_content = res.getString("block_content");
                        long size = res.getLong("size");
                        String md5 = res.getString("md5_checksum");

                        newEntityDetail.setBlockContent(block_content);
                        if (size > 0)
                            newEntityDetail.setSize(size);
                        if (md5 != null)
                            newEntityDetail.setMd5(md5);
                    }
                } else {
                    entityDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_COLLECTION);
                    entityDetailStmt.setString(1, entityID.replace(QueryConstants.COLLECTION_IDENTIFIER, ""));
                    l.debug("entityDetailStmt: " + entityDetailStmt);
                    res = entityDetailStmt.executeQuery();
                    if (res.next()) {
                        EntityDetail newEntityDetail = entityDetailList.addNewEntityDetail();
                        newEntityDetail.setId(entityID);
                        String uri = res.getString("collection_uri");
                        newEntityDetail.setCollectionURI(uri);

                        membershipDetailStmt = connection.prepareStatement(PROVSqlQuery.GET_MEMBERSHIP);
                        membershipDetailStmt.setString(1, entityID.replace(QueryConstants.COLLECTION_IDENTIFIER, ""));
                        membershipRes = membershipDetailStmt.executeQuery();

                        while (membershipRes.next()) {
                            MembershipDetail membership = newEntityDetail.addNewMembership();
                            membership.setId(membershipRes.getString("member_id"));

                            if (membershipRes.getString("entity_type").equals(EntityEnumType.BLOCK.toString())) {
                                membership.setEntityType(EntityEnumType.BLOCK);
                            } else if (membershipRes.getString("entity_type").equals(EntityEnumType.BLOCK.toString())) {
                                membership.setEntityType(EntityEnumType.FILE);
                            } else if (membershipRes.getString("entity_type").equals(EntityEnumType.COLLECTION.toString())) {
                                membership.setEntityType(EntityEnumType.COLLECTION);
                            } else {
                                l.error("Unrecognized data object type.");
                            }
//                            String instance_of = membershipRes.getString("instance_of");
//                            if (instance_of != null)
//                                membership.setInstanceOf(instance_of);
                        }
                        membershipRes.close();
                        membershipDetailStmt.close();
                    }
                }
            } catch (SQLException e) {
                l.error("Exiting getEntityDetail() with SQL errors.", e);
                return null;
            } finally {
                if (entityDetailStmt != null) {
                    entityDetailStmt.close();
                    entityDetailStmt = null;
                }
                if (membershipDetailStmt != null) {
                    membershipDetailStmt.close();
                    membershipDetailStmt = null;
                }
                if (res != null) {
                    res.close();
                    res = null;
                }
                if (membershipRes != null) {
                    membershipRes.close();
                    membershipRes = null;
                }
            }
        }

        l.debug("Response: " + getEntityDetailResponseDocument);
        l.debug("Exiting QueryEntityUtil.getEntityDetail() with success.");
        return getEntityDetailResponseDocument;

    }

    private void populateActivityDetails(ResultSet res, ActivityDetail activityDetail) throws SQLException {
        String activityType = res.getString("activity_type");
        String context_workflow_uri = res.getString("context_workflow_uri");
        String context_service_uri = res.getString("context_service_uri");
        int timestep = res.getInt("timestep");
        String context_wf_node_id_token = res.getString("context_wf_node_id_token");
        String instance_of = res.getString("instance_of");

        if (activityType != null)
            activityDetail.setType(activityType);
        if (context_workflow_uri != null)
            activityDetail.setWorkflowID(context_workflow_uri);
        if (context_service_uri != null)
            activityDetail.setServiceID(context_service_uri);
        if (timestep != -1)
            activityDetail.setTimestep(timestep);
        if (context_wf_node_id_token != null)
            activityDetail.setWorkflowNodeID(context_wf_node_id_token);
        if (instance_of != null)
            activityDetail.setInstanceOf(instance_of);
    }

}
