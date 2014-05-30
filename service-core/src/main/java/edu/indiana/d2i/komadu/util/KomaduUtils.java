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

import edu.indiana.d2i.komadu.ingest.IngestException;
import edu.indiana.d2i.komadu.ingest.IngestionResult;
import edu.indiana.d2i.komadu.ingest.db.BaseDBIngesterImplementer;
import edu.indiana.d2i.komadu.service.AgentEnumType;
import org.apache.log4j.Logger;
import org.apache.xmlbeans.XmlObject;
import org.apache.xmlbeans.XmlOptions;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.sql.*;
import java.util.Calendar;

public class KomaduUtils {

    public static final String CHECK_ACTIVITY_EXISTENCE = "SELECT activity_id FROM exe_activity " +
            "WHERE activity_uri = ? AND activity_type = ?";
    public static final String CHECK_AGENT_EXISTENCE = "SELECT agent_id FROM reg_agent " +
            "WHERE agent_uri = ? AND agent_type = ?";
    // entities
    public static final String CHECK_FILE_EXISTENCE = "SELECT file_id FROM exe_file WHERE file_uri = ?";
    public static final String CHECK_BLOCK_EXISTENCE = "SELECT block_id FROM exe_block WHERE block_uri = ?";
    public static final String CHECK_COLLECTION_EXISTENCE = "SELECT collection_id FROM exe_collection WHERE collection_uri = ?";
    public static final String CHECK_GENERIC_ENTITY_EXISTENCE = "SELECT generic_entity_id FROM exe_generic_entity WHERE generic_entity_uri = ?";

    private static Logger log = Logger.getLogger(KomaduUtils.class);

    /**
     * Calculate MD5 Checksum of a String
     *
     * @param content String whose MD5 to be calculated
     * @return MD5 checksum of the String, as a hex string
     *
     * @author Yiming Sun
     */
    public static String calculateMD5(String content) {
        String md5Sum = null;
        try {
            MessageDigest messageDigest = MessageDigest.getInstance("MD5");
            messageDigest.update(content.getBytes());
            byte[] digest = messageDigest.digest();
            BigInteger bigInteger = new BigInteger(digest);
            md5Sum = bigInteger.toString(16);
        } catch (NoSuchAlgorithmException e) {
            log.error("Error while generating MD5", e);
        }
        return md5Sum;
    }

    public static boolean manageDBLock(int lockOperation, String objectID, Connection connection)
            throws IngestException {
        CallableStatement lockStmt = null;
        int lockStatus = 0;
        int lockFailures = 0;
        int maxRetries = 1;
        int timeout = DBLockConstants.LOCK_WAIT_TIME;

        if (lockOperation == DBLockConstants.LOCK_ACQUIRE) {
            maxRetries = DBLockConstants.MAX_RETRIES;
        }
        boolean isLockAcquired = false;
        try{
            for (int i = 0; i < maxRetries; i++) {
                lockStmt = connection.prepareCall("{call PR_OBJECT_LOCK(?, ?, ?, ?)}");
                try{
                    int actualTimeout = timeout * i * 2;
                    lockStmt.setInt(1, lockOperation);
                    lockStmt.setInt(2, actualTimeout);
                    lockStmt.setString(3, objectID);
                    lockStmt.registerOutParameter(4, java.sql.Types.INTEGER);
                    lockStmt.execute();
                    lockStatus = lockStmt.getInt(4);
                } catch(SQLException e){
                    lockFailures++;
                    if (lockFailures == maxRetries) {
                        String msg = "Max retries " + maxRetries +
                                " for the lock reached for the object: " + objectID;
                        if (log.isDebugEnabled()) log.debug("manageDBLock-Error: " + msg);
                        throw new IngestException(msg);
                    }
                }
                if (lockStatus == DBLockConstants.LOCK_OP_SUCCESS) {
                    isLockAcquired = true;
                    break;
                }
            }
        } catch(SQLException e) {
            String msg = "SQLException during call to PR_OBJECT_LOCK";
            if (log.isDebugEnabled()) log.debug("manageDBLock-Error: " + msg + ":" +e.getMessage());
            throw new IngestException(msg);
        } finally{
            try{
                lockStmt.close();
            } catch(SQLException e){
                if (log.isDebugEnabled()) log.debug("manageDBLock-Error: " + e.getMessage());
            }
            lockStmt = null;
        }
        if(lockStatus != DBLockConstants.LOCK_OP_SUCCESS){
            String msg = "Lock not obtained after " + maxRetries +
                    " retries for the lock reached for the object: " + objectID;
            if (log.isDebugEnabled()) log.debug("manageDBLock-Error: " + msg);
            throw new IngestException(msg);
        }
        return isLockAcquired;
    }

