package edu.indiana.d2i.komadu.query.graph;


import edu.indiana.d2i.komadu.query.PROVSqlQuery;
import edu.indiana.d2i.komadu.query.QueryException;

import java.sql.Connection;
import java.sql.SQLException;

public class ActivityGraphGenerator extends NonContextGraphGenerator {

    @Override
    protected void populateRoot(Connection connection, String activityURI)
            throws QueryException, SQLException {
        // create the root activity and get it's internal id
        int rootID = createActivity(connection,
                PROVSqlQuery.GET_ACTIVITIES_BY_ACTIVITY_URI, activityURI);
        unexpandedNodes.push(new GraphNode(GraphNode.NodeType.ACTIVITY, rootID));
    }

}
