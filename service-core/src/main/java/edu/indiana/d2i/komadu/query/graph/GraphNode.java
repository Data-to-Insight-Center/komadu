package edu.indiana.d2i.komadu.query.graph;

public class GraphNode {

    public static enum NodeType {
        ACTIVITY,
        ENTITY,
        AGENT
    }

    private NodeType type;
    private int internalID;

    public GraphNode(NodeType type, int internalID) {
        this.type = type;
        this.internalID = internalID;
    }

    public NodeType getType() {
        return type;
    }

    public int getInternalID() {
        return internalID;
    }
}
