package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.query.DetailEnumType;
import edu.indiana.d2i.komadu.query.PROVSqlQuery;
import edu.indiana.d2i.komadu.query.QueryConstants;
import edu.indiana.d2i.komadu.query.QueryException;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.openprovenance.prov.model.*;
import org.openprovenance.prov.model.ActedOnBehalfOf;
import org.openprovenance.prov.model.Activity;
import org.openprovenance.prov.model.Agent;
import org.openprovenance.prov.model.AlternateOf;
import org.openprovenance.prov.model.Entity;
import org.openprovenance.prov.model.HadMember;
import org.openprovenance.prov.model.SpecializationOf;
import org.openprovenance.prov.model.Used;
import org.openprovenance.prov.model.WasAssociatedWith;
import org.openprovenance.prov.model.WasAttributedTo;
import org.openprovenance.prov.model.WasDerivedFrom;
import org.openprovenance.prov.model.WasEndedBy;
import org.openprovenance.prov.model.WasGeneratedBy;
import org.openprovenance.prov.model.WasInformedBy;
import org.openprovenance.prov.model.WasInvalidatedBy;
import org.openprovenance.prov.model.WasStartedBy;
import org.openprovenance.prov.xml.*;
import org.w3.www.ns.prov.Document;

import javax.xml.namespace.QName;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;
import java.util.Collection;

/**
 * Here we don't use any context workflow URI to generate the provenance graph. The activity with
 * the given URI will become the root of the graph and we build the graph by collecting nodes and
 * edges according to relationships found through notifications in the Komadu Database.
 */
public abstract class NonContextGraphGenerator extends GraphGenerator {

    private static final Log l = LogFactory.getLog(NonContextGraphGenerator.class);

    // list of <db_activity_id, activity> pairs
    protected HashMap<Integer, Activity> activities;
    // list of <db_entity_id, entity> pairs
    protected HashMap<Integer, Entity> entities;
    // list of <db_agent_id, agent> pairs
    protected HashMap<Integer, Agent> agents;
    // list of relationships
    protected HashMap<String, Statement> relationships;

    // while creating the graph, we have to keep track of unexpanded nodes
    protected Stack<GraphNode> unexpandedNodes;

    // info detail level
    private DetailEnumType.Enum infoDetailLevel;

