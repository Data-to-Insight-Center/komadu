package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.query.EntityEnumType;
import edu.indiana.d2i.komadu.query.PROVSqlQuery;
import edu.indiana.d2i.komadu.query.QueryConstants;
import edu.indiana.d2i.komadu.query.QueryException;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.Name;
import org.openprovenance.prov.xml.Other;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class EntityGraphGenerator extends NonContextGraphGenerator {

    private static final Log l = LogFactory.getLog(EntityGraphGenerator.class);

    private EntityEnumType.Enum entityType;

    public EntityGraphGenerator(EntityEnumType.Enum entityType) {
        this.entityType = entityType;
    }

    @Override
    protected void populateRoot(Connection connection, String entityURI)
            throws QueryException, SQLException {
        if (entityType == null) {
            throw new QueryException("Entity type not set");
        }
        // find this entity in the database and get the db id
        int rootID = createEntityByURI(connection, entityURI);
        // push the id to the unexpanded node stack
        unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, rootID));
    }

    private int createEntityByURI(Connection connection, String entityURI) throws SQLException {
        assert (entityURI != null);
        l.debug("Entering createEntityByURI()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        int entityID = -1;

        try {
            // The entity can be a file, block, collection or a generic entity
            if (entityType.equals(EntityEnumType.FILE)) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_FILE_BY_URI);
                stmt.setString(1, entityURI);
                resultSet = stmt.executeQuery();

                if (resultSet.next()) {
                    entityID = resultSet.getInt("file_id");
                    String size = resultSet.getString("size");
                    String creationDate = resultSet.getString("creation_date");
                    String fileName = resultSet.getString("file_name");
                    String md5 = resultSet.getString("md5_checksum");
                    Entity entity = newEntity(QueryConstants.FILE_IDENTIFIER + entityID,
                            entityURI, QueryConstants.ENTITY_FILE);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, sizeAtt);
                    Other dateAtt = pFactory.newOther(getKomaduAttQName("creation-date"), creationDate, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, dateAtt);
                    Other nameAtt = pFactory.newOther(getKomaduAttQName("file-name"), fileName, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, nameAtt);
                    Other md5Att = pFactory.newOther(getKomaduAttQName("md5_checksum"), md5, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, md5Att);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            "" + entityID, entity, connection);
                    // add to entity list
                    entities.put(entityID, entity);
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
            } else if (entityType.equals(EntityEnumType.BLOCK)) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_BLOCK_BY_URI);
                stmt.setString(1, entityURI);
                resultSet = stmt.executeQuery();

                if (resultSet.next()) {
                    entityID = resultSet.getInt("block_id");
                    String size = resultSet.getString("size");
                    String blockContent = resultSet.getString("block_content");
                    String md5 = resultSet.getString("md5_checksum");
                    Entity entity = newEntity(QueryConstants.BLOCK_IDENTIFIER + entityID,
                            entityURI, QueryConstants.ENTITY_BLOCK);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, sizeAtt);
                    Other contentAtt = pFactory.newOther(getKomaduAttQName("content"), blockContent, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, contentAtt);
                    Other md5Att = pFactory.newOther(getKomaduAttQName("md5_checksum"), md5, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(entity, md5Att);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            "" + entityID, entity, connection);
                    // add to entity list
                    entities.put(entityID, entity);
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
            } else if (entityType.equals(EntityEnumType.COLLECTION)) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_COLLECTION_BY_URI);
                stmt.setString(1, entityURI);
                resultSet = stmt.executeQuery();

                if (resultSet.next()) {
                    entityID = resultSet.getInt("collection_id");
                    Entity entity = newEntity(QueryConstants.COLLECTION_IDENTIFIER + entityID,
                            entityURI, QueryConstants.ENTITY_COLLECTION);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            "" + entityID, entity, connection);
                    // add to entity list
                    entities.put(entityID, entity);
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
            } else if (entityType.equals(EntityEnumType.GENERIC)) {
                stmt = connection.prepareStatement(PROVSqlQuery.GET_GENERIC_ENTITY_BY_URI);
                stmt.setString(1, entityURI);
                resultSet = stmt.executeQuery();

                if (resultSet.next()) {
                    entityID = resultSet.getInt("generic_entity_id");
                    Entity entity = newEntity(QueryConstants.ENTITY_IDENTIFIER + entityID,
                            entityURI, QueryConstants.ENTITY_GENERIC);
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ENTITY_ATTRIBUTES_BY_ID,
                            "" + entityID, entity, connection);
                    // add to entity list
                    entities.put(entityID, entity);
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

            l.debug("Exiting createEntityByURI() with success");
        } catch (SQLException e) {
            l.error("Exiting createEntityByURI() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
        return entityID;
    }

}
