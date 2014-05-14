package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.ingest.db.BaseDBIngesterImplementer;
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
import org.openprovenance.prov.model.Statement;
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
import org.openprovenance.prov.xml.Other;
import org.w3.www.ns.prov.Document;

import javax.xml.namespace.QName;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.sql.*;
import java.util.*;
import java.util.Collection;

public class ContextGraphGenerator extends GraphGenerator {

    private static final Log l = LogFactory.getLog(ContextGraphGenerator.class);

    /**
     * Computes the PROV graph using the given workflow uri
     */
    protected Document computeProvGraph(Connection connection,
                                        String contextWorkflowURI,
                                        DetailEnumType.Enum informationDetailLevel)
            throws QueryException, SQLException {

        Document provGraph = null;
        // first we find out all activities, entities and agents
        HashMap<String, Activity> activities = getActivities(connection,
                contextWorkflowURI, informationDetailLevel);
        HashMap<String, Entity> entities = getEntities(connection, contextWorkflowURI);
        HashMap<String, Agent> agents = getAgents(connection, contextWorkflowURI, informationDetailLevel);

        Collection<Activity> activityValues = activities.values();
        Collection<Entity> entityValues = entities.values();
        Collection<Agent> agentValues = agents.values();

        // list of relationships
        List<Statement> relationships = new ArrayList<Statement>();
        // adding different kinds of relationships
        // activity-entity relationships
        addUsages(connection, activities, entities, relationships, contextWorkflowURI, informationDetailLevel);
        addGenerations(connection, activities, entities, relationships, contextWorkflowURI, informationDetailLevel);
        addStarts(connection, activities, entities, relationships, contextWorkflowURI, informationDetailLevel);
        addEnds(connection, activities, entities, relationships, contextWorkflowURI, informationDetailLevel);
        addInvalidations(connection, activities, entities, relationships, contextWorkflowURI, informationDetailLevel);
        // agent-activity relationships
        addAssociations(connection, activities, agents, relationships, contextWorkflowURI, informationDetailLevel);
        // agent-entity relationships
        addAttributions(connection, agents, entities, relationships, contextWorkflowURI, informationDetailLevel);
        // agent-agent relationships
        addDelegations(connection, agents, relationships, contextWorkflowURI, informationDetailLevel);
        // activity-activity relationships
        addCommunications(connection, activities, relationships, contextWorkflowURI, informationDetailLevel);
        // entity-entity relationships
        addDerivations(connection, entities, relationships, contextWorkflowURI, informationDetailLevel);
        addAlternates(connection, entities, relationships);
        addSpecializations(connection, entities, relationships);
        addMemberships(connection, entities, relationships);

        // create the PROV graph using prov-toolbox library's api
        org.openprovenance.prov.model.Document graph = pFactory.newDocument(
                activityValues.toArray(new Activity[activityValues.size()]),
                entityValues.toArray(new Entity[entityValues.size()]),
                agentValues.toArray(new Agent[agentValues.size()]),
                relationships.toArray(new Statement[relationships.size()]));
        graph.setNamespace(Namespace.gatherNamespaces(graph));
        /*
         * Now we have to serialize the created graph and parse it to the Xmlbean type that
         * we want to return
         */
        ProvSerialiser serializer = ProvSerialiser.getThreadProvSerialiser();
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


    private HashMap<String, Activity> getActivities(Connection connection,
                                                   String contextWorkflowURI,
                                                   DetailEnumType.Enum informationDetailLevel) throws SQLException {

        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering getActivities()");

        HashMap<String, Activity> activities = new HashMap<String, Activity>();
        PreparedStatement getActivitiesStmt = null;
        PreparedStatement getRegActivitiesStmt = null;
        ResultSet actResult = null;
        ResultSet regActResult = null;
        HashMap<String, String> visitedRegEntity = new HashMap<String, String>();

        try {
            getActivitiesStmt = connection
                    .prepareStatement(PROVSqlQuery.GET_ACTIVITIES_BY_CONTEXT_WORKFLOW_URI);
            getActivitiesStmt.setString(1, contextWorkflowURI);
            getActivitiesStmt.setString(2, contextWorkflowURI);

            actResult = getActivitiesStmt.executeQuery();
            // loop through all activities and create corresponding Activity elements
            while (actResult.next()) {
                int timestep;
                String activityType = actResult.getString("activity_type");
                int instanceOfID = actResult.getInt("instance_of");

                /* create the activity ID */
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + actResult.getInt("activity_id");
                // create new prov activity
                Activity activity = pFactory.newActivity(getIdQName(activityID));
                // add current activity into the list
                activities.put(activityID, activity);

                if (informationDetailLevel != null && informationDetailLevel
                        .equals(DetailEnumType.FINE)) {

                    // add activity type attribute. note that this is not the prov:type
                    Other typeAtt = pFactory.newOther(getKomaduAttQName("type"),
                            activityType, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(activity, typeAtt);

                    if (activityType.equals(BaseDBIngesterImplementer.ActivityTypeEnum.WORKFLOW.toString())) {
                        String workflowID = actResult.getString("activity_uri");
                        // add workflow ID as a Komadu Attribute
                        Other workflowIDAtt = pFactory.newOther(getKomaduAttQName("workflowID"),
                                workflowID, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(activity, workflowIDAtt);
                    } else if (activityType.equals(BaseDBIngesterImplementer.ActivityTypeEnum.SERVICE.toString())
                            || activityType.equals(BaseDBIngesterImplementer.ActivityTypeEnum.METHOD.toString())) {
                        String workflowID = actResult.getString("context_workflow_uri");
                        String serviceID = actResult.getString("activity_uri");
                        String workflowNodeID = actResult.getString("context_wf_node_id_token");
                        timestep = actResult.getInt("timestep");

                        Other workflowIDAtt = pFactory.newOther(getKomaduAttQName("workflowID"),
                                workflowID, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(activity, workflowIDAtt);

                        Other workflowNodeIdAtt = pFactory.newOther(getKomaduAttQName("workflowNodeID"),
                                workflowNodeID, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(activity, workflowNodeIdAtt);

                        Other timestepAtt = pFactory.newOther(getKomaduAttQName("timestep"),
                                timestep, Name.QNAME_XSD_INT);
                        pFactory.addAttribute(activity, timestepAtt);

                        if (activityType.equals(BaseDBIngesterImplementer.ActivityTypeEnum.METHOD.toString())) {
                            serviceID = actResult.getString("context_service_uri");
                            String methodID = actResult.getString("activity_uri");
                            Other methodIDAtt = pFactory.newOther(getKomaduAttQName("methodID"),
                                    methodID, Name.QNAME_XSD_STRING);
                            pFactory.addAttribute(activity, methodIDAtt);
                        }

                        Other serviceIDAtt = pFactory.newOther(getKomaduAttQName("serviceID"),
                                serviceID, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(activity, serviceIDAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ACTIVITY_ATTRIBUTES_BY_ID,
                            activityID, activity, connection);
                }

                if (instanceOfID > 0) {
                    if (visitedRegEntity.get(QueryConstants.REG_ACTIVITY_IDENTIFIER + instanceOfID) == null) {

                        visitedRegEntity.put(QueryConstants.REG_ACTIVITY_IDENTIFIER + instanceOfID,
                                QueryConstants.REG_ACTIVITY_IDENTIFIER + instanceOfID);

                        getRegActivitiesStmt = connection
                                .prepareStatement(PROVSqlQuery.GET_REG_ACTIVITIES_BY_ID);
                        getRegActivitiesStmt.setString(1, instanceOfID + "");

                        regActResult = getRegActivitiesStmt.executeQuery();

                        while (regActResult.next()) {
                            /* create the activity ID */
                            activityID = QueryConstants.REG_ACTIVITY_IDENTIFIER + instanceOfID;
                            // create new prov activity
                            Activity regActivity = pFactory.newActivity(getIdQName(activityID));
                            // add current activity into the list
                            activities.put(activityID, regActivity);

                            if (informationDetailLevel != null && informationDetailLevel
                                    .equals(DetailEnumType.FINE)) {
                                String regActivityType = regActResult.getString("activity_type");
                                String regActivityName = regActResult.getString("activity_uri");
                                String regActivityVersion = regActResult.getString("version");
                                String regActivityCreationTime = regActResult.getString("creation_time");

                                Other activityTypeAtt = pFactory.newOther(getKomaduAttQName("type"),
                                        regActivityType, Name.QNAME_XSD_STRING);
                                pFactory.addAttribute(regActivity, activityTypeAtt);

                                Other activityNameAtt = pFactory.newOther(getKomaduAttQName("name"),
                                        regActivityName, Name.QNAME_XSD_STRING);
                                pFactory.addAttribute(regActivity, activityNameAtt);

                                Other activityVersionAtt = pFactory.newOther(getKomaduAttQName("version"),
                                        regActivityVersion, Name.QNAME_XSD_STRING);
                                pFactory.addAttribute(regActivity, activityVersionAtt);

                                Other activityTimeAtt = pFactory.newOther(getKomaduAttQName("creationTime"),
                                        regActivityCreationTime, Name.QNAME_XSD_STRING);
                                pFactory.addAttribute(regActivity, activityTimeAtt);

                                // TODO : Add reg_activity_attributes
                            }
                        }
                    }
                }
            }

            l.debug("Exiting getActivities()");
            return activities;
        } catch (SQLException e) {
            l.error("Exiting getActivities() with errors", e);
            // return an empty array
            return new HashMap<String, Activity>();
        } finally {
            if (actResult != null) {
                actResult.close();
            }

            if (regActResult != null) {
                regActResult.close();
            }

            if (getActivitiesStmt != null) {
                getActivitiesStmt.close();
            }

            if (getRegActivitiesStmt != null) {
                getRegActivitiesStmt.close();
            }
        }
    }

    private HashMap<String, Entity> getEntities(Connection connection,
                                String contextWorkflowURI) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering getEntities()");
        /*
         * There may be some data products that may be both produced and
         * consumed hence keep a list of urls which are already added
         */
        ArrayList<String> uris = new ArrayList<String>();
        // a list of entities created
        HashMap<String, Entity> provEntities = new HashMap<String, Entity>();

        PreparedStatement getDataObjectStmt = null;
        ResultSet res = null;

        try {
            /* get all the files that were produced */
            getDataObjectStmt = connection.prepareStatement(PROVSqlQuery.GET_DATA_FILES_GENERATED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);
            res = getDataObjectStmt.executeQuery();
            while (res.next()) {
                String fileURI = res.getString(1);
                String size = res.getString(2);
                String fileID = res.getString(3);
                // add the current entity if it is not already considered
                if (!uris.contains(fileURI)) {
                    Entity e = newEntity(QueryConstants.FILE_IDENTIFIER + fileID,
                            fileURI, QueryConstants.ENTITY_FILE);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, sizeAtt);
                    provEntities.put(fileID, e);
                    uris.add(fileURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }

            /* get all the blocks that were produced */
            getDataObjectStmt = connection.prepareStatement(PROVSqlQuery.GET_DATA_BLOCKS_GENERATED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);
            res = getDataObjectStmt.executeQuery();
            while (res.next()) {
                String blockID = res.getString(1);
                String blockURI = res.getString(2);
                String blockSize = res.getString(3);
                String blockContent = res.getString(4);

                if (!uris.contains(blockURI)) {
                    Entity e = newEntity(QueryConstants.BLOCK_IDENTIFIER + blockID,
                            blockURI, QueryConstants.ENTITY_BLOCK);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"),
                            blockSize, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, sizeAtt);
                    // add block content as an additional attribute
                    Other contentAtt = pFactory.newOther(getKomaduAttQName("content"),
                            blockContent, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, contentAtt);
                    provEntities.put(blockID, e);
                    uris.add(blockURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }

            getDataObjectStmt = connection
                    .prepareStatement(PROVSqlQuery.GET_DATA_COLLECTIONS_GENERATED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);
            res = getDataObjectStmt.executeQuery();
            while (res.next()) {
                String collectionID = res.getString(1);
                String collectionURI = res.getString(2);

                if (!uris.contains(collectionURI)) {
                    Entity e = newEntity(QueryConstants.COLLECTION_IDENTIFIER + collectionID,
                            collectionURI, QueryConstants.ENTITY_COLLECTION);
                    provEntities.put(collectionID, e);
                    uris.add(collectionURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }

            // TODO : Read Generic Entity

            /* get all the files that were consumed */
            getDataObjectStmt = connection.prepareStatement(PROVSqlQuery.GET_DATA_FILES_USED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);
            res = getDataObjectStmt.executeQuery();
            while (res.next()) {
                String fileURI = res.getString(1);
                String size = res.getString(2);
                String fileID = res.getString(3);
                // add the current entity if it is not already considered
                if (!uris.contains(fileURI)) {
                    Entity e = newEntity(QueryConstants.FILE_IDENTIFIER + fileID,
                            fileURI, QueryConstants.ENTITY_FILE);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"), size, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, sizeAtt);
                    provEntities.put(fileID, e);
                    uris.add(fileURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }

            /* get all the blocks that were consumed */
            getDataObjectStmt = connection.prepareStatement(PROVSqlQuery.GET_DATA_BLOCKS_USED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);
            res = getDataObjectStmt.executeQuery();

            while (res.next()) {
                String blockID = res.getString(1);
                String blockURI = res.getString(2);
                String blockSize = res.getString(3);
                String blockContent = res.getString(4);

                if (!uris.contains(blockURI)) {
                    Entity e = newEntity(QueryConstants.BLOCK_IDENTIFIER + blockID,
                            blockURI, QueryConstants.ENTITY_BLOCK);
                    // add size as an additional attribute
                    Other sizeAtt = pFactory.newOther(getKomaduAttQName("size"),
                            blockSize, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, sizeAtt);
                    // add block content as an additional attribute
                    Other contentAtt = pFactory.newOther(getKomaduAttQName("content"),
                            blockContent, Name.QNAME_XSD_STRING);
                    pFactory.addAttribute(e, contentAtt);
                    provEntities.put(blockID, e);
                    uris.add(blockURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }

            getDataObjectStmt = connection
                    .prepareStatement(PROVSqlQuery.GET_DATA_COLLECTIONS_USED);
            getDataObjectStmt.setString(1, contextWorkflowURI);
            getDataObjectStmt.setString(2, contextWorkflowURI);

            res = getDataObjectStmt.executeQuery();
            while (res.next()) {
                String collectionID = res.getString(1);
                String collectionURI = res.getString(2);
                if (!uris.contains(collectionURI)) {
                    Entity e = newEntity(QueryConstants.COLLECTION_IDENTIFIER + collectionID,
                            collectionURI, QueryConstants.ENTITY_COLLECTION);
                    provEntities.put(collectionID, e);
                    uris.add(collectionURI);
                }
            }

            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
                getDataObjectStmt = null;
            }

            if (res != null) {
                res.close();
                res = null;
            }
            // TODO : Here we only have considered usages and generations to find activities
            // TODO : But we have to consider start, end and invalidation too
            l.debug("Exiting getEntities() with success");
            // convert the list into an array and return
            return provEntities;
        } catch (SQLException e) {
            l.error("Exiting getEntities() with errors");
            l.error(e.toString());
            return new HashMap<String, Entity>();
        } finally {
            if (getDataObjectStmt != null) {
                getDataObjectStmt.close();
            }
            if (res != null) {
                res.close();
            }
        }
    }

    private HashMap<String, Agent> getAgents(Connection connection,
                                            String contextWorkflowURI,
                                            DetailEnumType.Enum informationDetailLevel) throws SQLException {

        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering getAgents()");

        HashMap<String, Agent> agents = new HashMap<String, Agent>();
        PreparedStatement getAgentsStmt = null;
        ResultSet result = null;

        try {
            if (informationDetailLevel != null && informationDetailLevel
                    .equals(DetailEnumType.FINE)) {
                getAgentsStmt = connection
                        .prepareStatement(PROVSqlQuery.GET_AGENTS_BY_ACTIVITY_URI);
                getAgentsStmt.setString(1, contextWorkflowURI);
                getAgentsStmt.setString(2, contextWorkflowURI);
                result = getAgentsStmt.executeQuery();

                while (result.next()) {
                    String id = result.getString("agent_id");
                    String uri = result.getString("agent_uri");
                    String type = result.getString("agent_type");
                    String name = result.getString("name");
                    String affiliation = result.getString("affiliation");
                    String email = result.getString("email");
                    // TODO : Handle role and location later
                    String role = result.getString("role");
                    String location = result.getString("location");

                    Agent a = newAgent(QueryConstants.AGENT_IDENTIFIER + id, uri, type);
                    // add name as an additional attribute
                    if (name != null) {
                        Other nameAtt = pFactory.newOther(getKomaduAttQName("name"), name,
                                Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, nameAtt);
                    }
                    // add affiliation as an additional attribute
                    if (affiliation != null) {
                        Other affiliationAtt = pFactory.newOther(getKomaduAttQName("affiliation"),
                                affiliation, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, affiliationAtt);
                    }
                    // add email as an additional attribute
                    if (email != null) {
                        Other emailAtt = pFactory.newOther(getKomaduAttQName("email"),
                                email, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(a, emailAtt);
                    }
                    // add the new agent into list
                    agents.put(QueryConstants.AGENT_IDENTIFIER + id, a);
                    // TODO : Add other kinds of Agents if any
                }
            }
            l.debug("Exiting getOPMAgents() with success");
            // convert the list of agents to an array and return
            return agents;
        } catch (SQLException e) {
            l.error("Exiting getOPMAgents() with errors");
            l.error(e.toString());
            return null;
        } finally {
            if (getAgentsStmt != null) {
                getAgentsStmt.close();
            }
            if (result != null) {
                result.close();
            }
        }
    }

    private void addUsages(Connection connection,
                          HashMap<String, Activity> activities,
                          HashMap<String, Entity> entities,
                          List<Statement> relationships,
                          String contextWorkflowURI,
                          DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addUsages()");

        PreparedStatement usedStmt = null;
        ResultSet resultSet = null;

        try {
            usedStmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_USAGES);
            usedStmt.setString(1, contextWorkflowURI);
            usedStmt.setString(2, contextWorkflowURI);

            resultSet = usedStmt.executeQuery();

            while (resultSet.next()) {
                String usageID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String entityID = resultSet.getString(3);
                String location = resultSet.getString(4);
                java.sql.Timestamp usedTime = resultSet.getTimestamp(5);

                Activity usedActivity = activities.get(activityID);
                Entity usedEntity = entities.get(entityID);
                Used used = pFactory.newUsed(getIdQName(usageID), usedActivity.getId(), usedEntity.getId());

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        used.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        Other timeAtt = pFactory.newOther(getKomaduAttQName("used-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(used, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_USAGE_ATTRIBUTES_BY_ID,
                            usageID, used, connection);
                }
                // add the used element into the list of relationships
                relationships.add(used);
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

    private void addGenerations(Connection connection,
                               HashMap<String, Activity> activities,
                               HashMap<String, Entity> entities,
                               List<Statement> relationships,
                               String contextWorkflowURI,
                               DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addGenerations()");

        PreparedStatement generatedStmt = null;
        ResultSet resultSet = null;

        try {
            generatedStmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_GENERATIONS);
            generatedStmt.setString(1, contextWorkflowURI);
            generatedStmt.setString(2, contextWorkflowURI);

            resultSet = generatedStmt.executeQuery();

            while (resultSet.next()) {
                String genID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String entityID = resultSet.getString(3);
                String location = resultSet.getString(4);
                java.sql.Timestamp usedTime = resultSet.getTimestamp(5);

                Activity activity = activities.get(activityID);
                Entity entity = entities.get(entityID);
                if (activity == null || entity == null) {
                    l.error("Activity or Entity is null. Inconsistent WasGeneratedBy relationship..");
                    return;
                }
                WasGeneratedBy wasGeneratedBy = pFactory.newWasGeneratedBy(getIdQName(genID),
                        entity.getId(), activity.getId());

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasGeneratedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        Other timeAtt = pFactory.newOther(getKomaduAttQName("generation-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasGeneratedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_GENERATION_ATTRIBUTES_BY_ID,
                            genID, wasGeneratedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasGeneratedBy);
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

    private void addStarts(Connection connection,
                          HashMap<String, Activity> activities,
                          HashMap<String, Entity> entities,
                          List<Statement> relationships,
                          String contextWorkflowURI,
                          DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addStarts()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_STARTS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String startID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String entityID = resultSet.getString(3);
                String location = resultSet.getString(4);
                java.sql.Timestamp usedTime = resultSet.getTimestamp(5);

                Activity activity = activities.get(activityID);
                Entity entity = entities.get(entityID);
                if (activity == null || entity == null) {
                    l.error("Activity or Entity is null. Inconsistent WasStartedBy relationship..");
                    return;
                }
                WasStartedBy wasStartedBy = pFactory.newWasStartedBy(getIdQName(startID),
                        activity.getId(), entity.getId(), null);     // TODO : check starter

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasStartedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        Other timeAtt = pFactory.newOther(getKomaduAttQName("start-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasStartedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_START_ATTRIBUTES_BY_ID,
                            startID, wasStartedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasStartedBy);
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

    private void addEnds(Connection connection,
                        HashMap<String, Activity> activities,
                        HashMap<String, Entity> entities,
                        List<Statement> relationships,
                        String contextWorkflowURI,
                        DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addEnds()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_ENDS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String endID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String entityID = resultSet.getString(3);
                String location = resultSet.getString(4);
                java.sql.Timestamp endTime = resultSet.getTimestamp(5);

                Activity activity = activities.get(activityID);
                Entity entity = entities.get(entityID);
                if (activity == null || entity == null) {
                    l.error("Activity or Entity is null. Inconsistent WasEndedBy relationship..");
                    return;
                }
                WasEndedBy wasEndedBy = pFactory.newWasEndedBy(getIdQName(endID),
                        activity.getId(), entity.getId(), null);     // TODO : check starter

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasEndedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (endTime != null) {
                        Other timeAtt = pFactory.newOther(getKomaduAttQName("end-time"),
                                endTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasEndedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_END_ATTRIBUTES_BY_ID,
                            endID, wasEndedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasEndedBy);
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

    private void addInvalidations(Connection connection,
                                 HashMap<String, Activity> activities,
                                 HashMap<String, Entity> entities,
                                 List<Statement> relationships,
                                 String contextWorkflowURI,
                                 DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addInvalidations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_INVALIDATIONS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String invalidationID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String entityID = resultSet.getString(3);
                String location = resultSet.getString(4);
                java.sql.Timestamp usedTime = resultSet.getTimestamp(5);

                Activity activity = activities.get(activityID);
                Entity entity = entities.get(entityID);
                if (activity == null || entity == null) {
                    l.error("Activity or Entity is null. Inconsistent WasInvalidatedBy relationship..");
                    return;
                }
                WasInvalidatedBy wasInvalidatedBy = pFactory.newWasInvalidatedBy(getIdQName(invalidationID),
                        entity.getId(), activity.getId());     // TODO : check starter

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (location != null) {
                        wasInvalidatedBy.getLocation().add(pFactory.newLocation(location, Name.QNAME_XSD_STRING));
                        // TODO : check Role
                    }
                    if (usedTime != null) {
                        Other timeAtt = pFactory.newOther(getKomaduAttQName("invalidation-time"),
                                usedTime, Name.QNAME_XSD_DATETIME);
                        pFactory.addAttribute(wasInvalidatedBy, timeAtt);
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_INVALIDATION_ATTRIBUTES_BY_ID,
                            invalidationID, wasInvalidatedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasInvalidatedBy);
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

    private void addAssociations(Connection connection,
                                HashMap<String, Activity> activities,
                                HashMap<String, Agent> agents,
                                List<Statement> relationships,
                                String contextWorkflowURI,
                                DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addAssociations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_ASSOCIATIONS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String associationID = resultSet.getString(1);
                String activityID = QueryConstants.ACTIVITY_IDENTIFIER + resultSet.getString(2);
                String agentID = resultSet.getString(3);
                String planID = resultSet.getString(4);

                Activity activity = activities.get(activityID);
                Agent agent = agents.get(QueryConstants.AGENT_IDENTIFIER + agentID);
                if (activity == null || agent == null) {
                    l.error("Activity or Agent is null. Inconsistent WasAssociatedWith relationship..");
                    return;
                }
                WasAssociatedWith wasAssociatedWith = pFactory.newWasAssociatedWith(getIdQName(associationID),
                        activity, agent);

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add attributes
                    if (planID != null) {
                        // TODO : handle plan
                    }
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ASSOCIATION_ATTRIBUTES_BY_ID,
                            associationID, wasAssociatedWith, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasAssociatedWith);
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

    private void addAttributions(Connection connection,
                                HashMap<String, Agent> agents,
                                HashMap<String, Entity> entities,
                                List<Statement> relationships,
                                String contextWorkflowURI,
                                DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addAttributions()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            // this query will return the attributions which are related to already considered agents
            // TODO : We have to consider attributions which are related to already considered entities too, that we introduce new Agents
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_ATTRIBUTIONS_THROUGH_ASSOCIATIONS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String attributionID = resultSet.getString(1);
                String agentID = resultSet.getString(2);
                String entityID = resultSet.getString(3);

                Agent agent = agents.get(QueryConstants.AGENT_IDENTIFIER + agentID);
                Entity entity = entities.get(entityID);
                // entity may not already exists. that happens when the entity is only connected to the
                // graph through the attribution
                if (entity == null) {
                    entity = createEntity(entityID, connection);
                }
                WasAttributedTo wasAttributedTo = pFactory.newWasAttributedTo(getIdQName(attributionID),
                        entity.getId(), agent.getId(), new ArrayList<Attribute>());

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_ATTRIBUTION_ATTRIBUTES_BY_ID,
                            attributionID, wasAttributedTo, connection);
                }
                // add the used element into the list of relationships
                relationships.add(wasAttributedTo);
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

    private void addDelegations(Connection connection,
                               HashMap<String, Agent> agents,
                               List<Statement> relationships,
                               String contextWorkflowURI,
                               DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addDelegations()");

        PreparedStatement stmt = null;
        ResultSet resultSet = null;

        try {
            /**
             * This query finds delegations in which the responsible agent is someone already associated with the
             * activity identified by the given workflow_uri.
             */
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_DELEGATIONS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String delegationID = resultSet.getString(1);
                String delAgentID = resultSet.getString(2);
                String resAgentID = resultSet.getString(3);
                String activityID = resultSet.getString(4);
                // properties of the new delegate agent
                // TODO : create a method to be called from here and getAgents()
                String uri = resultSet.getString("agent_uri");
                String type = resultSet.getString("agent_type");
                String name = resultSet.getString("name");
                String affiliation = resultSet.getString("affiliation");
                String email = resultSet.getString("email");
                // TODO : Handle role and location later
                String role = resultSet.getString("role");
                String location = resultSet.getString("location");

                Agent delAgent = agents.get(QueryConstants.AGENT_IDENTIFIER + delAgentID);
                Agent resAgent = agents.get(QueryConstants.AGENT_IDENTIFIER + resAgentID);

                if (delAgent == null) {
                    delAgent = newAgent(QueryConstants.AGENT_IDENTIFIER + delAgentID, uri, type);
                    // add name as an additional attribute
                    if (name != null) {
                        Other nameAtt = pFactory.newOther(getKomaduAttQName("name"), name,
                                Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(delAgent, nameAtt);
                    }
                    // add affiliation as an additional attribute
                    if (affiliation != null) {
                        Other affiliationAtt = pFactory.newOther(getKomaduAttQName("affiliation"),
                                affiliation, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(delAgent, affiliationAtt);
                    }
                    // add email as an additional attribute
                    if (email != null) {
                        Other emailAtt = pFactory.newOther(getKomaduAttQName("email"),
                                email, Name.QNAME_XSD_STRING);
                        pFactory.addAttribute(delAgent, emailAtt);
                    }
                    agents.put(QueryConstants.AGENT_IDENTIFIER + delAgentID, delAgent);
                }

                ActedOnBehalfOf behalfOf = pFactory.newActedOnBehalfOf(getIdQName(delegationID),
                        delAgent.getId(), resAgent.getId());

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DELEGATION_ATTRIBUTES_BY_ID,
                            delegationID, behalfOf, connection);
                }
                // add the used element into the list of relationships
                relationships.add(behalfOf);
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

    private void addCommunications(Connection connection,
                                  HashMap<String, Activity> activities,
                                  List<Statement> relationships,
                                  String contextWorkflowURI,
                                  DetailEnumType.Enum informationDetailLevel) throws SQLException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_COMMUNICATIONS_BY_ENTITY);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String informantID = resultSet.getString("gen_id");  // activity by which the entity was generated
                String informedID = resultSet.getString("used_id");  // activity by which the entity was used

                Activity infromantActivity = activities.get(informantID);
                Activity infromedActivity = activities.get(informedID);
                WasInformedBy informedBy = pFactory.newWasInformedBy(infromantActivity, infromedActivity);

                // add the used element into the list of relationships
                relationships.add(informedBy);
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_COMMUNICATIONS);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String communicationID = resultSet.getString(1);
                String informedID = resultSet.getString(2);
                String informantID = resultSet.getString(3);

                Activity informedActivity = activities.get(informedID);
                Activity informantActivity = activities.get(informantID);

                if (informedActivity == null) {
                    informedActivity = createActivityById(connection, informedID, informationDetailLevel);
                    if (informedActivity != null) {
                        activities.put(QueryConstants.ACTIVITY_IDENTIFIER + informedID, informedActivity);
                    } else {
                        l.error("No activity found. Invalid Activity ID : " + informedID);
                        continue;
                    }
                }

                if (informantActivity == null) {
                    informantActivity = createActivityById(connection, informantID, informationDetailLevel);
                    if (informantActivity != null) {
                        activities.put(QueryConstants.ACTIVITY_IDENTIFIER + informantID, informantActivity);
                    } else {
                        l.error("No activity found. Invalid Activity ID : " + informantID);
                        continue;
                    }
                }

                WasInformedBy informedBy = pFactory.newWasInformedBy(getIdQName(QueryConstants.COMMUNICATION_IDENTIFIER +
                        communicationID), informantActivity, informedActivity);

                if (informationDetailLevel != null
                        && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_COMMUNICATION_ATTRIBUTES_BY_ID,
                            communicationID, informedBy, connection);
                }
                // add the used element into the list of relationships
                relationships.add(informedBy);
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

    private void addDerivations(Connection connection,
                               HashMap<String, Entity> entities,
                               List<Statement> relationships,
                               String contextWorkflowURI,
                               DetailEnumType.Enum informationDetailLevel) throws SQLException, QueryException {
        assert (connection != null);
        assert (contextWorkflowURI != null);
        l.debug("Entering addDerivations()");

        /**
         * There are 2 possible cases here.
         * 1. There is a derivation notification in the database relating entity1 and entity2. In this
         *    case we directly map it into a derivation relationship in the graph. At least 1 entity must
         *    be already there in the list of entities.
         * 2. activity1 uses entity1 and generates entity2. But there's no derivation notification
         *    in the database for entity1 and entity2. In this case, we have to infer the derivation.
         */

        // derivations identified in case 1 should not be duplicated in case 2. therefore we have to
        // keep track of the pairs of entities considered in case 1
        List<String> foundList = new ArrayList<String>();

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            // Case 1.1 : both entities in context
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_DERIVATIONS_IN_CONTEXT);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String derivationId = resultSet.getString("derivation_id");
                String usedId = resultSet.getString("used_id");
                String generatedId = resultSet.getString("generated_id");
                String derivationType = resultSet.getString("derivation_type");
                // get entities from list
                Entity usedEntity = entities.get(usedId);
                Entity generatedEntity = entities.get(generatedId);
                // none of the entities can be null for this query
                if (usedEntity == null || generatedEntity == null) {
                    throw new QueryException("None of the entities can be null for a derivation in context");
                }
                // create the relationship
                WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                        derivationId), generatedEntity.getId(), usedEntity.getId());
                // if this is a revision, quotation or primary source, add type
                addDerivationType(derivationType, derivedFrom);
                if (informationDetailLevel != null && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DERIVATION_ATTRIBUTES_BY_ID,
                            derivationId, derivedFrom, connection);
                }
                // add the derivation element into the list of relationships
                relationships.add(derivedFrom);
                foundList.add(usedId + "-" + generatedId);
            }
            if (stmt != null) {
                stmt.close();
                stmt = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }

            // Case 1.2 : only the generated entity is in context
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_DERIVATIONS_GENERATED_IN_CONTEXT);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String derivationId = resultSet.getString("derivation_id");
                String usedId = resultSet.getString("used_id");
                String generatedId = resultSet.getString("generated_id");
                String derivationType = resultSet.getString("derivation_type");
                // get entities from list
                Entity usedEntity = entities.get(usedId);
                Entity generatedEntity = entities.get(generatedId);
                // generated entity must already be in the context
                if (generatedEntity == null) {
                    throw new QueryException("Generated entity can't be null because it's in the context");
                }
                if (usedEntity == null) {
                    usedEntity = createEntity(usedId, connection);
                }
                // create the relationship
                WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                        derivationId), generatedEntity.getId(), usedEntity.getId());
                // if this is a revision, quotation or primary source, add type
                addDerivationType(derivationType, derivedFrom);
                if (informationDetailLevel != null && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DERIVATION_ATTRIBUTES_BY_ID,
                            derivationId, derivedFrom, connection);
                }
                // add the used element into the list of relationships
                relationships.add(derivedFrom);
                foundList.add(usedId + "-" + generatedId);
            }
            if (stmt != null) {
                stmt.close();
                stmt = null;
            }
            if (resultSet != null) {
                resultSet.close();
                resultSet = null;
            }

            // Case 1.3 : only the used entity is in context
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_DERIVATIONS_USED_IN_CONTEXT);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);

            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String derivationId = resultSet.getString("derivation_id");
                String usedId = resultSet.getString("used_id");
                String generatedId = resultSet.getString("generated_id");
                String derivationType = resultSet.getString("derivation_type");
                // get entities from list
                Entity usedEntity = entities.get(usedId);
                Entity generatedEntity = entities.get(generatedId);
                // used entity can't be null in this case
                if (usedEntity == null) {
                    throw new QueryException("Used entity can't be null because it's in the context");
                }
                if (generatedEntity == null) {
                    generatedEntity = createEntity(generatedId, connection);
                }
                // create the relationship
                WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                        derivationId), generatedEntity.getId(), usedEntity.getId());
                // if this is a revision, quotation or primary source, add type
                addDerivationType(derivationType, derivedFrom);
                if (informationDetailLevel != null && informationDetailLevel.equals(DetailEnumType.FINE)) {
                    // add external attributes too
                    addCustomAttributes(PROVSqlQuery.GET_EXE_DERIVATION_ATTRIBUTES_BY_ID,
                            derivationId, derivedFrom, connection);
                }
                // add the used element into the list of relationships
                relationships.add(derivedFrom);
                foundList.add(usedId + "-" + generatedId);
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
            stmt = connection.prepareStatement(PROVSqlQuery.GET_PROV_DERIVATIONS_BY_ACTIVITY);
            stmt.setString(1, contextWorkflowURI);
            stmt.setString(2, contextWorkflowURI);
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                String generatedId = resultSet.getString("gen_id");
                String usedId = resultSet.getString("used_id");
                // now we have to check whether we've already considered this pair as a derivation
                if (!foundList.contains(usedId + "-" + generatedId)) {
                    // get entities from list
                    Entity usedEntity = entities.get(usedId);
                    Entity generatedEntity = entities.get(generatedId);
                    // used entity or generated entity can't be null in this case
                    if (usedEntity == null || generatedEntity == null) {
                        throw new QueryException("None of the entities can be null for a derivation in context");
                    }
                    // create the relationship
                    WasDerivedFrom derivedFrom = pFactory.newWasDerivedFrom(getIdQName(QueryConstants.DERIVATION_IDENTIFIER +
                            usedId + "_" + generatedId), generatedEntity.getId(), usedEntity.getId());
                    // add the used element into the list of relationships
                    relationships.add(derivedFrom);
                }
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

    private void addAlternates(Connection connection,
                              HashMap<String, Entity> entities,
                              List<Statement> relationships) throws SQLException, QueryException {
        assert (connection != null);
        assert (entities != null);
        l.debug("Entering addAlternates()");

        // Here we have a problem because we can't query for alternatives using the context
        // workflow uri. Therefore we have to check for each entity in entities list
        // TODO : Improve this if possible
        if (entities.isEmpty()) {
            return;
        }

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            // we are going to create the query by considering all entities that we have in the list
            StringBuilder query = new StringBuilder();
            query.append(PROVSqlQuery.GET_PROV_ALTERNATES);
            Set<String> entityIDs = entities.keySet();
            int i = 0;
            for (String entityId : entityIDs) {
                query.append("alternate1_id = ").append(entityId).append(" OR ");
                query.append("alternate2_id = ").append(entityId);
                if (i < entityIDs.size() - 1) {
                    query.append(" OR ");
                }
                i++;
            }
            stmt = connection.prepareStatement(query.toString());
            resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                String alt1 = resultSet.getString("alternate1_id");
                String alt2 = resultSet.getString("alternate2_id");
                Entity alt1Entity = entities.get(alt1);
                Entity alt2Entity = entities.get(alt2);
                if (alt1Entity == null && alt2Entity == null) {
                    throw new QueryException("At least 1 entity must not be null");
                }
                if (alt1Entity == null) {
                    alt1Entity = createEntity(alt1, connection);
                }
                if (alt2Entity == null) {
                    alt2Entity = createEntity(alt2, connection);
                }
                // create the relationship
                AlternateOf alternateOf = pFactory.newAlternateOf(alt1Entity.getId(), alt2Entity.getId());
                // add the used element into the list of relationships
                relationships.add(alternateOf);
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

    private void addSpecializations(Connection connection,
                                   HashMap<String, Entity> entities,
                                   List<Statement> relationships) throws SQLException, QueryException {
        assert (connection != null);
        assert (entities != null);
        l.debug("Entering addSpecializations()");

        // Here we have a problem because we can't query for specializations using the context
        // workflow uri. Therefore we have to check for each entity in entities list
        // TODO : Improve this if possible
        if (entities.isEmpty()) {
            return;
        }

        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            // we are going to create the query by considering all entities that we have in the list
            StringBuilder query = new StringBuilder();
            query.append(PROVSqlQuery.GET_PROV_SPECIALIZATIONS);
            Set<String> entityIDs = entities.keySet();
            int i = 0;
            for (String entityId : entityIDs) {
                query.append("specific_id = ").append(entityId).append(" OR ");
                query.append("general_id = ").append(entityId);
                if (i < entityIDs.size() - 1) {
                    query.append(" OR ");
                }
                i++;
            }
            stmt = connection.prepareStatement(query.toString());
            resultSet = stmt.executeQuery();
            while (resultSet.next()) {
                String specificId = resultSet.getString("specific_id");
                String generalId = resultSet.getString("general_id");
                Entity specificEntity = entities.get(specificId);
                Entity generalEntity = entities.get(generalId);
                if (specificEntity == null && generalEntity == null) {
                    throw new QueryException("At least 1 entity must not be null");
                }
                if (specificEntity == null) {
                    specificEntity = createEntity(specificId, connection);
                }
                if (generalEntity == null) {
                    generalEntity = createEntity(generalId, connection);
                }
                // create the relationship
                SpecializationOf specializationOf = pFactory.newSpecializationOf(specificEntity.getId(),
                        generalEntity.getId());
                // add the used element into the list of relationships
                relationships.add(specializationOf);
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

    private void addMemberships(Connection connection,
                                HashMap<String, Entity> entities,
                                List<Statement> relationships)
            throws SQLException, QueryException {
        assert (connection != null);
        assert (entities != null);
        l.debug("Entering addMemberships()");

        if (entities.isEmpty()) {
            return;
        }

        HashMap<Integer, List<QName>> collections = new HashMap<Integer, List<QName>>();
        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        try {
            // we are going to create the query by considering all entities that we have in the list
            StringBuilder query = new StringBuilder();
            query.append(PROVSqlQuery.GET_PROV_MEMBERSHIPS);
            Set<String> entityIDs = entities.keySet();
            int i = 0;
            for (String entityId : entityIDs) {
                query.append("collection_id = ").append(entityId);
                if (i < entityIDs.size() - 1) {
                    query.append(" OR ");
                }
                i++;
            }
            stmt = connection.prepareStatement(query.toString());
            resultSet = stmt.executeQuery();

            while (resultSet.next()) {
                int collectionId = resultSet.getInt("collection_id");
                int memberId = resultSet.getInt("member_id");
                // get entity from list
                List<QName> collection = collections.get(collectionId);
                if (collection == null) {
                    collection = new ArrayList<QName>();
                    collections.put(collectionId, collection);
                }
                Entity memberEntity = entities.get("" + memberId);
                if (memberEntity == null) {
                    memberEntity = createEntity("" + memberId, connection);
                }
                collection.add(memberEntity.getId());
            }

            Set<Integer> keys = collections.keySet();
            for (Integer key : keys) {
                List<QName> members = collections.get(key);
                if (members.size() > 0) {
                    // get the collection entity which must already be in the list
                    Entity collectionEntity = entities.get("" + key);
                    // create the relationship
                    HadMember hadMember = pFactory.newHadMember(collectionEntity.getId(), members);
                    // add the used element into the list of relationships
                    relationships.add(hadMember);
                }
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
     * Creates a PROV Activity by querying the database using the given db id.
     */
    private Activity createActivityById(Connection connection, String dbId,
                                        DetailEnumType.Enum infoDetailLevel)
            throws SQLException {
        PreparedStatement stmt = null;
        ResultSet resultSet = null;
        Activity activity = null;

        try {
            stmt = connection.prepareStatement(PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_ID);
            stmt.setString(1, dbId);
            resultSet = stmt.executeQuery();
            if (resultSet.next()) {
                int activityID = resultSet.getInt("activity_id");
                String activityUri = resultSet.getString("activity_uri");
                String activityType = resultSet.getString("activity_type");
                String contextWorkflowUri = resultSet.getString("context_workflow_uri");
                String contextServiceUri = resultSet.getString("context_service_uri");
                String timestep = resultSet.getString("timestep");
//                String location = resultSet.getString("location");     // TODO : Handle location, role
                String contextWfNodeIdToken = resultSet.getString("context_wf_node_id_token");

                // create new prov activity
                activity = pFactory.newActivity(getIdQName(
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
        return activity;
    }

}
