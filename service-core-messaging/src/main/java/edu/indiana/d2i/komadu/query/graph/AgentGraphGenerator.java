package edu.indiana.d2i.komadu.query.graph;

import edu.indiana.d2i.komadu.query.PROVSqlQuery;
import edu.indiana.d2i.komadu.query.QueryException;

import java.sql.Connection;
import java.sql.SQLException;

public class AgentGraphGenerator extends NonContextGraphGenerator {

    @Override
    protected void populateRoot(Connection connection, String agentURI)
            throws QueryException, SQLException {
        // find this agent in the database and get the db id
        int rootID = createAgent(connection, PROVSqlQuery.GET_AGENTS_BY_AGENT_URI, agentURI);
        // push the id to the unexpanded node stack
        unexpandedNodes.push(new GraphNode(GraphNode.NodeType.AGENT, rootID));
    }

}
