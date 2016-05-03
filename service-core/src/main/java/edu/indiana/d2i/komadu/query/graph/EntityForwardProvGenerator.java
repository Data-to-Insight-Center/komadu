package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.query.*;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.xml.ProvSerialiser;
import org.w3.www.ns.prov.Document;

import javax.xml.namespace.QName;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;

public class EntityForwardProvGenerator extends EntityGraphGenerator {

    private static final Log l = LogFactory.getLog(EntityForwardProvGenerator.class);

    public EntityForwardProvGenerator(EntityEnumType.Enum entityType) {
        super(entityType);
    }

    @Override
    protected Document computeProvGraph(Connection connection, String graphURI,
                                        DetailEnumType.Enum informationDetailLevel)
            throws QueryException, SQLException {
        assert (connection != null);
        assert (graphURI != null);
        l.debug("Entering NonContextGraphGenerator.computeProvGraph()");

        // initialize global maps
        activities = new HashMap<Integer, Activity>();
        entities = new HashMap<Integer, Entity>();
        agents = new HashMap<Integer, Agent>();
        relationships = new HashMap<String, Statement>();
        // initialize map node stack
        unexpandedNodes = new Stack<GraphNode>();

        infoDetailLevel = informationDetailLevel;

        // create the root node of the graph depending on the graph type
        populateRoot(connection, graphURI);

        // build the graph in Depth-First manner
        while (!unexpandedNodes.empty()) {
            GraphNode node = unexpandedNodes.pop();
            GraphNode.NodeType type = node.getType();
            if (type == GraphNode.NodeType.ACTIVITY) {
                expandActivityNode(connection, node.getInternalID());
            } else if (type == GraphNode.NodeType.ENTITY) {
                expandEntityNode(connection, node.getInternalID());
            }
            // we don't need to expand agent nodes for forward provenance
        }

        // now we have to build the PROV graph
        Collection<Activity> activityValues = activities.values();
        Collection<Entity> entityValues = entities.values();
        Collection<Agent> agentValues = agents.values();
        Collection<Statement> relationshipValues = relationships.values();

        // create the PROV graph using prov-toolbox library's api
        org.openprovenance.prov.model.Document graph = pFactory.newDocument(
                activityValues.toArray(new Activity[activityValues.size()]),
                entityValues.toArray(new Entity[entityValues.size()]),
                agentValues.toArray(new Agent[agentValues.size()]),
                relationshipValues.toArray(new Statement[relationships.size()]));
        graph.setNamespace(Namespace.gatherNamespaces(graph));
        /*
         * Now we have to serialize the created graph and parse it to the Xmlbean type that
         * we want to return
         */
        ProvSerialiser serializer = ProvSerialiser.getThreadProvSerialiser();
        Document provGraph = null;
        try {
            ByteArrayOutputStream os = new ByteArrayOutputStream();
            serializer.serialiseDocument(os, graph, true);
            ByteArrayInputStream is = new ByteArrayInputStream(os.toByteArray());
            provGraph = org.w3.www.ns.prov.Document.Factory.parse(is);
        } catch (Exception e) {
            l.error("Error while serializing the prov-toolbox graph..", e);
        }
        return provGraph;
    }

    /**
     * Takes the database id of an activity. This method assumes that this particular activity
     * has already been populated. This method only expands it to find out adjacent nodes.
     */
    private void expandActivityNode(Connection connection, int activityID)
            throws QueryException, SQLException {
        // consider communications and find out related activities
        addCommunications(connection, activityID);
        // find related entities through activity-entity relationships
        addGenerations(connection, PROVSqlQuery.GET_GENERATIONS_BY_ACTIVITY_ID, activityID);
        addInvalidations(connection, PROVSqlQuery.GET_INVALIDATIONS_BY_ACTIVITY_ID, activityID);
    }

    /**
     * Takes the database id of an entity. This method assumes that this particular entity
     * has already been populated. This method only expands it to find out adjacent nodes.
     */
    private void expandEntityNode(Connection connection, int entityID)
            throws QueryException, SQLException {
        // find related activities through activity-entity relationships
        addUsages(connection, PROVSqlQuery.GET_USAGES_BY_ENTITY_ID, entityID);
        addStarts(connection, PROVSqlQuery.GET_STARTS_BY_ENTITY_ID, entityID);
        addEnds(connection, PROVSqlQuery.GET_ENDS_BY_ENTITY_ID, entityID);
        // find related entities through entity-entity relationships
        addDerivations(connection, entityID);
        addAlternates(connection, entityID);
        addSpecializations(connection, entityID);
        addMemberships(connection, entityID);
    }

