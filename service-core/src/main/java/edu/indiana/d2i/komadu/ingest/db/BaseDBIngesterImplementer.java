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

import edu.indiana.d2i.komadu.common.ObjectPool;
import edu.indiana.d2i.komadu.ingest.*;
import edu.indiana.d2i.komadu.ingest.db.AttributeFactory.AttributeDefinitionScopeEnum;
import edu.indiana.d2i.komadu.ingest.IngesterConstants.ProcessingFilterType;
import edu.indiana.d2i.komadu.ingest.IngesterConstants.ProcessingStatus;
import edu.indiana.d2i.komadu.ingest.NotificationSummary.NotificationTypeEnum;
import edu.indiana.d2i.komadu.query.*;
import edu.indiana.d2i.komadu.service.*;
import edu.indiana.d2i.komadu.service.EntityEnumType;
import edu.indiana.d2i.komadu.util.DBLockConstants;
import edu.indiana.d2i.komadu.util.KomaduUtils;
import org.apache.log4j.Logger;
import org.apache.xmlbeans.XmlObject;

import java.sql.*;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class BaseDBIngesterImplementer implements IngesterImplementer<Long, String> {

    private static Logger log = Logger.getLogger(BaseDBIngesterImplementer.class);
    private static Logger plog = Logger.getLogger("perflog");

    protected ObjectPool<Connection> connectionPool = null;

    public static final int DEFAULT_RAW_NOTIFICATION_CACHE_SIZE = 100;
    protected int rawNotificationCacheSize = DEFAULT_RAW_NOTIFICATION_CACHE_SIZE;

    public static enum ActivityTypeEnum {
        WORKFLOW, METHOD, SERVICE, GENERIC
    }

    public static enum EntityTypeEnum {
        FILE, BLOCK, COLLECTION, GENERIC
    }

    public static enum DerivationTypeEnum {
        DERIVATION, REVISION, QUOTATION, PRIMARY_SOURCE
    }

    protected List<StoredRawNotification<Long, String>> rawUnknownNotificationCache;
    protected List<StoredRawNotification<Long, String>> rawKnownNotificationCache;

    static final String STATEMENT_SELECT_KNOWN_NOTIF = "SELECT raw_id, notification_type, notification FROM raw_notification WHERE processing_status=? AND notification_type<>? LIMIT ?";
    static final String STATEMENT_SELECT_UNKNOWN_NOTIF = "SELECT raw_id, notification_type, notification FROM raw_notification WHERE processing_status=? AND notification_type=? LIMIT ?";
    static final String STATEMENT_UPDATE_RAW_NOTIF_STATUS = "UPDATE raw_notification SET processing_status=? WHERE raw_id IN (";

    public BaseDBIngesterImplementer(int cacheSize) {

        this.rawNotificationCacheSize = cacheSize > 0 ? cacheSize : DEFAULT_RAW_NOTIFICATION_CACHE_SIZE;

        rawKnownNotificationCache = new ArrayList<StoredRawNotification<Long, String>>();

        rawUnknownNotificationCache = new ArrayList<StoredRawNotification<Long, String>>();

//        DBConnectionPool.init(dbLocation, dbUsername, dbPassword, initialPoolSize, maxPoolSize, timeToLive);
//
        connectionPool = DBConnectionPool.getInstance();
//
//        DBConnectionPool.launch();

    }


    public void storeRawNotification(NotificationSummary.NotificationTypeEnum notificationType, Calendar storeTime, XmlObject xmlObject) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            addNewRawNotification(notificationType, storeTime, xmlObject, connection);
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void resetUnfinishedRawNotifications() throws IngestException {
        log.debug("Resetting unfinished raw notifications");
        Connection connection = null;
        PreparedStatement statement = null;
        try {
            connection = getConnection();
            statement = connection.prepareStatement("UPDATE raw_notification SET processing_status=? WHERE processing_status=?");
            statement.setString(1, ProcessingStatus.RAW.toString());
            statement.setString(2, ProcessingStatus.PROCESSING.toString());
            statement.executeUpdate();
            statement.close();
            log.debug("Done resetting unfinished raw notifications");
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            if (statement != null) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    log.warn("Unable to close statement", e);
                }
                statement = null;
            }
            connectionPool.releaseEntry(connection);

        }
    }

    public List<StoredRawNotification<Long, String>> retrieveUnprocessedRawNotifications(
            ProcessingFilterType processingFilterType, int batchLimit) throws IngestException {

        List<StoredRawNotification<Long, String>> list = new ArrayList<StoredRawNotification<Long, String>>();

        if (ProcessingFilterType.KNOWN_TYPES.equals(processingFilterType)) {
            synchronized (rawKnownNotificationCache) {
                if (rawKnownNotificationCache.isEmpty()) {
                    try {
                        cacheRawNotificationsFromDB(processingFilterType);
                    } catch (Exception e) {
                        log.error("error caching raw notifications from db ", e);
                    }
                }
                int cacheSize = rawKnownNotificationCache.size();
                int count = batchLimit < cacheSize ? batchLimit : cacheSize;
                for (int i = 0; i < count; i++) {
                    StoredRawNotification<Long, String> rawNotification = rawKnownNotificationCache.remove(0);
                    list.add(rawNotification);
                }
            }

        } else if (ProcessingFilterType.UNKNOWN_TYPES.equals(processingFilterType)) {
            synchronized (rawUnknownNotificationCache) {
                if (rawUnknownNotificationCache.isEmpty()) {
                    try {
                        cacheRawNotificationsFromDB(processingFilterType);
                    } catch (Exception e) {
                        log.error("error caching raw notifications from db ", e);
                    }
                }
                int cacheSize = rawUnknownNotificationCache.size();
                int count = batchLimit < cacheSize ? batchLimit : cacheSize;
                for (int i = 0; i < count; i++) {
                    StoredRawNotification<Long, String> rawNotification = rawUnknownNotificationCache.remove(0);
                    list.add(rawNotification);
                }
            }

        }
        return list;
    }

    public void storeActivityActivityRelationship(ActivityActivityType activityActivity) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process Activity1 and insert into the db
            IngestionResult activity1Result = addNewActivity(activityActivity.getActivity1(), connection);
            // process Activity2 and insert into the db
            IngestionResult activity2Result = addNewActivity(activityActivity.getActivity2(), connection);
            // now we have to deal with the communication
            if (activity1Result.getActualId() != null && activity2Result.getActualId() != null) {
                CommunicationType communication = activityActivity.getCommunication();
                // informed = activity 1 and informant = activity 2 case
                if (communication.getInformedActivityID().equals(activity1Result.getActualId()) &&
                        communication.getInformantActivityID().equals(activity2Result.getActualId())) {
                    addNewCommunication(communication, activity1Result.getDbId(), activity2Result.getDbId(), connection);
                    // informed = activity 2 and informant = activity 1 case
                } else if (communication.getInformedActivityID().equals(activity2Result.getActualId()) &&
                        communication.getInformantActivityID().equals(activity1Result.getActualId())) {
                    addNewCommunication(communication, activity2Result.getDbId(), activity1Result.getDbId(), connection);
                } else {
                    throw new IngestException("Invalid Activity IDs in Communication");
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void storeActivityEntityRelationship(ActivityEntityType activityEntity) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process activity and entity and store
            IngestionResult activityResult = addNewActivity(activityEntity.getActivity(), connection);
            IngestionResult entityResult = addNewEntity(activityEntity.getEntity(), connection);

            // relationship between Activity and Entity can be one of these
            // usage, generation, start, end, invalidation
            if (activityResult.getActualId() != null && entityResult.getActualId() != null) {
                if (activityEntity.getUsage() != null) { // usage case
                    UsageType usage = activityEntity.getUsage();
                    if (!usage.getActivityID().trim().equals(activityResult.getActualId())) {
                        throw new IngestException("Invalid Activity in Usage");
                    } else if (!usage.getEntityID().trim().equals(entityResult.getActualId())) {
                        throw new IngestException("Invalid Entity in Usage");
                    } else {
                        addNewUsage(usage, activityResult.getDbId(), entityResult.getDbId(), connection);
                    }
                } else if (activityEntity.getGeneration() != null) { // generation case
                    GenerationType generation = activityEntity.getGeneration();
                    if (!generation.getActivityID().trim().equals(activityResult.getActualId())) {
                        throw new IngestException("Invalid Activity in Generation");
                    } else if (!generation.getEntityID().trim().equals(entityResult.getActualId())) {
                        throw new IngestException("Invalid Entity in Generation");
                    } else {
                        addNewGeneration(generation, activityResult.getDbId(), entityResult.getDbId(), connection);
                    }
                } else if (activityEntity.getStart() != null) { // start case
                    StartType start = activityEntity.getStart();
                    if (!start.getActivityID().trim().equals(activityResult.getActualId())) {
                        throw new IngestException("Invalid Activity in Start");
                    } else if (!start.getTriggerID().trim().equals(entityResult.getActualId())) {
                        throw new IngestException("Invalid Entity in Start");
                    } else {
                        addNewStart(start, activityResult.getDbId(), entityResult.getDbId(), connection);
                    }
                } else if (activityEntity.getEnd() != null) { // end case
                    EndType end = activityEntity.getEnd();
                    if (!end.getActivityID().trim().equals(activityResult.getActualId())) {
                        throw new IngestException("Invalid Activity in End");
                    } else if (!end.getTriggerID().trim().equals(entityResult.getActualId())) {
                        throw new IngestException("Invalid Entity in End");
                    } else {
                        addNewEnd(end, activityResult.getDbId(), entityResult.getDbId(), connection);
                    }
                } else if (activityEntity.getInvalidation() != null) { // invalidation case
                    InvalidationType invalidation = activityEntity.getInvalidation();
                    if (!invalidation.getActivityID().trim().equals(activityResult.getActualId())) {
                        throw new IngestException("Invalid Activity in Invalidation");
                    } else if (!invalidation.getEntityID().trim().equals(entityResult.getActualId())) {
                        throw new IngestException("Invalid Entity in Invalidation");
                    } else {
                        addNewInvalidation(invalidation, activityResult.getDbId(), entityResult.getDbId(), connection);
                    }
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void storeAgentAgentRelationship(AgentAgentType agentAgent) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process Agents and insert into the db
            IngestionResult delAgentResult = addNewAgent(agentAgent.getDelegateAgent(), connection);
            IngestionResult resAgentResult = addNewAgent(agentAgent.getResponsibleAgent(), connection);
            // finally we have to deal with the delegation
            if (resAgentResult.getActualId() != null && delAgentResult.getActualId() != null) {
                DelegationType delegation = agentAgent.getDelegation();
                if (!delegation.getDelegateAgentID().trim().equals(delAgentResult.getActualId())) {
                    throw new IngestException("Invalid delegate Agent ID in Delegation");
                } else if (!delegation.getResponsibleAgentID().trim().equals(resAgentResult.getActualId())) {
                    throw new IngestException("Invalid responsible Agent ID in Delegation");
                } else {
                    addNewDelegation(delegation, delAgentResult.getDbId(), resAgentResult.getDbId(), connection);
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void storeAgentEntityRelationship(AgentEntityType agentEntity) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process Agent and insert into the db
            IngestionResult agentResult = addNewAgent(agentEntity.getAgent(), connection);
            // process Entity and insert into the db
            IngestionResult entityResult = addNewEntity(agentEntity.getEntity(), connection);
            // finally we have to deal with the delegation
            if (agentResult.getActualId() != null && entityResult.getActualId() != null) {
                AttributionType attribution = agentEntity.getAttribution();
                if (!attribution.getEntityID().trim().equals(entityResult.getActualId())) {
                    throw new IngestException("Invalid entity in Attribution");
                } else if (!attribution.getAgentID().trim().equals(agentResult.getActualId())) {
                    throw new IngestException("Invalid agent in Attribution");
                } else {
                    addNewAttribution(attribution, agentResult.getDbId(), entityResult.getDbId(), connection);
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void storeEntityEntityRelationship(EntityEntityType entityEntity) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process Entity 1 and insert into the db
            IngestionResult entity1Result = addNewEntity(entityEntity.getEntity1(), connection);
            // process Entity 2 and insert into the db
            IngestionResult entity2Result = addNewEntity(entityEntity.getEntity2(), connection);
            // finally we have to deal with the delegation
            if (entity1Result.getActualId() != null && entity2Result.getActualId() != null) {
                // revision, quotation and primary source are also special kinds of derivations
                if (entityEntity.getDerivation() != null) {   // derivation
                    handleDerivation(entityEntity.getDerivation(), DerivationTypeEnum.DERIVATION,
                            entity1Result, entity2Result, connection);
                } else if (entityEntity.getRevision() != null) {   // revision
                    handleDerivation(entityEntity.getRevision(), DerivationTypeEnum.REVISION,
                            entity1Result, entity2Result, connection);
                } else if (entityEntity.getQuotation() != null) {   // quotation
                    handleDerivation(entityEntity.getQuotation(), DerivationTypeEnum.QUOTATION,
                            entity1Result, entity2Result, connection);
                } else if (entityEntity.getPrimarySource() != null) {   // primary source
                    handleDerivation(entityEntity.getPrimarySource(), DerivationTypeEnum.PRIMARY_SOURCE,
                            entity1Result, entity2Result, connection);
                } else if (entityEntity.getAlternate() != null) {   // alternate
                    AlternateType alternate = entityEntity.getAlternate();
                    String alt1 = alternate.getAlternate1ID().trim();
                    String alt2 = alternate.getAlternate2ID().trim();
                    // we don't care about the order of alternate, but id's must match
                    if (alt1.equals(entity1Result.getActualId()) && alt2.equals(entity2Result.getActualId()) ||
                            alt1.equals(entity2Result.getActualId()) && alt2.equals(entity1Result.getActualId())) {
                        addNewAlternate(entity1Result.getDbId(), entity2Result.getDbId(), connection);
                    } else {
                        throw new IngestException("Invalid Entity IDs in Alternate");
                    }
                } else if (entityEntity.getSpecialization() != null) {   // specialization
                    SpecializationType specialization = entityEntity.getSpecialization();
                    String specific = specialization.getSpecificEntityID().trim();
                    String general = specialization.getGeneralEntityID().trim();
                    if (specific.equals(entity1Result.getActualId()) && general.equals(entity2Result.getActualId())) {
                        addNewSpecialization(entity1Result.getDbId(), entity2Result.getDbId(), connection);
                    } else if (specific.equals(entity2Result.getActualId()) && general.equals(entity1Result.getActualId())) {
                        addNewSpecialization(entity2Result.getDbId(), entity1Result.getDbId(), connection);
                    } else {
                        throw new IngestException("Invalid Entity IDs in Specialization");
                    }
                } else if (entityEntity.getMembership() != null) {   // membership
                    MembershipType membership = entityEntity.getMembership();
                    String collection = membership.getCollectionID().trim();
                    String member = membership.getEntityID().trim();
                    if (collection.equals(entity1Result.getActualId()) && member.equals(entity2Result.getActualId())) {
                        addNewMembership(entity1Result.getDbId(), entity2Result.getDbId(), connection);
                    } else if (collection.equals(entity2Result.getActualId()) && member.equals(entity1Result.getActualId())) {
                        addNewMembership(entity2Result.getDbId(), entity1Result.getDbId(), connection);
                    } else {
                        throw new IngestException("Invalid Entity IDs in Membership");
                    }
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    protected void handleDerivation(DerivationType derivation, DerivationTypeEnum type,
                                    IngestionResult entity1Result, IngestionResult entity2Result,
                                    Connection connection) throws IngestException, SQLException {
        if (derivation.getUsedEntityID().equals(entity1Result.getActualId()) &&
                derivation.getGeneratedEntityID().equals(entity2Result.getActualId())) {
            addNewDerivation(derivation, type, entity1Result.getDbId(), entity2Result.getDbId(), connection);
        } else if (derivation.getUsedEntityID().equals(entity2Result.getActualId()) &&
                derivation.getGeneratedEntityID().equals(entity1Result.getActualId())) {
            addNewDerivation(derivation, type, entity2Result.getDbId(), entity1Result.getDbId(), connection);
        } else {
            throw new IngestException("Invalid Entity IDs in Derivation");
        }
    }

    public void storeAgentActivityRelationship(AgentActivityType agentActivity) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            // process Agent and insert into the db
            IngestionResult agentResult = addNewAgent(agentActivity.getAgent(), connection);
            // process Activity and insert into the db
            IngestionResult activityResult = addNewActivity(agentActivity.getActivity(), connection);
            // finally we have to deal with the association
            if (activityResult.getActualId() != null) {
                AssociationType association = agentActivity.getAssociation();
                if (!association.getActivityID().trim().equals(activityResult.getActualId())) {
                    throw new IngestException("Invalid Activity ID in Association");
                } else if (!association.getAgentID().trim().equals(agentResult.getActualId())) {
                    throw new IngestException("Invalid Agent ID in Association");
                } else {
                    addNewAssociation(association, activityResult.getDbId(), agentResult.getDbId(), connection);
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    @Override
    public void storeAddAttributes(AddAttributesType addAttributes) throws IngestException {
        Connection connection = null;
        try {
            connection = getConnection();
            ObjectEnumType.Enum objectType =  addAttributes.getObjectType();
            String uri = addAttributes.getObjectID();
            // 3 parameters related to object table
            String objectTableName = null, objectUriColumn = null, objectIdColumn = null;
            // 2 parameters related to target attribute table
            String attributeTableName, attributeColumnName;
            // assign table and column name depending on object type
            if (objectType == ObjectEnumType.ACTIVITY) {
                objectTableName = "exe_activity";
                objectUriColumn = "activity_uri";
                objectIdColumn = "activity_id";
                attributeTableName = "exe_activity_attribute";
                attributeColumnName = "activity_id";
            } else if (objectType == ObjectEnumType.ENTITY) {
                attributeTableName = "exe_entity_attribute";
                attributeColumnName = "entity_id";
                EntityEnumType.Enum entityType = addAttributes.getEntityType();
                if (entityType != null && entityType != EntityEnumType.GENERIC) {
                    if (entityType == EntityEnumType.FILE) {
                        objectTableName = "exe_file";
                        objectUriColumn = "file_uri";
                        objectIdColumn = "file_id";
                    } else if (entityType == EntityEnumType.BLOCK) {
                        objectTableName = "exe_block";
                        objectUriColumn = "block_uri";
                        objectIdColumn = "block_id";
                    } else if (entityType == EntityEnumType.COLLECTION) {
                        objectTableName = "exe_collection";
                        objectUriColumn = "collection_uri";
                        objectIdColumn = "collection_id";
                    }
                } else {
                    // generic entity case
                    objectTableName = "exe_generic_entity";
                    objectUriColumn = "generic_entity_uri";
                    objectIdColumn = "generic_entity_id";
                }
            } else if (objectType == ObjectEnumType.AGENT) {
                attributeTableName = "reg_agent_attribute";
                attributeColumnName = "agent_id";
                objectTableName = "reg_agent";
                objectUriColumn = "agent_uri";
                objectIdColumn = "agent_id";
            } else {
                return;
            }
            // get the set of internal ids using the object URI
            List<Long> internalIds = getInternalId(objectTableName, objectIdColumn,
                    objectUriColumn, uri, connection);
            // if we have multiple objects from the given URI, we have to insert the
            // attributes into all objects
            for (Long internalId : internalIds) {
                addAttributes(attributeTableName, attributeColumnName, internalId,
                        addAttributes.getAttributes().getAttributeArray(), connection);
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            connectionPool.releaseEntry(connection);
        }
    }

    public void markRawNotifications(List<StoredRawNotification<Long, String>> list, ProcessingStatus processingStatus) throws IngestException {
        Connection connection = null;
        PreparedStatement statement = null;

        try {
            if (list != null && list.size() > 0) {
                connection = getConnection();
                StringBuilder sqlStatementBuilder = new StringBuilder(STATEMENT_UPDATE_RAW_NOTIF_STATUS);
                int listSize = list.size();
                for (int i = 0; i < listSize - 1; i++) {
                    sqlStatementBuilder.append("?, ");
                }
                sqlStatementBuilder.append("?)");

                statement = connection.prepareStatement(sqlStatementBuilder.toString());
                statement.setString(1, processingStatus.toString());
                int counter = 2;
                for (StoredRawNotification<Long, String> storedRawNotification : list) {
                    Long internalIDObj = storedRawNotification.getInternalID();
                    statement.setLong(counter, internalIDObj);
                    counter++;
                }

                long startTime = 0;
                if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
                int result = statement.executeUpdate();
                if (plog.isTraceEnabled()) plog.trace("markRawNotification DB UPDATE time: " + (System.currentTimeMillis() - startTime));

                statement.close();
                if (log.isDebugEnabled())log.debug("Number of entries marked " + processingStatus.toString() + ": " + result);
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            if (statement != null) {
                try {
                    statement.close();
                } catch (SQLException e) {
                    log.warn("Unable to close statement", e);
                }
            }
            connectionPool.releaseEntry(connection);
        }
    }

    protected Connection getConnection() throws SQLException {
        return connectionPool.getEntry();
    }

    protected Long addNewRawNotification(NotificationTypeEnum notificationType, Calendar storeTime,
                                         XmlObject xmlObject, Connection connection)
            throws SQLException, IngestException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("store_time", KomaduUtils.getTimestamp(storeTime),
                TableAttributeData.DataType.TIMESTAMP);
        tuple.addAttribute("notification_type", notificationType.name(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("processing_status", ProcessingStatus.RAW.name(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("notification", xmlObject.xmlText(IngesterConstants.PRETTY_PRINT_OPTS),
                TableAttributeData.DataType.STRING);
        // finally call insertTuple by passing the tuple and connection
        return insertTuple("raw_notification", tuple, "addNewRawNotification", connection);
    }

    protected Long getLastAutoID(Connection connection) throws SQLException {
        Long lastAutoID = null;
        PreparedStatement prepStatement = null;
        ResultSet resultSet = null;

        try {
            prepStatement = connection.prepareStatement("SELECT LAST_INSERT_ID()");
            resultSet = prepStatement.executeQuery();
            if (resultSet.next()) {
                long lastID = resultSet.getLong(1);
                if (!resultSet.wasNull()) {
                    lastAutoID = lastID;
                }
            }
        } finally {
            if (resultSet != null) {
                resultSet.close();
            }
            if (prepStatement != null) {
                prepStatement.close();
            }
        }
        return lastAutoID;
    }

    protected void cacheRawNotificationsFromDB(ProcessingFilterType processingFilterType)
            throws SQLException, IngestException {

        Connection connection = null;
        List<StoredRawNotification<Long, String>> workList;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        PreparedStatement updateStatement = null;

        try {
            connection = getConnection();
            StringBuilder sqlStatementBuilder;
            String selectFilter;

            if (ProcessingFilterType.KNOWN_TYPES.equals(processingFilterType)) {
                sqlStatementBuilder = new StringBuilder(STATEMENT_SELECT_KNOWN_NOTIF);
                selectFilter = ProcessingFilterType.UNKNOWN_TYPES.name();
                workList = rawKnownNotificationCache;
            } else {
                sqlStatementBuilder = new StringBuilder(STATEMENT_SELECT_UNKNOWN_NOTIF);
                selectFilter = processingFilterType.name();
                workList = rawUnknownNotificationCache;
            }

            statement = connection.prepareStatement(sqlStatementBuilder.toString());
            statement.setString(1, ProcessingStatus.RAW.name());
            statement.setString(2, selectFilter);
            statement.setInt(3, rawNotificationCacheSize);

            long startTime = 0;
            if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
            resultSet = statement.executeQuery();
            if (plog.isTraceEnabled())
                plog.trace("fetch raw from db time: " + (System.currentTimeMillis() - startTime));

            StringBuilder updateStatementBuilder = new StringBuilder(STATEMENT_UPDATE_RAW_NOTIF_STATUS);
            List<Long> internalIDList = new ArrayList<Long>();

            while (resultSet.next()) {
                long internalID = resultSet.getLong("raw_id");
                internalIDList.add(internalID);
                String notificationTypeString = resultSet.getString("notification_type");
                String notification = resultSet.getString("notification");
                BaseDBStoredRawNotification storedRawNotification = new BaseDBStoredRawNotification(internalID,
                        NotificationTypeEnum.valueOf(notificationTypeString), notification);
                workList.add(storedRawNotification);

            }

            int listSize = internalIDList.size();
            if (listSize > 0) {
                for (int i = 0; i < listSize - 1; i++) {
                    updateStatementBuilder.append("?,");
                }
                updateStatementBuilder.append("?)");
                updateStatement = connection.prepareStatement(updateStatementBuilder.toString());
                updateStatement.setString(1, ProcessingStatus.PROCESSING.name());
                int index = 2;
                for (Long id : internalIDList) {
                    updateStatement.setLong(index++, id);
                }

                if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
                int result = updateStatement.executeUpdate();
                if (plog.isTraceEnabled())
                    plog.trace("update raw notif status DB UPDATE time: " + (System.currentTimeMillis() - startTime));

                if (result != listSize) {
                    throw new IngestException("List size mismatch. Cached: " + listSize + " updated: " + result);
                }
            }
        } catch (SQLException sqle) {
            throw new IngestException(sqle);
        } finally {
            if (updateStatement != null) {
                updateStatement.close();
            }

            if (resultSet != null) {
                resultSet.close();
            }
            if (statement != null) {
                statement.close();
            }
            connectionPool.releaseEntry(connection);
        }
    }

    private AgentRecord getAgentRecord(String agentID, Connection connection) throws SQLException {
        if (log.isDebugEnabled()) log.debug("UserEntity DN: " + agentID);

        AgentRecord agentRecord = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        try {
            statement = connection.prepareStatement("SELECT agent_id, agent_type, name, affiliation, email, role, location FROM reg_agent WHERE agent_uri=?");
            statement.setString(1, agentID);

            long startTime = 0;
            if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
            resultSet = statement.executeQuery();
            if (plog.isTraceEnabled()) plog.trace("get agent record time: " + (System.currentTimeMillis() - startTime));

            if (resultSet.next()) {
                long internalID = resultSet.getLong("agent_id");
                agentRecord = new AgentRecord(internalID, agentID, getStringFromResultSet(resultSet, "agent_type"),
                        getStringFromResultSet(resultSet, "name"),
                        getStringFromResultSet(resultSet, "affiliation"),
                        getStringFromResultSet(resultSet, "email"),
                        getStringFromResultSet(resultSet, "role"),
                        getStringFromResultSet(resultSet, "location")
                );
            }
        } finally {
            if (resultSet != null) {
                resultSet.close();
            }
            if (statement != null) {
                statement.close();
            }
        }
        return agentRecord;
    }

    private String getStringFromResultSet(ResultSet result, String attName) throws SQLException {
        String val = result.getString(attName);
        if (result.wasNull()) {
            val = null;
        }
        return val;
    }

    /**
     * Add a new agent into the Database. This agent can either be a user agent or
     * a generic agent
     *
     * @param agentInfo  agent information to be added, user can be accessed through this
     * @param connection established connection to DB
     * @return DB internal ID of the newly added record
     * @throws IngestException thrown if failed to add the new entity;
     * @throws SQLException
     */
    protected IngestionResult addNewAgent(AgentType agentInfo, Connection connection)
            throws IngestException, SQLException {
        GenericAgentType agent;
        if (agentInfo.getUserAgent() != null)
            agent = agentInfo.getUserAgent();
        else if (agentInfo.getGenericAgent() != null)
            agent = agentInfo.getGenericAgent();
        else
            throw new IngestException("Agent not found");

        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, agent.getAgentID(), connection)) {
            // check whether the activity already exists
            ingestionResult = KomaduUtils.isAgentExists(agent.getAgentID(), agentInfo.getType(), connection);
            if (ingestionResult == null) {
                // construct the tuple with attributes and values
                TupleData tuple = new TupleData();
                tuple.addAttribute("agent_uri", agent.getAgentID(), TableAttributeData.DataType.STRING);
                tuple.addAttribute("agent_type", agentInfo.getType().toString(), TableAttributeData.DataType.STRING);    // TODO : DEBUG
                if (agent instanceof UserAgentType) {
                    UserAgentType userAgent = (UserAgentType) agent;
                    if (userAgent.getFullName() != null)
                        tuple.addAttribute("name", userAgent.getFullName(), TableAttributeData.DataType.STRING);
                    if (userAgent.getAffiliation() != null)
                        tuple.addAttribute("affiliation", userAgent.getAffiliation(), TableAttributeData.DataType.STRING);
                    if (userAgent.getEmail() != null)
                        tuple.addAttribute("email", userAgent.getEmail(), TableAttributeData.DataType.STRING);
                }
                if (agentInfo.getRole() != null)    // TODO : DEBUG
                    tuple.addAttribute("role", agentInfo.getRole(), TableAttributeData.DataType.STRING);
                if (agentInfo.getLocation() != null)    // TODO : DEBUG
                    tuple.addAttribute("location", agentInfo.getLocation(), TableAttributeData.DataType.STRING);
                // finally call insertTuple by passing the tuple and connection
                Long agentId = insertTuple("reg_agent", tuple, "addNewAgent", connection);
                // Insert agent attributes
                if (agent.getAttributes() != null) {
                    addAttributes("reg_agent_attribute", "agent_id", agentId,
                            agent.getAttributes().getAttributeArray(), connection);
                }
                ingestionResult = new IngestionResult(agent.getAgentID(), agentId);
            }
        }
        return ingestionResult;
    }

    protected IngestionResult addNewEntity(EntityType entityInfo, Connection connection)
            throws IngestException, SQLException {
        // there can be 4 types of entities, File, Block, Collection or Generic
        IngestionResult result;
        if (entityInfo.getFile() != null) {
            result = KomaduUtils.isEntityExists(entityInfo.getFile().getFileURI(),
                    EntityTypeEnum.FILE, connection);
            if (result == null)
                result = addNewFileEntity(entityInfo, connection);
        } else if (entityInfo.getBlock() != null) {
            result = KomaduUtils.isEntityExists(entityInfo.getBlock().getBlockURI(),
                    EntityTypeEnum.BLOCK, connection);
            if (result == null)
                result = addNewBlockEntity(entityInfo, connection);
        } else if (entityInfo.getCollection() != null) {
            result = KomaduUtils.isEntityExists(entityInfo.getCollection().getCollectionURI(),
                    EntityTypeEnum.COLLECTION, connection);
            if (result == null)
                result = addNewCollection(entityInfo, connection);
        } else if (entityInfo.getGenericEntity() != null) {
            result = KomaduUtils.isEntityExists(entityInfo.getGenericEntity().getEntityURI(),
                    EntityTypeEnum.GENERIC, connection);
            if (result == null)
                result = addNewGenericEntity(entityInfo, connection);
        } else {
            throw new IngestException("Entity not found");
        }
        return result;
    }

    protected IngestionResult addNewCollection(EntityType entityInfo, Connection connection)
            throws IngestException, SQLException {
        CollectionType collection = entityInfo.getCollection();
        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, collection.getCollectionURI(), connection)) {
            // first we have to insert the base entity entry and get the id
            Long baseEntityId = addNewBaseEntity(EntityTypeEnum.COLLECTION, entityInfo.getAttributes(),
                    entityInfo.getRole(), entityInfo.getLocation(), connection);

            // construct the block tuple
            TupleData tuple = new TupleData();
            tuple.addAttribute("collection_id", baseEntityId, TableAttributeData.DataType.LONG);
            tuple.addAttribute("collection_uri", collection.getCollectionURI(), TableAttributeData.DataType.STRING);

            // insert the collection tuple
            insertTuple("exe_collection", tuple, "addNewCollection", connection);
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, collection.getCollectionURI(), connection);

            // handle members of collection
            MembersType members = collection.getMembers();
            for (EntityType member : members.getMemberArray()) {
                IngestionResult memberResult = addNewEntity(member, connection);
                addNewMembership(baseEntityId, memberResult.getDbId(), connection);
            }
            // finally return collection ids
            ingestionResult = new IngestionResult(collection.getCollectionURI(), baseEntityId);
        }
        return ingestionResult;
    }

    protected IngestionResult addNewGenericEntity(EntityType entityInfo, Connection connection)
            throws IngestException, SQLException {
        GenericEntityType genericEntity = entityInfo.getGenericEntity();
        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, genericEntity.getEntityURI(), connection)) {
            // first we have to insert the base entity entry and get the id
            Long baseEntityId = addNewBaseEntity(EntityTypeEnum.GENERIC, entityInfo.getAttributes(),
                    entityInfo.getRole(), entityInfo.getLocation(), connection);

            // construct the block tuple
            TupleData tuple = new TupleData();
            tuple.addAttribute("generic_entity_id", baseEntityId, TableAttributeData.DataType.LONG);
            tuple.addAttribute("generic_entity_uri", genericEntity.getEntityURI(), TableAttributeData.DataType.STRING);

            // finally insert the tuple
            Long genericId = insertTuple("exe_generic_entity", tuple, "addNewGenericEntity", connection);
            ingestionResult = new IngestionResult(genericEntity.getEntityURI(), genericId);
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, genericEntity.getEntityURI(), connection);
        }
        return ingestionResult;
    }

    protected IngestionResult addNewBlockEntity(EntityType entityInfo, Connection connection)
            throws IngestException, SQLException {
        BlockType block = entityInfo.getBlock();
        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, block.getBlockURI(), connection)) {
            // first we have to insert the base entity entry and get the id
            Long baseEntityId = addNewBaseEntity(EntityTypeEnum.BLOCK, entityInfo.getAttributes(),
                    entityInfo.getRole(), entityInfo.getLocation(), connection);

            // construct the block tuple
            TupleData tuple = new TupleData();
            tuple.addAttribute("block_id", baseEntityId, TableAttributeData.DataType.LONG);
            tuple.addAttribute("block_uri", block.getBlockURI(), TableAttributeData.DataType.STRING);
            String content = block.getBlockContent();
            // calculate md5 from content
            String md5 = KomaduUtils.calculateMD5(content);
            if (md5 != null)
                tuple.addAttribute("md5_checksum", md5, TableAttributeData.DataType.STRING);

            tuple.addAttribute("size", content.length(), TableAttributeData.DataType.LONG);
            tuple.addAttribute("block_content", content, TableAttributeData.DataType.STRING);

            // finally insert the tuple
            Long blockId = insertTuple("exe_block", tuple, "addNewBlockEntity", connection);
            ingestionResult = new IngestionResult(block.getBlockURI(), blockId);
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, block.getBlockURI(), connection);
        }
        return ingestionResult;
    }

    protected IngestionResult addNewFileEntity(EntityType entityInfo, Connection connection)
            throws IngestException, SQLException {
        FileType file = entityInfo.getFile();

        // handle owner agent of the entity, we have to insert the agent if it doesn't already exists
        IngestionResult ownerResult = null;
        if (file.getOwnerDN() != null) {
            AgentType ownerAgent = AgentType.Factory.newInstance();
            // create a user agent using the DN
            UserAgentType user = UserAgentType.Factory.newInstance();
            user.setAgentID(file.getOwnerDN());
            ownerAgent.setUserAgent(user);
            ownerAgent.setType(AgentEnumType.OTHER);
            ownerResult = addNewAgent(ownerAgent, connection);
        }

        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, file.getFileURI(), connection)) {
            // first we have to insert the base entity entry and get the id
            Long baseEntityId = addNewBaseEntity(EntityTypeEnum.FILE, entityInfo.getAttributes(),
                    entityInfo.getRole(), entityInfo.getLocation(), connection);

            // then construct the file tuple
            TupleData tuple = new TupleData();
            tuple.addAttribute("file_id", baseEntityId, TableAttributeData.DataType.LONG);
            tuple.addAttribute("file_uri", file.getFileURI(), TableAttributeData.DataType.STRING);
            if (ownerResult != null)
                tuple.addAttribute("owner_id", ownerResult.getDbId(), TableAttributeData.DataType.LONG);
            if (file.isSetCreateDate())
                tuple.addAttribute("creation_date", KomaduUtils.getTimestamp(file.getCreateDate()),
                        TableAttributeData.DataType.TIMESTAMP);
            tuple.addAttribute("size", file.getSize(), TableAttributeData.DataType.LONG);
            tuple.addAttribute("md5_checksum", file.getMd5Sum(), TableAttributeData.DataType.STRING);
            tuple.addAttribute("file_name", file.getFileName(), TableAttributeData.DataType.STRING);

            // finally insert the tuple
            Long fileId = insertTuple("exe_file", tuple, "addNewFileEntity", connection);
            ingestionResult = new IngestionResult(file.getFileURI(), fileId);
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, file.getFileURI(), connection);
        }
        return ingestionResult;
    }

    protected Long addNewBaseEntity(EntityTypeEnum type, AttributesType attributes, String role, String location,
                                    Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("entity_type", type.name(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("role", role, TableAttributeData.DataType.STRING);
        tuple.addAttribute("location", location, TableAttributeData.DataType.STRING);
        // insert entity
        Long entityId = insertTuple("exe_entity", tuple, "addNewBaseEntity", connection);
        // Insert entity attributes
        if (attributes != null) {
            addAttributes("exe_entity_attribute", "entity_id", entityId,
                    attributes.getAttributeArray(), connection);
        }
        return entityId;
    }

    protected void addNewMembership(Long collectionId, Long memberId, Connection connection)
            throws IngestException, SQLException {
        // create a tuple for membership
        TupleData memberTuple = new TupleData();
        memberTuple.addAttribute("collection_id", collectionId, TableAttributeData.DataType.LONG);
        memberTuple.addAttribute("member_id", memberId, TableAttributeData.DataType.LONG);
        // insert membership tuple
        insertTuple("exe_collection_membership", memberTuple, "addNewMembership", connection);
    }

    protected void addNewSpecialization(Long specificId, Long generalId, Connection connection)
            throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("specific_id", specificId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("general_id", generalId, TableAttributeData.DataType.LONG);
        // insert specialization
        insertTuple("exe_specialization", tuple, "addNewSpecialization", connection);
    }

    protected void addNewAlternate(Long alternate1Id, Long alternate2Id, Connection connection)
            throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("alternate1_id", alternate1Id, TableAttributeData.DataType.LONG);
        tuple.addAttribute("alternate2_id", alternate2Id, TableAttributeData.DataType.LONG);
        // insert alternate
        insertTuple("exe_alternate", tuple, "addNewAlternate", connection);
    }

    protected void addNewDerivation(DerivationType derivation, DerivationTypeEnum type, Long usedId,
                                    Long generatedId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("used_id", usedId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("generated_id", generatedId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("derivation_type", type.name(), TableAttributeData.DataType.STRING);
        // insert derivation
        Long derivationId = insertTuple("exe_derivation", tuple, "addNewDerivation", connection);
        // Insert derivation attributes
        if (derivation.getAttributes() != null) {
            addAttributes("exe_derivation_attribute", "derivation_id", derivationId,
                    derivation.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewCommunication(CommunicationType communication, Long informedId,
                                       Long informantId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("informed_id", informedId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("informant_id", informantId, TableAttributeData.DataType.LONG);
        // insert communication
        Long communicationId = insertTuple("exe_communication", tuple, "addNewCommunication", connection);
        // Insert communication attributes
        if (communication.getAttributes() != null) {
            addAttributes("exe_communication_attribute", "communication_id", communicationId,
                    communication.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewAssociation(AssociationType association, Long activityId,
                                     Long agentId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("agent_id", agentId, TableAttributeData.DataType.LONG);
        if (association.getPlanID() != null)
            tuple.addAttribute("plan_id", association.getPlanID(), TableAttributeData.DataType.STRING);
        Long associationId = insertTuple("exe_association", tuple, "addNewAssociation", connection);
        // Insert association attributes
        if (association.getAttributes() != null) {
            addAttributes("exe_association_attribute", "association_id", associationId,
                    association.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewDelegation(DelegationType delegation, Long delAgentId,
                                     Long resAgentId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("del_agent_id", delAgentId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("res_agent_id", resAgentId, TableAttributeData.DataType.LONG);
        // if there is an activity associated with the delegation, we have to store it
        if (delegation.getActivity() != null) {
            IngestionResult activityResult = addNewActivity(delegation.getActivity(), connection);
            // use it's id as a foreign key in delegation tuple
            tuple.addAttribute("activity_id", activityResult.getDbId(), TableAttributeData.DataType.LONG);
        }
        Long delId = insertTuple("exe_delegation", tuple, "addNewAssociation", connection);
        // Insert delegation attributes
        if (delegation.getAttributes() != null) {
            addAttributes("exe_delegation_attribute", "delegation_id", delId,
                    delegation.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewGeneration(GenerationType generation, Long activityId, 
                                    Long entityId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("entity_id", entityId, TableAttributeData.DataType.LONG);
        if (generation.isSetLocation())
            tuple.addAttribute("location", generation.getLocation(), TableAttributeData.DataType.STRING);
        if (generation.isSetTimestamp())
            tuple.addAttribute("generation_time", KomaduUtils.getTimestamp(generation.getTimestamp()),
                    TableAttributeData.DataType.TIMESTAMP);
        // Insert generation tuple
        Long generationId = insertTuple("exe_generation", tuple, "addNewGeneration", connection);
        // Insert generation attributes
        if (generation.getAttributes() != null) {
            addAttributes("exe_generation_attribute", "generation_id", generationId,
                    generation.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewUsage(UsageType usage, Long activityId,
                               Long entityId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("entity_id", entityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("location", usage.getLocation(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("usage_time", KomaduUtils.getTimestamp(usage.getTimestamp()),
                TableAttributeData.DataType.TIMESTAMP);
        // Insert usage tuple
        Long usageId = insertTuple("exe_usage", tuple, "addNewUsage", connection);
        // Insert usage attributes
        if (usage.getAttributes() != null) {
            addAttributes("exe_usage_attribute", "usage_id", usageId,
                    usage.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewStart(StartType start, Long activityId,
                               Long triggerId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("trigger_id", triggerId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("location", start.getLocation(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("start_time", KomaduUtils.getTimestamp(start.getTimestamp()),
                TableAttributeData.DataType.TIMESTAMP);
        // Insert start tuple
        Long startId = insertTuple("exe_start", tuple, "addNewStart", connection);
        // Insert start attributes
        if (start.getAttributes() != null) {
            addAttributes("exe_start_attribute", "start_id", startId,
                    start.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewEnd(EndType end, Long activityId, 
                             Long triggerId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("trigger_id", triggerId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("location", end.getLocation(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("end_time", KomaduUtils.getTimestamp(end.getTimestamp()), TableAttributeData.DataType.TIMESTAMP);
        // Insert end tuple
        Long endId = insertTuple("exe_end", tuple, "addNewEnd", connection);
        // Insert end attributes
        if (end.getAttributes() != null) {
            addAttributes("exe_end_attribute", "end_id", endId,
                    end.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewInvalidation(InvalidationType invalidation, Long activityId,
                                      Long entityId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_id", activityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("entity_id", entityId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("location", invalidation.getLocation(), TableAttributeData.DataType.STRING);
        tuple.addAttribute("invalidation_time", KomaduUtils.getTimestamp(invalidation.getTimestamp()), TableAttributeData.DataType.TIMESTAMP);
        // Insert invalidation tuple
        Long invalidationId = insertTuple("exe_invalidation", tuple, "addNewInvalidation", connection);
        // Insert invalidation attributes
        if (invalidation.getAttributes() != null) {
            addAttributes("exe_invalidation_attribute", "invalidation_id", invalidationId,
                    invalidation.getAttributes().getAttributeArray(), connection);
        }
    }

    protected void addNewAttribution(AttributionType attribution, Long agentId,
                                     Long entityId, Connection connection) throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("agent_id", agentId, TableAttributeData.DataType.LONG);
        tuple.addAttribute("entity_id", entityId, TableAttributeData.DataType.LONG);
        // Insert attribution tuple
        Long attributionId = insertTuple("exe_attribution", tuple, "addNewAttribution", connection);
        // Insert attribution attributes
        if (attribution.getAttributes() != null) {
            addAttributes("exe_attribution_attribute", "attribution_id", attributionId,
                    attribution.getAttributes().getAttributeArray(), connection);
        }
    }

    /**
     * Stores a given workflow activity into the database. A workflow activity can be a
     * workflow, service or a method
     *
     * @param activity     - ActivityType instance
     * @param connection   - db connection
     * @return id of the ingested tuple
     * @throws IngestException
     * @throws SQLException
     */
    protected IngestionResult addNewActivity(ActivityType activity, Connection connection)
            throws IngestException, SQLException {
        // resolve URIs depending on the type
        String activityUri;
        String contextWorkflowUri = null;
        String contextServiceUri = null;
        WorkflowInformationType workflowInfo;
        ActivityTypeEnum type;
        String location = activity.getLocation();

        // an activity can either be a workflow, service, method or a generic activity
        if (activity.getWorkflowInformation() != null) {
            workflowInfo = activity.getWorkflowInformation();
            activityUri = workflowInfo.getWorkflowID();
            type = ActivityTypeEnum.WORKFLOW;
        } else if (activity.getServiceInformation() != null) {
            workflowInfo = activity.getServiceInformation();
            activityUri = activity.getServiceInformation().getServiceID();
            contextWorkflowUri = workflowInfo.getWorkflowID();
            type = ActivityTypeEnum.SERVICE;
        } else if (activity.getMethodInformation() != null) {
            workflowInfo = activity.getMethodInformation();
            MethodInformationType methodInfo = (MethodInformationType) workflowInfo;
            activityUri = methodInfo.getMethodID();
            contextWorkflowUri = methodInfo.getWorkflowID();
            contextServiceUri = methodInfo.getServiceID();
            type = ActivityTypeEnum.METHOD;
        } else if (activity.getActivityInformation() != null) {
            return addNewGenericActivity(activity.getActivityInformation(), location, connection);
        } else {
            throw new IngestException("Activity not found");
        }

        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, activityUri, connection)) {
            // check whether the activity already exists
            ingestionResult = KomaduUtils.isActivityExists(activityUri, type, connection);
            if (ingestionResult == null) {
                // construct the tuple with attributes and values
                TupleData tuple = new TupleData();
                tuple.addAttribute("activity_uri", activityUri, TableAttributeData.DataType.STRING);
                tuple.addAttribute("activity_type", type.name(), TableAttributeData.DataType.STRING);
                if (contextWorkflowUri != null)
                    tuple.addAttribute("context_workflow_uri", contextWorkflowUri, TableAttributeData.DataType.STRING);
                if (contextServiceUri != null)
                    tuple.addAttribute("context_service_uri", contextServiceUri, TableAttributeData.DataType.STRING);
                tuple.addAttribute("timestep", workflowInfo.getTimestep(), TableAttributeData.DataType.INT);
                if (workflowInfo.getWorkflowNodeID() != null)
                    tuple.addAttribute("context_wf_node_id_token", workflowInfo.getWorkflowNodeID(),
                            TableAttributeData.DataType.STRING);
                if (location != null)
                    tuple.addAttribute("location", location, TableAttributeData.DataType.STRING);

                // handle instance of : store registry info
                if (workflowInfo.getInstanceOf() != null) {
                    tuple.addAttribute("instance_of", addNewActivityRegInfo(workflowInfo.getInstanceOf(),
                            type.name(), connection), TableAttributeData.DataType.LONG);
                }
                Long activityId = insertTuple("exe_activity", tuple, "addNewActivity", connection);
                // Insert activity attributes
                if (workflowInfo.getAttributes() != null) {
                    addAttributes("exe_activity_attribute", "activity_id", activityId,
                            workflowInfo.getAttributes().getAttributeArray(), connection);
                }
                ingestionResult = new IngestionResult(activityUri, activityId);
            }
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, activityUri, connection);
        }
        return ingestionResult;
    }

    protected IngestionResult addNewGenericActivity(ActivityInformationType genericActInfo, String location,
                                                    Connection connection) throws IngestException, SQLException {
        IngestionResult ingestionResult = null;
        // acquire lock before ingest
        String activity_uri = genericActInfo.getActivityID();
        if (KomaduUtils.manageDBLock(DBLockConstants.LOCK_ACQUIRE, activity_uri, connection)) {
            // check whether the activity already exists
            ingestionResult = KomaduUtils.isActivityExists(activity_uri, ActivityTypeEnum.GENERIC, connection);
            if (ingestionResult == null) {
                // construct the tuple with attributes and values
                TupleData tuple = new TupleData();
                tuple.addAttribute("activity_uri", activity_uri, TableAttributeData.DataType.STRING);
                tuple.addAttribute("activity_type", ActivityTypeEnum.GENERIC.name(), TableAttributeData.DataType.STRING);
                if (location != null)
                    tuple.addAttribute("location", location, TableAttributeData.DataType.STRING);
                Long activityId = insertTuple("exe_activity", tuple, "addNewGenericActivity", connection);
                // Insert activity attributes
                if (genericActInfo.getAttributes() != null) {
                    addAttributes("exe_activity_attribute", "activity_id", activityId,
                            genericActInfo.getAttributes().getAttributeArray(), connection);
                }
                ingestionResult = new IngestionResult(activity_uri, activityId);
            }
            KomaduUtils.manageDBLock(DBLockConstants.LOCK_RELEASE, activity_uri, connection);
        }
        return ingestionResult;
    }

    protected Long addNewActivityRegInfo(InstanceOfType instanceOfInfo, String activityType, Connection connection)
            throws IngestException, SQLException {
        // construct the tuple with attributes and values
        TupleData tuple = new TupleData();
        tuple.addAttribute("activity_type", activityType, TableAttributeData.DataType.STRING);
        tuple.addAttribute("activity_uri", instanceOfInfo.getInstanceOfID(), TableAttributeData.DataType.STRING);
        if (instanceOfInfo.getVersion() != null)
            tuple.addAttribute("version", instanceOfInfo.getVersion(), TableAttributeData.DataType.STRING);
        if (instanceOfInfo.getCreationTime() != null)
            tuple.addAttribute("creation_time", KomaduUtils.getTimestamp(instanceOfInfo.getCreationTime()),
                    TableAttributeData.DataType.TIMESTAMP);
        return insertTuple("reg_activity", tuple, "addNewActivityRegInfo", connection);
    }

    /**
     * Inserts an array of attributes to the given table
     *
     * @param tableName           table to add attributes
     * @param subjectIDColumnName name of the column which is a foreign key
     * @param internalID          foreign key
     * @param attributeList       list of attributes
     * @param connection          database connection
     * @throws SQLException
     * @throws IngestException
     */
    private void addAttributes(String tableName, String subjectIDColumnName,
                               long internalID, AttributeType[] attributeList,
                               Connection connection) throws SQLException, IngestException {
        PreparedStatement statement = null;
        try {
            if (attributeList != null && attributeList.length > 0) {
                StringBuilder builder = new StringBuilder("INSERT INTO " + tableName + " (" +
                        subjectIDColumnName + ", attribute_name, attribute_value, attribute_type) VALUES (?, ?, ?, ?)");
                int size = attributeList.length;
                for (int i = 1; i < size; i++) {
                    builder.append(",(?, ?, ?, ?)");
                }

                if (log.isDebugEnabled()) log.debug(builder.toString() + ": " + internalID);

                statement = connection.prepareStatement(builder.toString());

                for (int i = 0; i < size; i++) {
                    AttributeType attribute = attributeList[i];
                    String property = attribute.getProperty();
                    String value = attribute.getValue();
                    AttributeDefinitionScopeEnum scope = AttributeFactory.getScopeDefinition(property);

                    statement.setLong(i * 4 + 1, internalID);
                    statement.setString(i * 4 + 2, property);
                    statement.setString(i * 4 + 3, value);
                    statement.setString(i * 4 + 4, scope.name());
                }

                long startTime = 0;
                if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
                int result = statement.executeUpdate();
                if (plog.isTraceEnabled())
                    plog.trace("addAttributes DB INSERT time: " + (System.currentTimeMillis() - startTime));

                if (result != size) {
                    throw new IngestException("Failed to add into " + tableName);
                }
            }
        } finally {
            if (statement != null) {
                statement.close();
            }
        }
    }

    /**
     * Inserts a given tuple into the given table using the given connection
     *
     * @param tableName  - table to which tuple will be inserted
     * @param tuple      - data
     * @param operation  - insert operation name for logs
     * @param connection - database connection
     * @return key of the tuple inserted
     * @throws IngestException
     * @throws SQLException
     */
    private Long insertTuple(String tableName, TupleData tuple, String operation,
                             Connection connection) throws IngestException, SQLException {
        Long internalID = null;
        PreparedStatement statement = null;
        // strings to construct insert statement
        StringBuilder builder = new StringBuilder("INSERT INTO " + tableName + " (");
        StringBuilder tailBuilder = new StringBuilder("VALUES (");

        // loop through all attributes of the tuple and build the statement
        int att_length = tuple.getAttributeList().size();
        int i = 0;
        for (TableAttributeData attribute : tuple.getAttributeList()) {
            String query_connector = (i == att_length - 1) ? ")" : ", ";
            String tail_connector = (i == att_length - 1) ? ")" : ", ";
            if (attribute.getAttributeName() != null) {
                builder.append(attribute.getAttributeName());
                builder.append(query_connector);
                tailBuilder.append("?");
                tailBuilder.append(tail_connector);
            }
            i++;
        }

        try {
            statement = connection.prepareStatement(builder.toString() + tailBuilder.toString());
            // set values into the statement
            int index = 1;
            for (TableAttributeData attribute : tuple.getAttributeList()) {
                setValueToStatement(statement, attribute, index);
                index++;
            }
            // execute the query and measure time for logs
            long startTime = 0;
            if (plog.isTraceEnabled()) startTime = System.currentTimeMillis();
            int result = statement.executeUpdate();
            if (plog.isTraceEnabled()) plog.trace(operation + " DB INSERT time: " +
                    (System.currentTimeMillis() - startTime));

            if (result > 0) {
                internalID = getLastAutoID(connection);
            } else {
                throw new IngestException("Failed to add new user agent");
            }
        } finally {
            if (statement != null) {
                statement.close();
            }
        }
        return internalID;
    }

    private List<Long> getInternalId(String tableName, String idColumnName, String uriColumnName, String value,
                               Connection connection) throws IngestException, SQLException {
        PreparedStatement stmt = null;
        ResultSet result = null;
        List<Long> internalIds = new ArrayList<Long>();

        if (tableName == null || idColumnName == null || uriColumnName == null ||
                value == null || connection == null) {
            return internalIds;
        }

        try {
            stmt = connection.prepareStatement("SELECT " + idColumnName + " FROM " + tableName +
                    " WHERE " + uriColumnName + "= ?");
            stmt.setString(1, value);
            result = stmt.executeQuery();
            while (result.next()) {
                internalIds.add(result.getLong(idColumnName));
            }
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (result != null) {
                result.close();
            }
        }
        return internalIds;
    }

    /**
     * Sets value of the correct type to the given PreparedStatement
     *
     * @param statement - PreparedStatement instance
     * @param att       - Attribute instance with the value and the type
     * @param index     - index to be set on PreparedStatement
     * @throws SQLException
     */
    private void setValueToStatement(PreparedStatement statement, TableAttributeData att,
                                     int index) throws SQLException {
        switch (att.getType()) {
            case STRING: {
                statement.setString(index, (String) att.getValue());
                break;
            }
            case INT: {
                statement.setInt(index, (Integer) att.getValue());
                break;
            }
            case DOUBLE: {
                statement.setDouble(index, (Double) att.getValue());
                break;
            }
            case FLOAT: {
                statement.setFloat(index, (Float) att.getValue());
                break;
            }
            case LONG: {
                statement.setLong(index, (Long) att.getValue());
                break;
            }
            case SHORT: {
                statement.setShort(index, (Short) att.getValue());
                break;
            }
            case DATE: {
                statement.setDate(index, (Date) att.getValue());
                break;
            }
            case TIME: {
                statement.setTime(index, (Time) att.getValue());
                break;
            }
            case TIMESTAMP: {
                statement.setTimestamp(index, (Timestamp) att.getValue());
            }
        }
    }



}