    protected abstract void populateRoot(Connection connection, String graphURI)
            throws QueryException, SQLException;

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
            } else if (type == GraphNode.NodeType.AGENT) {
                expandAgentNode(connection, node.getInternalID());
            }
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
            l.error("Exiting getProvGraph() with SQL errors", e);
        }
        return provGraph;
    }

    /**
     * Takes the database id of an activity. This method assumes that this particular activity
     * has already been populated. This method only expands it to find out adjacent nodes.
     */
    private void expandActivityNode(Connection connection, int activityID)
            throws QueryException, SQLException {
        // consider associations and find out agents through that
        addAssociations(connection, PROVSqlQuery.GET_ASSOCIATIONS_BY_ACTIVITY_ID, activityID);
        // consider communications and find out related activities
        addCommunications(connection, activityID);
        // find related entities through activity-entity relationships
        addUsages(connection, PROVSqlQuery.GET_USAGES_BY_ACTIVITY_ID, activityID);
        addGenerations(connection, PROVSqlQuery.GET_GENERATIONS_BY_ACTIVITY_ID, activityID);
        addStarts(connection, PROVSqlQuery.GET_STARTS_BY_ACTIVITY_ID, activityID);
        addEnds(connection, PROVSqlQuery.GET_ENDS_BY_ACTIVITY_ID, activityID);
        addInvalidations(connection, PROVSqlQuery.GET_INVALIDATIONS_BY_ACTIVITY_ID, activityID);
    }

    /**
     * Takes the database id of an agent. This method assumes that this particular agent
     * has already been populated. This method only expands it to find out adjacent nodes.
     */
    private void expandAgentNode(Connection connection, int agentID)
            throws QueryException, SQLException {
        // consider associations and find out activities through that
        addAssociations(connection, PROVSqlQuery.GET_ASSOCIATIONS_BY_AGENT_ID, agentID);
        // consider attributions and find out entities through that
        addAttributions(connection, PROVSqlQuery.GET_ATTRIBUTIONS_BY_AGENT_ID, agentID);
        // consider delegations and find out agents through that
        addDelegations(connection, agentID);
    }

    /**
     * Takes the database id of an entity. This method assumes that this particular entity
     * has already been populated. This method only expands it to find out adjacent nodes.
     */
    private void expandEntityNode(Connection connection, int entityID)
            throws QueryException, SQLException {
        // consider attributions and find out agents through that
        addAttributions(connection, PROVSqlQuery.GET_ATTRIBUTIONS_BY_ENTITY_ID, entityID);
        // find related activities through activity-entity relationships
        addUsages(connection, PROVSqlQuery.GET_USAGES_BY_ENTITY_ID, entityID);
        addGenerations(connection, PROVSqlQuery.GET_GENERATIONS_BY_ENTITY_ID, entityID);
        addStarts(connection, PROVSqlQuery.GET_STARTS_BY_ENTITY_ID, entityID);
        addEnds(connection, PROVSqlQuery.GET_ENDS_BY_ENTITY_ID, entityID);
        addInvalidations(connection, PROVSqlQuery.GET_INVALIDATIONS_BY_ENTITY_ID, entityID);
        // find related entities through entity-entity relationships
        addDerivations(connection, entityID);
        addAlternates(connection, entityID);
        addSpecializations(connection, entityID);
        addMemberships(connection, entityID);
    }

    /**
     * Creates a PROV Activity by querying the database using the given query and param.
     * If the query uses the activity URI, param should be activity URI. And if the query uses
     * the activity ID, param should be activity ID.
     */
    protected int createActivity(Connection connection, String query, String param)
            throws QueryException, SQLException {
        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        int activityID = -1;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setString(1, param);
            resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                activityID = resultSet.getInt("activity_id");
                String activityUri = resultSet.getString("activity_uri");
                String activityType = resultSet.getString("activity_type");
                String contextWorkflowUri = resultSet.getString("context_workflow_uri");
                String contextServiceUri = resultSet.getString("context_service_uri");
                String timestep = resultSet.getString("timestep");
//                String location = resultSet.getString("location");     // TODO : Handle location, role
                String contextWfNodeIdToken = resultSet.getString("context_wf_node_id_token");

                // create new prov activity
                Activity activity = pFactory.newActivity(getIdQName(
                        QueryConstants.ACTIVITY_IDENTIFIER + activityID));

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    // activity uri attribute
                    pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("activityUri"),
                            activityUri, Name.QNAME_XSD_STRING));
                    // activity type attribute
                    pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("type"),
                            activityType, Name.QNAME_XSD_STRING));
                    // context WF uri
                    if (contextWorkflowUri != null) {
                        pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("contextWorkflowUri"),
                                contextWorkflowUri, Name.QNAME_XSD_STRING));
                    }
                    // context Service uri
                    if (contextServiceUri != null) {
                        pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("contextServiceUri"),
                                contextServiceUri, Name.QNAME_XSD_STRING));
                    }
                    // timestep
                    if (timestep != null) {
                        pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("timestep"),
                                timestep, Name.QNAME_XSD_STRING));
                    }
                    // node id
                    if (contextWfNodeIdToken != null) {
                        pFactory.addAttribute(activity, pFactory.newOther(getKomaduAttQName("workflowNodeID"),
                                timestep, Name.QNAME_XSD_STRING));
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ACTIVITY_ATTRIBUTES_BY_ID,
                            "" + activityID, activity, connection);
                }
                // add the activity to activity map
                activities.put(activityID, activity);
            }
            l.debug("createActivity() successful");
        } catch (SQLException e) {
            l.error("createActivity() with error");
            l.error(e.toString());
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
        // return id
        return activityID;
    }

    /**
     * Creates an agent using the given query and puts it into the list
     */
    protected int createAgent(Connection connection, String query, String param) throws SQLException {
        assert (connection != null);
        assert (param != null);
        l.debug("Entering createAgent()");
        int agentID = -1;

        PreparedStatement getAgentsStmt = null;
        ResultSet result = null;

        try {
            getAgentsStmt = connection.prepareStatement(query);
            getAgentsStmt.setString(1, param);
            result = getAgentsStmt.executeQuery();

            if (result.next()) {
                agentID = result.getInt("agent_id");
                String uri = result.getString("agent_uri");
                String type = result.getString("agent_type");
                String name = result.getString("name");
                String affiliation = result.getString("affiliation");
                String email = result.getString("email");
                // TODO : Handle role and location later
//                    String role = result.getString("role");
//                    String location = result.getString("location");

                Agent a = newAgent(QueryConstants.AGENT_IDENTIFIER + param, uri, type);
                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add name as an additional attribute
                    if (name != null) {
                        org.openprovenance.prov.xml.Other nameAtt = pFactory.newOther(getKomaduAttQName("name"), name,
                                Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, nameAtt);
                    }
                    // add affiliation as an additional attribute
                    if (affiliation != null) {
                        org.openprovenance.prov.xml.Other affiliationAtt = pFactory.newOther(getKomaduAttQName("affiliation"),
                                affiliation, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, affiliationAtt);
                    }
                    // add email as an additional attribute
                    if (email != null) {
                        org.openprovenance.prov.xml.Other emailAtt = pFactory.newOther(getKomaduAttQName("email"),
                                email, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, emailAtt);
                    }
                }
                // add the new agent into list
                agents.put(agentID, a);
            }

            l.debug("Exiting createAgent() with success");
        } catch (SQLException e) {
            l.error("Exiting createAgent() with errors");
            l.error(e.toString());
        } finally {
            if (getAgentsStmt != null) {
                getAgentsStmt.close();
            }
            if (result != null) {
                result.close();
            }
        }
        return agentID;
    }

    private void addAssociations(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addAssociations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setInt(1, param);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String associationID = resultSet.getString("association_id");
                int activityID = resultSet.getInt("activity_id");
                int agentID = resultSet.getInt("agent_id");
                String planID = resultSet.getString("plan_id");

                // check whether the relationship already exists, if yes, don't add it again
                String activityAgentId = getActivityAgentId(activityID, agentID);
                if (relationships.get(activityAgentId) != null) {
                    continue;
                }

                Activity activity = activities.get(activityID);
                if (activity == null) {
                    // this means, we've found a new activity. so we have to populate
                    // it and add it to unexpanded list
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    activity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }

                Agent agent = agents.get(agentID);
                if (agent == null) {
                    // this means, we've found a new agent. so we have to populate
                    // it and add it to unexpanded list
                    createAgent(connection, PROVSqlQuery.GET_AGENTS_BY_AGENT_ID, "" + agentID);
                    // now the agent must be in the map
                    agent = agents.get(agentID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.AGENT, agentID));
                }
                // create association
                WasAssociatedWith wasAssociatedWith = pFactory.newWasAssociatedWith(
                        getIdQName(QueryConstants.ASSOCIATION_IDENTIFIER + associationID), activity, agent);

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (planID != null) {
                        // TODO : handle plan
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ASSOCIATION_ATTRIBUTES_BY_ID,
                            associationID, wasAssociatedWith, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityAgentId, wasAssociatedWith);
            }
            l.debug("addAssociations() successful");
        } catch (SQLException e) {
            l.error("Exiting addAssociations() with error", e);
        } finally {
            if (stmt != null) {
                stmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
    }

    private void addCommunications(Connection connection,
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_COMMUNICATIONS_BY_ENTITY_NO_CONTEXT);
            stmt.setInt(1, activityID);
            stmt.setInt(2, activityID);
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
                WasInformedBy informedBy = pFactory.newWasInformedBy(infromantActivity, infromedActivity);
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_COMMUNICATIONS_BY_ACTIVITY_ID);
            stmt.setInt(1, activityID);
            stmt.setInt(2, activityID);

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
                        communicationID), infromantActivity, infromedActivity);

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

    private void addUsages(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addUsages()");

        PreparedStatement usedStmt = null;
        ResultSet resultSet = null;

        try {
            usedStmt = connection.prepareStatement(query);
            usedStmt.setInt(1, param);
            resultSet = usedStmt.executeQuery();

            while (resultSet.next()) {
                String usageID = resultSet.getString("usage_id");
                int activityID = resultSet.getInt("activity_id");
                int entityID = resultSet.getInt("entity_id");
                String location = resultSet.getString("location");
                java.sql.Timestamp usedTime = resultSet.getTimestamp("usage_time");

                // check whether the relationship already exists, if yes, don't add it again
                String activityEntityId = getActivityEntityId(activityID, entityID);
                if (relationships.get(activityEntityId) != null) {
                    continue;
                }

                Activity usedActivity = activities.get(activityID);
                if (usedActivity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    usedActivity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }
                Entity usedEntity = entities.get(entityID);
                if (usedEntity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    usedEntity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }
                Used used = pFactory.newUsed(getIdQName(QueryConstants.USAGE_IDENTIFIER + usageID),
                        usedActivity.getId(), usedEntity.getId());

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        used.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        org.openprovenance.prov.xml.Other timeAtt = pFactory.newOther(getKomaduAttQName("used-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(used, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_USAGE_ATTRIBUTES_BY_ID,
                            usageID, used, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityEntityId, used);
            }
            l.debug("addUsages() successful");
        } catch (SQLException e) {
            l.error("Exiting addUsages() with error");
            l.error(e.toString());
        } finally {
            if (usedStmt != null) {
                usedStmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
    }

    private void addGenerations(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addGenerations()");

        PreparedStatement generatedStmt = null;
        ResultSet resultSet = null;

        try {
            generatedStmt = connection.prepareStatement(query);
            generatedStmt.setInt(1, param);
            resultSet = generatedStmt.executeQuery();

            while (resultSet.next()) {
                String genID = resultSet.getString("generation_id");
                int activityID = resultSet.getInt("activity_id");
                int entityID = resultSet.getInt("entity_id");
                String location = resultSet.getString("location");
                java.sql.Timestamp usedTime = resultSet.getTimestamp("generation_time");

                // check whether the relationship already exists, if yes, don't add it again
                String activityEntityId = getActivityEntityId(activityID, entityID);
                if (relationships.get(activityEntityId) != null) {
                    continue;
                }

                Activity activity = activities.get(activityID);
                if (activity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    activity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }
                Entity entity = entities.get(entityID);
                if (entity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    entity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }
                WasGeneratedBy wasGeneratedBy = pFactory.newWasGeneratedBy(
                        getIdQName(QueryConstants.GENERATION_IDENTIFIER + genID),
                        entity.getId(), activity.getId());

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasGeneratedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        org.openprovenance.prov.xml.Other timeAtt = pFactory.newOther(getKomaduAttQName("generation-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasGeneratedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_GENERATION_ATTRIBUTES_BY_ID,
                            genID, wasGeneratedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityEntityId, wasGeneratedBy);
            }
            l.debug("addGenerations() successful");
        } catch (SQLException e) {
            l.error("Exiting addGenerations() with error");
            l.error(e.toString());
        } finally {
            if (generatedStmt != null) {
                generatedStmt.close();
            }
            if (resultSet != null) {
                resultSet.close();
            }
        }
    }

    private void addStarts(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addStarts()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setInt(1, param);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String startID = resultSet.getString("start_id");
                int activityID = resultSet.getInt("activity_id");
                int entityID = resultSet.getInt("trigger_id");
                String location = resultSet.getString("location");
                java.sql.Timestamp startTime = resultSet.getTimestamp("start_time");

                // check whether the relationship already exists, if yes, don't add it again
                String activityEntityId = getActivityEntityId(activityID, entityID);
                if (relationships.get(activityEntityId) != null) {
                    continue;
                }

                Activity activity = activities.get(activityID);
                if (activity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    activity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }
                Entity entity = entities.get(entityID);
                if (entity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    entity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }
                WasStartedBy wasStartedBy = pFactory.newWasStartedBy(
                        getIdQName(QueryConstants.START_IDENTIFIER + startID),
                        activity.getId(), entity.getId(), null);     // TODO : check starter

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasStartedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (startTime != null) {
                        org.openprovenance.prov.xml.Other timeAtt = pFactory.newOther(getKomaduAttQName("start-time"),
                                startTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasStartedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_START_ATTRIBUTES_BY_ID,
                            startID, wasStartedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityEntityId, wasStartedBy);
            }
            l.debug("addStarts() successful");
        } catch (SQLException e) {
            l.error("Exiting addStarts() with error");
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

    private void addEnds(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addEnds()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setInt(1, param);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String endID = resultSet.getString("end_id");
                int activityID = resultSet.getInt("activity_id");
                int entityID = resultSet.getInt("trigger_id");
                String location = resultSet.getString("location");
                java.sql.Timestamp endTime = resultSet.getTimestamp("end_time");

                // check whether the relationship already exists, if yes, don't add it again
                String activityEntityId = getActivityEntityId(activityID, entityID);
                if (relationships.get(activityEntityId) != null) {
                    continue;
                }

                Activity activity = activities.get(activityID);
                if (activity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    activity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }
                Entity entity = entities.get(entityID);
                if (entity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    entity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }
                WasEndedBy wasEndedBy = pFactory.newWasEndedBy(
                        getIdQName(QueryConstants.END_IDENTIFIER + endID),
                        activity.getId(), entity.getId(), null);     // TODO : check ender

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasEndedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (endTime != null) {
                        org.openprovenance.prov.xml.Other timeAtt = pFactory.newOther(getKomaduAttQName("end-time"),
                                endTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasEndedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_END_ATTRIBUTES_BY_ID,
                            endID, wasEndedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityEntityId, wasEndedBy);
            }
            l.debug("addEnds() successful");
        } catch (SQLException e) {
            l.error("Exiting addEnds() with error");
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

    private void addInvalidations(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addInvalidations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setInt(1, param);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String invalidationID = resultSet.getString("invalidation_id");
                int activityID = resultSet.getInt("activity_id");
                int entityID = resultSet.getInt("entity_id");
                String location = resultSet.getString("location");
                java.sql.Timestamp usedTime = resultSet.getTimestamp("invalidation_time");

                // check whether the relationship already exists, if yes, don't add it again
                String activityEntityId = getActivityEntityId(activityID, entityID);
                if (relationships.get(activityEntityId) != null) {
                    continue;
                }

                Activity activity = activities.get(activityID);
                if (activity == null) {
                    // this is a new activity, so populate it
                    createActivity(connection, PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID, "" + activityID);
                    // now the activity must be in the map
                    activity = activities.get(activityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, activityID));
                }
                Entity entity = entities.get(entityID);
                if (entity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    entity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }
                WasInvalidatedBy wasInvalidatedBy = pFactory.newWasInvalidatedBy(
                        getIdQName(QueryConstants.INVALIDATION_IDENTIFIER + invalidationID),
                        entity.getId(), activity.getId());

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasInvalidatedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        org.openprovenance.prov.xml.Other timeAtt = pFactory.newOther(getKomaduAttQName("invalidation-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasInvalidatedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_INVALIDATION_ATTRIBUTES_BY_ID,
                            invalidationID, wasInvalidatedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.put(activityEntityId, wasInvalidatedBy);
            }
            l.debug("addInvalidations() successful");
        } catch (SQLException e) {
            l.error("Exiting addInvalidations() with error");
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

    private void addAttributions(Connection connection, String query, int param)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (query != null);
        assert (param != -1);
        l.debug("Entering addAttributions()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(query);
            stmt.setInt(1, param);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String attributionID = resultSet.getString("attribution_id");
                int agentID = resultSet.getInt("agent_id");
                int entityID = resultSet.getInt("entity_id");

                // check whether the relationship already exists, if yes, don't add it again
                String agentEntityID = getEntityAgentId(entityID, agentID);
                if (relationships.get(agentEntityID) != null) {
                    continue;
                }

                Agent agent = agents.get(agentID);
                if (agent == null) {
                    // this means, we've found a new agent. so we have to populate
                    // it and add it to unexpanded list
                    createAgent(connection, PROVSqlQuery.GET_AGENTS_BY_AGENT_ID, "" + agentID);
                    // now the agent must be in the map
                    agent = agents.get(agentID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.AGENT, agentID));
                }
                Entity entity = entities.get(entityID);
                if (entity == null) {
                    // this is a new entity, so populate it
                    entities.put(entityID, createEntity("" + entityID, connection));
                    // now the entity must be in the map
                    entity = entities.get(entityID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ENTITY, entityID));
                }

                WasAttributedTo wasAttributedTo = pFactory.newWasAttributedTo(
                        getIdQName(QueryConstants.ATTRIBUTION_IDENTIFIER + attributionID),
                        entity.getId(), agent.getId(), new ArrayList<Attribute>());

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ATTRIBUTION_ATTRIBUTES_BY_ID,
                            attributionID, wasAttributedTo, connection);
                }
                // add the used element into the list of relationships
                relationships.put(agentEntityID, wasAttributedTo);
            }
            l.debug("addAttributions() successful");
        } catch (SQLException e) {
            l.error("Exiting addAttributions() with error");
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

    private void addDelegations(Connection connection, int agentID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (agentID != -1);
        l.debug("Entering addDelegations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_DELEGATIONS_BY_AGENT_ID);
            stmt.setInt(1, agentID);
            stmt.setInt(2, agentID);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String delegationID = resultSet.getString("delegation_id");
                int delAgentID = resultSet.getInt("del_agent_id");
                int resAgentID = resultSet.getInt("res_agent_id");
                int activityID = resultSet.getInt("activity_id"); // TODO : handle this

                // check whether the relationship already exists, if yes, don't add it again
                String agentAgentId = getAgentAgentId(delAgentID, resAgentID);
                if (relationships.get(agentAgentId) != null) {
                    continue;
                }

                Agent delAgent = agents.get(delAgentID);
                if (delAgent == null) {
                    // this means, we've found a new agent. so we have to populate
                    // it and add it to unexpanded list
                    createAgent(connection, PROVSqlQuery.GET_AGENTS_BY_AGENT_ID, "" + delAgentID);
                    // now the agent must be in the map
                    delAgent = agents.get(delAgentID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.AGENT, delAgentID));
                }
                Agent resAgent = agents.get(resAgentID);
                if (resAgent == null) {
                    // this means, we've found a new agent. so we have to populate
                    // it and add it to unexpanded list
                    createAgent(connection, PROVSqlQuery.GET_AGENTS_BY_AGENT_ID, "" + resAgentID);
                    // now the agent must be in the map
                    resAgent = agents.get(resAgentID);
                    unexpandedNodes.push(new GraphNode(GraphNode.NodeType.AGENT, resAgentID));
                }

                ActedOnBehalfOf behalfOf = pFactory.newActedOnBehalfOf(
                        getIdQName(QueryConstants.DELEGATION_IDENTIFIER + delegationID),
                        delAgent.getId(), resAgent.getId());

                if (infoDetailLevel != null && infoDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DELEGATION_ATTRIBUTES_BY_ID,
                            delegationID, behalfOf, connection);
                }
                // add the used element into the list of relationships
                relationships.put(agentAgentId, behalfOf);
            }
            l.debug("addDelegations() successful");
        } catch (SQLException e) {
            l.error("Exiting addDelegations() with error");
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

    private void addDerivations(Connection connection, int entityID)
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_DERIVATIONS_BY_ENTITY_ID);
            stmt.setInt(1, entityID);
            stmt.setInt(2, entityID);

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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_DERIVATIONS_BY_ACTIVITY_NO_CONTEXT);
            stmt.setInt(1, entityID);
            stmt.setInt(2, entityID);
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

    private void addAlternates(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addAlternates()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_ALTERNATES_BY_ENTITY_ID);
            stmt.setInt(1, entityID);
            stmt.setInt(2, entityID);
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

    private void addSpecializations(Connection connection, int entityID)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entityID != -1);
        l.debug("Entering addSpecializations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_SPECIALIZATIONS_BY_ENTITY_ID);
            stmt.setInt(1, entityID);
            stmt.setInt(2, entityID);
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

    private void addMemberships(Connection connection, int entityID)
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

    /**
     * These util methods create unique identifiers for relationships that we create
     */
    private String getActivityAgentId(int activityID, int agentID) {
        return QueryConstants.ACTIVITY_IDENTIFIER + activityID + "_" +
                QueryConstants.AGENT_IDENTIFIER + agentID;
    }

    private String getActivityEntityId(int activityID, int entityID) {
        return QueryConstants.ACTIVITY_IDENTIFIER + activityID + "_" +
                QueryConstants.ENTITY_IDENTIFIER + entityID;
    }

    private String getEntityAgentId(int entityID, int agentID) {
        return QueryConstants.ENTITY_IDENTIFIER + entityID + "_" +
                QueryConstants.AGENT_IDENTIFIER + agentID;
    }

    private String getActivityActivityId(int activity1ID, int activity2ID) {
        return getSameElementId(activity1ID, activity2ID, QueryConstants.ACTIVITY_IDENTIFIER);
    }

    private String getAgentAgentId(int agent1ID, int agent2ID) {
        return getSameElementId(agent1ID, agent2ID, QueryConstants.AGENT_IDENTIFIER);
    }

    private String getEntityEntityId(int entity1ID, int entity2ID) {
        return  getSameElementId(entity1ID, entity2ID, QueryConstants.ENTITY_IDENTIFIER);
    }

    /**
     * Generates an id for 2 same kind elements. Here we use an important convention where
     * always the lesser id will be added first. This is because we use the created id to check
     * duplicates.
     */
    private String getSameElementId(int id1, int id2, String prefix) {
        int elem1, elem2;
        if (id1 <= id2) {
            elem1 = id1;
            elem2 = id2;
        } else {
            elem1 = id2;
            elem2 = id1;
        }
        return prefix + elem1 + "_" + prefix + elem2;
    }

}