    protected void addDerivations(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addDerivations()");

        /**
         * There are 2 possible cases here.
         * 1. There is a derivation notification in the database relating the given entityID and
         *    some other entity. In this case we directly map it into a derivation relationship in the graph.
         * 2. activity1 uses entity1 and generates entity2. But there's no derivation notification
         *    in the database for entity1 and entity2. In this case, we have to infer the derivation.
         */

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            // Case 1
            stmt = connection.prepareStatement(PROVSqlQuery.GET_DERIVATIONS_BY_USED_ENTITY_ID);
            stmt.setInt(1, entityID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String derivationId = resultSet.getString("derivation_id");
                int usedId = resultSet.getInt("used_id");
                int generatedId = resultSet.getInt("generated_id");
                String derivationType = resultSet.getString("derivation_type");

                // check whether the relationship already exists, if yes, don't add it again
                String entityEntityID = getEntityEntityId(usedId, generatedId);
                if (relationships.get(entityEntityID) != null) {
                    continue;
                }

                // get entities from list
                Entity usedEntity = entities.get(usedId);
                if (usedEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(usedId, createEntity("" + usedId, connection));
                    // now the entity must be in the map
                    usedEntity = entities.get(usedId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, usedId));
                }
                Entity generatedEntity = entities.get(generatedId);
                if (generatedEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(generatedId, createEntity("" + generatedId, connection));
                    // now the entity must be in the map
                    generatedEntity = entities.get(generatedId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, generatedId));
                }