    public static IngestionResult isActivityExists(String activity_uri, BaseDBIngesterImplementer.ActivityTypeEnum type,
                                                   Connection connection) throws SQLException {
        if (log.isDebugEnabled()) log.debug("activity uri: " + activity_uri);
        IngestionResult ingestionResult = null;
        ResultSet resultSet = null;
        PreparedStatement statement = null;
        try {
            statement = connection.prepareStatement(CHECK_ACTIVITY_EXISTENCE);
            statement.setString(1, activity_uri);
            statement.setString(2, type.name());
            // execute the query
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                long activity_id = resultSet.getLong("activity_id");
                ingestionResult = new IngestionResult(activity_uri, activity_id);
            }
        } finally {
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }
            if (statement != null) {
                statement.close();
                statement = null;
            }
        }
        return ingestionResult;
    }

    public static IngestionResult isAgentExists(String agent_uri, AgentEnumType.Enum type,
                                                Connection connection) throws SQLException {
        if (log.isDebugEnabled()) log.debug("agent uri: " + agent_uri);
        IngestionResult ingestionResult = null;
        ResultSet resultSet = null;
        PreparedStatement statement = null;
        try {
            statement = connection.prepareStatement(CHECK_AGENT_EXISTENCE);
            statement.setString(1, agent_uri);
            statement.setString(2, type.toString());
            // execute the query
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                long agent_id = resultSet.getLong("agent_id");
                ingestionResult = new IngestionResult(agent_uri, agent_id);
            }
        } finally {
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }
            if (statement != null) {
                statement.close();
                statement = null;
            }
        }
        return ingestionResult;
    }

    public static IngestionResult isEntityExists(String entity_uri, BaseDBIngesterImplementer.EntityTypeEnum type,
                                                 Connection connection) throws SQLException {
        if (log.isDebugEnabled()) log.debug("entity uri: " + entity_uri);
        IngestionResult ingestionResult = null;
        ResultSet resultSet = null;
        PreparedStatement statement = null;
        try {
            if (type == BaseDBIngesterImplementer.EntityTypeEnum.FILE)
                statement = connection.prepareStatement(CHECK_FILE_EXISTENCE);
            else if (type == BaseDBIngesterImplementer.EntityTypeEnum.BLOCK)
                statement = connection.prepareStatement(CHECK_BLOCK_EXISTENCE);
            else if (type == BaseDBIngesterImplementer.EntityTypeEnum.COLLECTION)
                statement = connection.prepareStatement(CHECK_COLLECTION_EXISTENCE);
            else if (type == BaseDBIngesterImplementer.EntityTypeEnum.GENERIC)
                statement = connection.prepareStatement(CHECK_GENERIC_ENTITY_EXISTENCE);
            statement.setString(1, entity_uri);
            // execute the query
            resultSet = statement.executeQuery();
            if (resultSet.next()) {
                long entity_id = resultSet.getLong(1);
                ingestionResult = new IngestionResult(entity_uri, entity_id);
            }
        } finally {
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }
            if (statement != null) {
                statement.close();
                statement = null;
            }
        }
        return ingestionResult;
    }

    /**
     * converts an XmlObject into a pretty printed string
     *
     * @param any XmlObject
     * @return converted string
     */
    public static String anyTypeToString(XmlObject any) {
        return any.xmlText(new XmlOptions().setSavePrettyPrint());
    }

    /**
     * Converts Calendar to java.sql.Timestamp
     *
     * @param time Calendar
     * @return Timestamp
     */
    public static Timestamp getTimestamp(Calendar time) {
        return new Timestamp(time.getTimeInMillis());
    }

    /*
	 * This function converts a Timestamp object to a Calendar object.
	 *
	 * @param - Timestamp t
	 * @return - Calendar : calendar object which represents the input timestamp.
	 */
    public static Calendar getCalendarFromTimeStamp(Timestamp t) {
        Calendar c = Calendar.getInstance();
        c.setTimeInMillis(t.getTime());
        return c;
    }

}
