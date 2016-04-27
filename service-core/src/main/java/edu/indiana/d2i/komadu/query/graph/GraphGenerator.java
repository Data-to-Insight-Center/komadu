package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.ingest.db.BaseDBIngesterImplementer;
import edu.indiana.d2i.komadu.query.DetailEnumType;
import edu.indiana.d2i.komadu.query.PROVSqlQuery;
import edu.indiana.d2i.komadu.query.QueryConstants;
import edu.indiana.d2i.komadu.query.QueryException;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.xmlbeans.XmlException;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.xml.Other;
import org.w3.www.ns.prov.Document;

import javax.xml.namespace.QName;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Calendar;

public abstract class GraphGenerator {

    private static final Log l = LogFactory.getLog(GraphGenerator.class);

    protected static org.openprovenance.prov.xml.ProvFactory pFactory = new org.openprovenance.prov.xml.ProvFactory();

    /**
     * First checks whether the requested graph is in the cache. If yes, returns the graph. If not
     * computes the graph and puts it into the cache and returns
     */
    public Document getProvGraph(Connection connection,
                                 String graphURI,
                                 DetailEnumType.Enum informationDetailLevel,
                                 String cachePrefix,
                                 long cacheExpiration)
            throws QueryException, SQLException, IOException {
        Document provGraph = null;

        PreparedStatement statement = null;
        PreparedStatement getCountStatement = null;
        ResultSet resultSet = null;
        ResultSet rs = null;
        ByteArrayInputStream byteArrayInputStream = null;

        try {
            statement = connection.prepareStatement(PROVSqlQuery.GET_CACHE_GRAPH);
            statement.setString(1, cachePrefix + graphURI);
            if (informationDetailLevel.equals(DetailEnumType.FINE)) {
                statement.setBoolean(2, true);
            } else {
                statement.setBoolean(2, false);
            }
            resultSet = statement.executeQuery();

            boolean isCached;
            boolean isDirty;
            int id = 0;
            if (resultSet.next()) {
                isDirty = resultSet.getBoolean("dirty");
                // get graph ID
                id = resultSet.getInt(1);
                // get full cached graph
                String cachedGraph = resultSet.getString(3);
                isCached = true;

                Timestamp currentTime = new java.sql.Timestamp(Calendar
                        .getInstance().getTimeInMillis());
                Timestamp lastQueriedTime = resultSet.getTimestamp(4);

                long difference = currentTime.getTime() - lastQueriedTime.getTime();
                l.debug("Last query was issued " + difference + " milliseconds ago..");

                if (difference > cacheExpiration) {
                    isDirty = true; // force record to be dirty and update.
                }

                // If the cached graph is not dirty, return it
                if (!isDirty) {
                    l.info("Returning cached graph.");

                    if (statement != null) {
                        statement.close();
                        statement = null;
                    }

                    if (resultSet != null) {
                        resultSet.close();
                        resultSet = null;
                    }

                    statement = connection.prepareStatement(PROVSqlQuery.UPDATE_QUERY_DATE);
                    statement.setTimestamp(1, new java.sql.Timestamp(Calendar
                            .getInstance().getTimeInMillis()));
                    statement.setInt(2, id);
                    statement.execute();
                    statement.close();
                    // parse the PROV Document and return it
                    provGraph = Document.Factory.parse(cachedGraph);
                    return provGraph;
                }
            } else {
                l.info("Query has not been cached.");
                isCached = false;
            }
            if (statement != null) {
                statement.close();
                statement = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }

            // If the graph is not cached or cache is already expired, we come here and create
            // the graph from the scratch
            long beginTime = System.currentTimeMillis();
            provGraph = computeProvGraph(connection, graphURI, informationDetailLevel);
            long endTime = System.currentTimeMillis();
            long generationTime = endTime - beginTime;
            if (!isCached) {
                // graph is not cached
                getCountStatement = connection
                        .prepareStatement(PROVSqlQuery.GET_CACHE_COUNT);
                rs = getCountStatement.executeQuery();
                if (rs.next()) {
                    if (rs.getInt(1) == QueryConstants.MAX_CACHE_ENTRIES) {
                        statement = connection
                                .prepareStatement(PROVSqlQuery.GET_GRAPH_TO_DELETE);
                        resultSet = statement.executeQuery();
                        if (resultSet.next()) {
                            resultSet.deleteRow();
                        }
                        if (statement != null) {
                            statement.close();
                            statement = null;
                        }

                        if (resultSet != null) {
                            resultSet.close();
                            resultSet = null;
                        }
                    }

                    statement = connection.prepareStatement(PROVSqlQuery.NEW_CACHE_GRAPH);
                    byteArrayInputStream = new ByteArrayInputStream(provGraph
                            .xmlText().getBytes());

                    statement.setString(1, cachePrefix + graphURI);
                    statement.setBinaryStream(2, byteArrayInputStream);
                    statement.setString(3, String.valueOf(generationTime));
                    statement.setTimestamp(4, new java.sql.Timestamp(Calendar
                            .getInstance().getTimeInMillis()));

                    if (informationDetailLevel == DetailEnumType.FINE) {
                        statement.setBoolean(5, true);
                    } else {
                        statement.setBoolean(5, false);
                    }

                }

                getCountStatement.close();
                l.info("Caching graph.");
            } else {
                // dirty bit was set so update
                byteArrayInputStream = new ByteArrayInputStream(provGraph
                        .xmlText().getBytes());
                statement = connection.prepareStatement(PROVSqlQuery.UPDATE_CACHE_GRAPH);
                statement.setBinaryStream(1, byteArrayInputStream);
                statement.setBoolean(2, false);
                statement.setString(3, String.valueOf(generationTime));
                statement.setTimestamp(4, new java.sql.Timestamp(Calendar
                        .getInstance().getTimeInMillis()));
                statement.setInt(5, id);
                l.info("Updating cache graph.");
            }

            if (statement != null) {
                statement.executeUpdate();
                statement.close();
            }

        } catch (SQLException e) {
            l.error("Exiting getProvGraph() with SQL errors");
            l.error(e.toString());
            return provGraph;
        } catch (XmlException e) {
            l.error("Exiting getProvGraph() with XML parse errors");
            l.error(e.toString());
            return null;
        } finally {
            if (statement != null) {
                statement.close();
            }
            if (getCountStatement != null) {
                getCountStatement.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
            if (rs != null) {
                rs.close();
            }
            if (byteArrayInputStream != null) {
                byteArrayInputStream.close();
            }
        }

        l.debug("Exiting getProvGraph() with success");
        return provGraph;
    }

    protected abstract Document computeProvGraph(Connection connection,
                                                 String graphURI,
                                                 DetailEnumType.Enum informationDetailLevel)
            throws QueryException, SQLException;

    /**
     * Reads attributes from the *_attribute relation in the database using the given query
     * and creates PROV attributes and sets those to the given element.
     *
     * @param query - query which reads the *_attribute relation
     * @param elementID - id to retrieve attributes. Eg: agent_id in the case of agent attributes
     * @param element - element can be any of the basic components or their relationships
     * @param connection - MySQL connection to read the database
     * @throws SQLException - on SQL errors
     */
    protected void addCustomAttributes(String query, String elementID, HasOther element,
                                     Connection connection) throws SQLException {
        assert (connection != null);
        assert (elementID != null);
        l.debug("Entering addCustomAttributes()");

        PreparedStatement activityAttStmt = null;
        ResultSet activityAttResult = null;

        try {
            activityAttStmt = connection
                    .prepareStatement(query);
            activityAttStmt.setString(1, elementID);
            activityAttResult = activityAttStmt.executeQuery();

            while (activityAttResult.next()) {
                String attName = activityAttResult.getString(3);
                String attType = activityAttResult.getString(5);
                String value = activityAttResult.getString(4);
                Other provAtt = pFactory.newOther(getExtAttQName(attName),
                        value, Name.QNAME_XSD_STRING);
                pFactory.addAttribute(element, provAtt);
            }

            l.debug("Exiting addCustomAttributes() with success");

        } catch (SQLException e) {
            l.error("Exiting addCustomAttributes() with error");
            l.error(e.toString());
        } finally {
            if (activityAttStmt != null) {
                activityAttStmt.close();
            }

            if (activityAttResult != null) {
                activityAttResult.close();
            }
        }
    }

    /**
     * Creates a prov entity using the given entity Id. First queries the exe_entity table to
     * get the type of the entity and then queries the relevant table to get further information.
     *
     * @param entityId - entity Id in the database
     * @return Entity instance or null if there's no such entity
     */
    protected Entity createEntity(String entityId, Connection connection) throws SQLException {
        assert (entityId != null);
        l.debug("Entering createEntity()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        Entity entity = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_ENTITY_TYPE);
            stmt.setString(1, entityId);
            resultSet = stmt.executeQuery();
            String entityType;

            if (resultSet.next()) {
                entityType = resultSet.getString("entity_type");
            } else {
                return null;
            }
            // close the statement and result set
            if (stmt != null) {
                stmt.close();
                stmt = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }
            // The entity can be a file, block, collection or a generic entity
            if (entityType.equals(BaseDBIngesterImplementer.EntityTypeEnum.FILE.name())) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_FILE_BY_ID);
                stmt.setString(1, entityId);
                resultSet = stmt.executeQuery();
                while (resultSet.next()) {
                    String fileURI = resultSet.getString("file_uri");
                    String size = resultSet.getString("size");
                    String creationDate = resultSet.getString("creation_date");
                    String fileName = resultSet.getString("file_name");
                    String md5 = resultSet.getString("md5_checksum");
                    entity = newEntity(QueryConstants.FILE_IDENTIFIER + entityId,
                            fileURI, QueryConstants.ENTITY_FILE);
                    // add size as an additional attribute
                    if (size != null) {
                        Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, sizeAtt);
                    }
                    if (creationDate != null) {
                        Other dateAtt = pFactory.newOther(getKomaduAttQName("creation-date"), creationDate, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, dateAtt);
                    }
                    if (fileName != null) {
                        Other nameAtt = pFactory.newOther(getKomaduAttQName("file-name"), fileName, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, nameAtt);
                    }
                    if (md5 != null) {
                        Other md5Att = pFactory.newOther(getKomaduAttQName("md5_checksum"), md5, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, md5Att);
                    }
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            entityId, entity, connection);
                }
                // close the statement and result set
                if (stmt != null) {
                    stmt.close();
                    stmt = null;
                }
                if (resultSet != null) {
                    resultSet.close();
                    resultSet = null;
                }
            } else if (entityType.equals(BaseDBIngesterImplementer.EntityTypeEnum.BLOCK.name())) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_BLOCK_BY_ID);
                stmt.setString(1, entityId);
                resultSet = stmt.executeQuery();
                while (resultSet.next()) {
                    String blockUri = resultSet.getString("block_uri");
                    String size = resultSet.getString("size");
                    String blockContent = resultSet.getString("block_content");
                    String md5 = resultSet.getString("md5_checksum");
                    entity = newEntity(QueryConstants.BLOCK_IDENTIFIER + entityId,
                            blockUri, QueryConstants.ENTITY_BLOCK);
                    // add size as an additional attribute
                    if (size != null) {
                        Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, sizeAtt);
                    }
                    if (blockContent != null) {
                        Other contentAtt = pFactory.newOther(getKomaduAttQName("content"), blockContent, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, contentAtt);
                    }
                    if (md5 != null) {
                        Other md5Att = pFactory.newOther(getKomaduAttQName("md5_checksum"), md5, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(entity, md5Att);
                    }

                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            entityId, entity, connection);
                }
                // close the statement and result set
                if (stmt != null) {
                    stmt.close();
                    stmt = null;
                }
                if (resultSet != null) {
                    resultSet.close();
                    resultSet = null;
                }
            } else if (entityType.equals(BaseDBIngesterImplementer.EntityTypeEnum.COLLECTION.name())) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_COLLECTION_BY_ID);
                stmt.setString(1, entityId);
                resultSet = stmt.executeQuery();
                while (resultSet.next()) {
                    String collectionUri = resultSet.getString("collection_uri");
                    entity = newEntity(QueryConstants.COLLECTION_IDENTIFIER + entityId,
                            collectionUri, QueryConstants.ENTITY_COLLECTION);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            entityId, entity, connection);
                }
                // close the statement and result set
                if (stmt != null) {
                    stmt.close();
                    stmt = null;
                }
                if (resultSet != null) {
                    resultSet.close();
                    resultSet = null;
                }
            } else if (entityType.equals(BaseDBIngesterImplementer.EntityTypeEnum.GENERIC.name())) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_GENERIC_ENTITY_BY_ID);
                stmt.setString(1, entityId);
                resultSet = stmt.executeQuery();
                while (resultSet.next()) {
                    String genericEntityUri = resultSet.getString("generic_entity_uri");
                    entity = newEntity(QueryConstants.ENTITY_IDENTIFIER + entityId,
                            genericEntityUri, QueryConstants.ENTITY_GENERIC);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            entityId, entity, connection);
                }
                // close the statement and result set
                if (stmt != null) {
                    stmt.close();
                    stmt = null;
                }
                if (resultSet != null) {
                    resultSet.close();
                    resultSet = null;
                }
            }

            l.debug("Exiting createEntity() with success");
        } catch (SQLException e) {
            l.error("Exiting createEntity() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }

            if (resultSet != null) {
                resultSet.close();
            }
        }
        return entity;
    }

    protected void addDerivationType(String derivationType, WasDerivedFrom derivedFrom) {
        // if this is a revision, quotation or primary source, add type
        if (derivationType.equals(BaseDBIngesterImplementer.DerivationTypeEnum.REVISION.name())) {
            derivedFrom.getType().add(pFactory.newType(Name.QNAME_PROV_REVISION, Name.QNAME_XSD_QNAME));
        } else if (derivationType.equals(BaseDBIngesterImplementer.DerivationTypeEnum.QUOTATION.name())) {
            derivedFrom.getType().add(pFactory.newType(Name.QNAME_PROV_QUOTATION, Name.QNAME_XSD_QNAME));
        } else if (derivationType.equals(BaseDBIngesterImplementer.DerivationTypeEnum.PRIMARY_SOURCE.name())) {
            derivedFrom.getType().add(pFactory.newType(Name.QNAME_PROV_PRIMARY_SOURCE, Name.QNAME_XSD_QNAME));
        }
    }

    // External customer attributes
    protected static QName getExtAttQName(String n) {
        return new QName(QueryConstants.KOMADU_EXTERNAL_NS, n, QueryConstants.KOMADU_EXTERNAL_PREFIX);
    }

    protected static QName getKomaduAttQName(String n) {
        return new QName(QueryConstants.KOMADU_NS, n, QueryConstants.KOMADU_PREFIX);
    }

    protected static QName getIdQName(String n) {
        return new QName(QueryConstants.KOMADU_NS, n, QueryConstants.KOMADU_PREFIX);
    }

    protected static Agent newAgent(String id, String url, String type) {
        Agent agent = pFactory.newAgent(getIdQName(id));
        // add a custom type attribute
        Other typeAtt = pFactory.newOther(getKomaduAttQName("type"), type, Name.QNAME_XSD_STRING);
        pFactory.addAttribute(agent, typeAtt);
        // add a url attribute too
        Other urlAtt = pFactory.newOther(getKomaduAttQName("url"), url, Name.QNAME_XSD_STRING);
        pFactory.addAttribute(agent, urlAtt);
        return agent;
    }

    protected static Entity newEntity(String id, String url, String type) {
        Entity entity = pFactory.newEntity(getIdQName(id));
        if (type.equals(QueryConstants.ENTITY_COLLECTION)) {
            // add a prov type for collection
            entity.getType().add(pFactory.newType(Name.newProvQName(type), Name.QNAME_XSD_QNAME));
        } else {
            // add a custom type attribute
            Other typeAtt = pFactory.newOther(getKomaduAttQName("type"), type, Name.QNAME_XSD_STRING);
            pFactory.addAttribute(entity, typeAtt);
        }
        // add a url attribute too
        Other urlAtt = pFactory.newOther(getKomaduAttQName("url"), url, Name.QNAME_XSD_STRING);
        pFactory.addAttribute(entity, urlAtt);
        return entity;
    }

}