                // create the relationship
                WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                        derivationId), generatedEntity.getId(), usedEntity.getId());
                // if this is a revision, quotation or primary source, add type
                addDerivationType(derivationType, derivedFrom);

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DERIVATION_ATTRIBUTES_BY_ID,
                            derivationId, derivedFrom, connection);
                }

                // add the derivation element into the list of relationships
                relationships.put(entityEntityID, derivedFrom);
            }
            if (stmt != null) {
                stmt.close();
                stmt = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }

            // Case 2
            stmt = connection.prepareStatement(PROVSqlQuery.GET_DERIVATIONS_BY_ACTIVITY_BY_USED_ENTITY_NO_CONTEXT);
            stmt.setInt(1, entityID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                int generatedId = resultSet.getInt("gen_id");
                int usedId = resultSet.getInt("used_id");

                // check whether the relationship already exists, if yes, don't add it again
                String entityEntityID = getEntityEntityId(usedId, generatedId);
                if (relationships.get(entityEntityID) != null) {
                    continue;
                }

                // get entities from list
                Entity usedEntity = entities.get(usedId);
                if (usedEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(usedId, createEntity("" + usedId, connection));
                    // now the entity must be in the map
                    usedEntity = entities.get(usedId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, usedId));
                }
                Entity generatedEntity = entities.get(generatedId);
                if (generatedEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(generatedId, createEntity("" + generatedId, connection));
                    // now the entity must be in the map
                    generatedEntity = entities.get(generatedId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, generatedId));
                }
                // create the relationship
                WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                        usedId + "_" + generatedId), generatedEntity.getId(), usedEntity.getId());
                // add the used element into the list of relationships
                relationships.put(entityEntityID, derivedFrom);
            }

            l.debug("addDerivations() successful");
        } catch (SQLException e) {
            l.error("Exiting addDerivations() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
    }

    protected void addAlternates(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addAlternates()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_ALTERNATES_BY_ALT2_ENTITY_ID);
            stmt.setInt(1, entityID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                int alt1 = resultSet.getInt("alternate1_id");
                int alt2 = resultSet.getInt("alternate2_id");

                // check whether the relationship already exists, if yes, don't add it again
                String entityEntityId = getEntityEntityId(alt1, alt2);
                if (relationships.get(entityEntityId) != null) {
                    continue;
                }

                // get entities from list
                Entity alt1Entity = entities.get(alt1);
                if (alt1Entity == null) {
                    // this is a new entity, so populate it
                    entities.put(alt1, createEntity("" + alt1, connection));
                    // now the entity must be in the map
                    alt1Entity = entities.get(alt1);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, alt1));
                }
                Entity alt2Entity = entities.get(alt2);
                if (alt2Entity == null) {
                    // this is a new entity, so populate it
                    entities.put(alt2, createEntity("" + alt2, connection));
                    // now the entity must be in the map
                    alt2Entity = entities.get(alt2);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, alt2));
                }
                // create the relationship
                AlternateOf alternateOf = pFactory.newAlternateOf(alt1Entity.getId(), alt2Entity.getId());
                // add the used element into the list of relationships
                relationships.put(entityEntityId, alternateOf);
            }

            l.debug("Exiting addAlternates() with success");
        } catch (SQLException e) {
            l.error("Exiting addAlternates() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }

    }

    protected void addSpecializations(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addSpecializations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_SPECIALIZATIONS_BY_GENERAL_ENTITY_ID);
            stmt.setInt(1, entityID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                int specificId = resultSet.getInt("specific_id");
                int generalId = resultSet.getInt("general_id");

                // check whether the relationship already exists, if yes, don't add it again
                String entityEntityId = getEntityEntityId(specificId, generalId);
                if (relationships.get(entityEntityId) != null) {
                    continue;
                }

                // get entities from list
                Entity specificEntity = entities.get(specificId);
                if (specificEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(specificId, createEntity("" + specificId, connection));
                    // now the entity must be in the map
                    specificEntity = entities.get(specificId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, specificId));
                }
                Entity generalEntity = entities.get(generalId);
                if (generalEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(generalId, createEntity("" + generalId, connection));
                    // now the entity must be in the map
                    generalEntity = entities.get(generalId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, generalId));
                }
                // create the relationship
                SpecializationOf specializationOf = pFactory.newSpecializationOf(specificEntity.getId(),
                        generalEntity.getId());
                // add the used element into the list of relationships
                relationships.put(entityEntityId, specializationOf);
            }

            l.debug("Exiting addSpecializations() with success");
        } catch (SQLException e) {
            l.error("Exiting addSpecializations() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }

    }

    protected void addMemberships(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addMemberships()");

        // check whether the collection already exists, if yes, don't add it again
        String collectionId = QueryConstants.COLLECTION_IDENTIFIER + entityID;
        if (relationships.get(collectionId) != null) {
            return;
        }

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_MEMBERSHIPS_BY_COLLECTION_ID);
            stmt.setInt(1, entityID);
            resultSet = stmt.executeQuery();
            List<QName> members = new ArrayList<QName>();

            while (resultSet.next()) {
                int memberId = resultSet.getInt("member_id");
                // get entity from list
                Entity memberEntity = entities.get(memberId);
                if (memberEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(memberId, createEntity("" + memberId, connection));
                    // now the entity must be in the map
                    memberEntity = entities.get(memberId);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, memberId));
                }
                members.add(memberEntity.getId());
            }

            if (members.size() > 0) {
                // get the collection entity which must already be in the list
                Entity collectionEntity = entities.get(entityID);
                // create the relationship
                HadMember hadMember = pFactory.newHadMember(collectionEntity.getId(), members);
                // add the used element into the list of relationships
                relationships.put(collectionId, hadMember);
            }
            l.debug("Exiting addMemberships() with success");
        } catch (SQLException e) {
            l.error("Exiting addMemberships() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }

    }

    protected void addCommunications(Connection connection,
                                     int activityID) throws SQLException, QueryException {
        assert (connection != null);
        assert (activityID != -1);
        l.debug("Entering addCommunications()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        /**
         * There are 2 possible cases here
         * 1. activity1 generates entity1 and activity2 uses entity1. We have to build this relationship
         *    by looking at generations and usages.
         * 2. activity1 invokes activity2. There should be a separate notification and a relation in the
         *    database to handle this case.
         */

        try {
            // Case 1
            stmt = connection.prepareStatement(PROVSqlQuery.GET_COMMUNICATIONS_BY_ENTITY_BY_INFORMANT_NO_CONTEXT);
            stmt.setInt(1, activityID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                int informantID = resultSet.getInt("gen_id");  // activity by which the entity was generated
                int informedID = resultSet.getInt("used_id");  // activity by which the entity was used

                // check whether the relationship already exists, if yes, don't add it again
                String activityActivityId = getActivityActivityId(informantID, informedID);
                if (relationships.get(activityActivityId) != null) {
                    continue;
                }

                Activity infromantActivity = activities.get(informantID);
                if (infromantActivity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + informantID);
                    // now the activity must be in the map
                    infromantActivity = activities.get(informantID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, informantID));
                }

                Activity infromedActivity = activities.get(informedID);
                if (infromedActivity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + informedID);
                    // now the activity must be in the map
                    infromedActivity = activities.get(informedID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, informedID));
                }
                // create relationship
                WasInformedBy informedBy = pFactory.newWasInformedBy(infromedActivity, infromantActivity);
                // add the informedBy element into the list of relationships
                relationships.put(activityActivityId, informedBy);
            }

            if (stmt != null) {
                stmt.close();
                stmt = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }

            // Case 2
            stmt = connection.prepareStatement(PROVSqlQuery.GET_COMMUNICATIONS_BY_INFORMANT_ACTIVITY_ID);
            stmt.setInt(1, activityID);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String communicationID = resultSet.getString("communication_id");
                int informedID = resultSet.getInt("informed_id");
                int informantID = resultSet.getInt("informant_id");

                // check whether the relationship already exists, if yes, don't add it again
                String activityActivityId = getActivityActivityId(informantID, informedID);
                if (relationships.get(activityActivityId) != null) {
                    continue;
                }

                Activity infromantActivity = activities.get(informantID);
                if (infromantActivity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + informantID);
                    // now the activity must be in the map
                    infromantActivity = activities.get(informantID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, informantID));
                }

                Activity infromedActivity = activities.get(informedID);
                if (infromedActivity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + informedID);
                    // now the activity must be in the map
                    infromedActivity = activities.get(informedID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, informedID));
                }

                WasInformedBy informedBy = pFactory.newWasInformedBy(getIdQName(QueryConstants.COMMUNICATION_IDENTIFIER +
                        communicationID), infromedActivity, infromantActivity);

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_COMMUNICATION_ATTRIBUTES_BY_ID,
                            communicationID, informedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityActivityId, informedBy);
            }
            l.debug("addCommunications() successful");
        } catch (SQLException e) {
            l.error("Exiting addCommunications() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
    }



}
