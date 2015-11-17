package edu.indiana.d2i.komadu.axis2.client;

public class KomaduClientConstants {

    public static final String AGENT_USER = "agent.user";
    public static final String AGENT_GENERIC = "agent.generic";

    public static final String ACTIVITY_WORKFLOW = "activity.workflow";
    public static final String ACTIVITY_SERVICE = "activity.service";
    public static final String ACTIVITY_METHOD = "activity.method";
    public static final String ACTIVITY_GENERIC = "activity.generic";

    public static final String ENTITY_FILE = "entity.file";
    public static final String ENTITY_COLLECTION = "entity.collection";
    public static final String ENTITY_GENERIC = "entity.generic";

    public static final String WORKFLOW_ID = "workflowID";
    public static final String WORKFLOW_NODE_ID = "workflowNodeID";
    public static final String SERVICE_ID = "serviceID";
    public static final String METHOD_ID = "methodID";
    public static final String ACTIVITY_ID = "activityID";
    public static final String INSTANCE_OF_ID = "instanceOfID";
    public static final String INSTANCE_OF_VERSION = "instanceOfVersion";

    public static final String AGENT_ID = "agentID";
    public static final String AGENT_FULL_NAME = "fullName";
    public static final String AGENT_AFFILIATION = "affiliation";
    public static final String AGENT_EMAIL = "email";

    public static final String FILE_URI = "fileURI";
    public static final String FILE_OWNER = "ownerDN";
    public static final String FILE_CREATE_DATE = "createDate";
    public static final String FILE_SIZE = "size";
    public static final String FILE_NAME = "fileName";

    public static final String ENTITY_URI = "entityURI";

    public static enum Derivation {
        DERIVATION, REVISION, QUOTATION, PRIMARY_SOURCE
    }
}
