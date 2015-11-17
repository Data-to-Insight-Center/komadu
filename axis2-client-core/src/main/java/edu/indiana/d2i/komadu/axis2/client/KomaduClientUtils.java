package edu.indiana.d2i.komadu.axis2.client;

import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.AgentResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Map;

public class KomaduClientUtils {

    public static AgentResult createAgent(
            Map<String, String> agentAttributes) throws Exception {
        AgentResult agent = null;
        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_USER)) {
            agent = createUserAgent(agentAttributes);
        } else if (agentAttributes.containsKey(KomaduClientConstants.AGENT_GENERIC)) {
            agent = createGenericAgent(agentAttributes);
        }
        return agent;
    }

    public static ActivityResult createActivity(
            Map<String, String> activityAttributes) throws Exception {
        ActivityResult activity = null;
        if (activityAttributes.containsKey(KomaduClientConstants.ACTIVITY_WORKFLOW)) {
            activity = createWorkflowActivity(activityAttributes);
        } else if (activityAttributes.containsKey(KomaduClientConstants.ACTIVITY_SERVICE)) {
            activity = createServiceActivity(activityAttributes);
        } else if (activityAttributes.containsKey(KomaduClientConstants.ACTIVITY_METHOD)) {
            activity = createMethodActivity(activityAttributes);
        } else if (activityAttributes.containsKey(KomaduClientConstants.ACTIVITY_GENERIC)) {
            activity = createGenericActivity(activityAttributes);
        }
        return activity;
    }

    public static EntityResult createEntity(Map<String, String> entityAttributes)
            throws Exception {
        EntityResult entity = null;
        if (entityAttributes.containsKey(KomaduClientConstants.ENTITY_FILE)) {
            entity = createFileEntity(entityAttributes);
        } else if (entityAttributes.containsKey(KomaduClientConstants.ENTITY_COLLECTION)) {
            entity = createCollectionEntity(entityAttributes);
        } else if (entityAttributes.containsKey(KomaduClientConstants.ENTITY_GENERIC)) {
            entity = createGenericEntity(entityAttributes);
        }
        return entity;
    }

    public static AssociationType createAssociation(Map<String, String> assAttributes,
                                                    String agentId,
                                                    String activityId) throws Exception {
        AssociationType association = AssociationType.Factory.newInstance();
        association.setAgentID(agentId);
        association.setActivityID(activityId);
        association.setAttributes(createAttributes(assAttributes, new ArrayList<String>()));
        return association;
    }

    public static UsageType createUsage(Map<String, String> usageAttributes,
                                        String entityId,
                                        String activityId) throws Exception {
        UsageType usage = UsageType.Factory.newInstance();
        usage.setActivityID(activityId);
        usage.setEntityID(entityId);
        usage.setTimestamp(Calendar.getInstance());
        usage.setAttributes(createAttributes(usageAttributes, new ArrayList<String>()));
        return usage;
    }

    public static GenerationType createGeneration(Map<String, String> generationAttributes,
                                                  String entityId,
                                                  String activityId) throws Exception {
        GenerationType generation = GenerationType.Factory.newInstance();
        generation.setActivityID(activityId);
        generation.setEntityID(entityId);
        generation.setTimestamp(Calendar.getInstance());
        generation.setAttributes(createAttributes(generationAttributes, new ArrayList<String>()));
        return generation;
    }

    public static StartType createStart(Map<String, String> startAttributes,
                                        String entityId,
                                        String activityId) throws Exception {
        StartType start = StartType.Factory.newInstance();
        start.setActivityID(activityId);
        start.setTriggerID(entityId);
        start.setTimestamp(Calendar.getInstance());
        start.setAttributes(createAttributes(startAttributes, new ArrayList<String>()));
        return start;
    }

    public static EndType createEnd(Map<String, String> endAttributes,
                                    String entityId,
                                    String activityId) throws Exception {
        EndType usage = EndType.Factory.newInstance();
        usage.setActivityID(activityId);
        usage.setTriggerID(entityId);
        usage.setTimestamp(Calendar.getInstance());
        usage.setAttributes(createAttributes(endAttributes, new ArrayList<String>()));
        return usage;
    }

    public static InvalidationType createInvalidation(Map<String, String> invalidationAttributes,
                                                      String entityId,
                                                      String activityId) throws Exception {
        InvalidationType invalidation = InvalidationType.Factory.newInstance();
        invalidation.setActivityID(activityId);
        invalidation.setEntityID(entityId);
        invalidation.setTimestamp(Calendar.getInstance());
        invalidation.setAttributes(createAttributes(invalidationAttributes, new ArrayList<String>()));
        return invalidation;
    }

    public static DelegationType createDelegation(Map<String, String> delegationAttributes,
                                                  String delegateId,
                                                  String responsibleId) throws Exception {
        DelegationType delegation = DelegationType.Factory.newInstance();
        delegation.setDelegateAgentID(delegateId);
        delegation.setResponsibleAgentID(responsibleId);
        delegation.setAttributes(createAttributes(delegationAttributes, new ArrayList<String>()));
        return delegation;
    }

    public static AttributionType createAttribution(Map<String, String> attributionAttributes,
                                                    String entityId,
                                                    String agentId) throws Exception {
        AttributionType attribution = AttributionType.Factory.newInstance();
        attribution.setAgentID(agentId);
        attribution.setEntityID(entityId);
        attribution.setAttributes(createAttributes(attributionAttributes, new ArrayList<String>()));
        return attribution;
    }

    public static CommunicationType createCommunication(Map<String, String> communicationAttributes,
                                                        String informantId,
                                                        String informedId) throws Exception {
        CommunicationType communication = CommunicationType.Factory.newInstance();
        communication.setInformantActivityID(informantId);
        communication.setInformedActivityID(informedId);
        communication.setAttributes(createAttributes(communicationAttributes, new ArrayList<String>()));
        return communication;
    }

    public static DerivationType createDerivation(KomaduClientConstants.Derivation derType,
                                                  Map<String, String> derivationAttributes,
                                                  String usedId,
                                                  String generatedId) throws Exception {
        DerivationType derivation;
        if (derType == KomaduClientConstants.Derivation.REVISION) {
            derivation = RevisionType.Factory.newInstance();
        } else if (derType == KomaduClientConstants.Derivation.QUOTATION) {
            derivation = QuotationType.Factory.newInstance();
        } else if (derType == KomaduClientConstants.Derivation.PRIMARY_SOURCE) {
            derivation = PrimarySourceType.Factory.newInstance();
        } else {
            derivation = DerivationType.Factory.newInstance();
        }
        derivation.setUsedEntityID(usedId);
        derivation.setGeneratedEntityID(generatedId);
        derivation.setAttributes(createAttributes(derivationAttributes, new ArrayList<String>()));
        return derivation;
    }

    public static EntityResult createFileEntity(
            Map<String, String> entityAttributes) throws Exception {
        EntityResult result = new EntityResult();
        EntityType entity = EntityType.Factory.newInstance();
        FileType file = FileType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ENTITY_FILE);

        if (entityAttributes.containsKey(KomaduClientConstants.FILE_URI)) {
            file.setFileURI(entityAttributes.get(KomaduClientConstants.FILE_URI));
            knownAttributes.add(KomaduClientConstants.FILE_URI);
            result.setEntityId(entityAttributes.get(KomaduClientConstants.FILE_URI));
        } else {
            throw new Exception(KomaduClientConstants.FILE_URI + " missing..");
        }

        if (entityAttributes.containsKey(KomaduClientConstants.FILE_NAME)) {
            file.setFileName(entityAttributes.get(KomaduClientConstants.FILE_NAME));
            knownAttributes.add(KomaduClientConstants.FILE_NAME);
        }

        if (entityAttributes.containsKey(KomaduClientConstants.FILE_OWNER)) {
            file.setOwnerDN(entityAttributes.get(KomaduClientConstants.FILE_OWNER));
            knownAttributes.add(KomaduClientConstants.FILE_OWNER);
        }

        if (entityAttributes.containsKey(KomaduClientConstants.FILE_CREATE_DATE)) {
            file.setCreateDate(Calendar.getInstance());
            knownAttributes.add(KomaduClientConstants.FILE_CREATE_DATE);
        }

        if (entityAttributes.containsKey(KomaduClientConstants.FILE_SIZE)) {
            file.setSize(Long.parseLong(entityAttributes.get(KomaduClientConstants.FILE_SIZE)));
            knownAttributes.add(KomaduClientConstants.FILE_SIZE);
        }

        entity.setAttributes(createAttributes(entityAttributes, knownAttributes));
        entity.setFile(file);
        result.setEntity(entity);
        return result;
    }

    public static EntityResult createCollectionEntity(
            Map<String, String> entityAttributes) throws Exception {
        // TODO
        return new EntityResult();
    }

    public static EntityResult createGenericEntity(
            Map<String, String> entityAttributes) throws Exception {
        EntityResult result = new EntityResult();
        EntityType entity = EntityType.Factory.newInstance();
        GenericEntityType genericEntity = GenericEntityType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ENTITY_GENERIC);

        if (entityAttributes.containsKey(KomaduClientConstants.ENTITY_URI)) {
            genericEntity.setEntityURI(entityAttributes.get(KomaduClientConstants.ENTITY_URI));
            knownAttributes.add(KomaduClientConstants.ENTITY_URI);
            result.setEntityId(entityAttributes.get(KomaduClientConstants.ENTITY_URI));
        } else {
            throw new Exception(KomaduClientConstants.ENTITY_URI + " missing..");
        }

        entity.setAttributes(createAttributes(entityAttributes, knownAttributes));
        entity.setGenericEntity(genericEntity);
        result.setEntity(entity);
        return result;
    }

    public static AgentResult createUserAgent(
            Map<String, String> agentAttributes) throws Exception {
        AgentResult result = new AgentResult();
        UserAgentType userAgent = UserAgentType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.AGENT_USER);

        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_ID)) {
            userAgent.setAgentID(agentAttributes.get(KomaduClientConstants.AGENT_ID));
            knownAttributes.add(KomaduClientConstants.AGENT_ID);
            result.setAgentId(agentAttributes.get(KomaduClientConstants.AGENT_ID));
        } else {
            throw new Exception(KomaduClientConstants.AGENT_ID + " missing..");
        }

        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_FULL_NAME)) {
            userAgent.setFullName(agentAttributes.get(KomaduClientConstants.AGENT_FULL_NAME));
            knownAttributes.add(KomaduClientConstants.AGENT_FULL_NAME);
        }

        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_AFFILIATION)) {
            userAgent.setAffiliation(agentAttributes.get(KomaduClientConstants.AGENT_AFFILIATION));
            knownAttributes.add(KomaduClientConstants.AGENT_AFFILIATION);
        }

        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_EMAIL)) {
            userAgent.setEmail(agentAttributes.get(KomaduClientConstants.AGENT_EMAIL));
            knownAttributes.add(KomaduClientConstants.AGENT_EMAIL);
        }
        userAgent.setAttributes(createAttributes(agentAttributes, knownAttributes));
        AgentType agent = AgentType.Factory.newInstance();
        agent.setUserAgent(userAgent);
        result.setAgent(agent);
        return result;
    }

    public static AgentResult createGenericAgent(
            Map<String, String> agentAttributes) throws Exception {
        AgentResult result = new AgentResult();
        List<String> knownAttributes = new ArrayList<String>();
        GenericAgentType genericAgent = GenericAgentType.Factory.newInstance();
        knownAttributes.add(KomaduClientConstants.AGENT_GENERIC);

        if (agentAttributes.containsKey(KomaduClientConstants.AGENT_ID)) {
            genericAgent.setAgentID(agentAttributes.get(KomaduClientConstants.AGENT_ID));
            knownAttributes.add(KomaduClientConstants.AGENT_ID);
            result.setAgentId(agentAttributes.get(KomaduClientConstants.AGENT_ID));
        } else {
            throw new Exception(KomaduClientConstants.AGENT_ID + " missing..");
        }

        genericAgent.setAttributes(createAttributes(agentAttributes, knownAttributes));
        AgentType agent = AgentType.Factory.newInstance();
        agent.setGenericAgent(genericAgent);
        result.setAgent(agent);
        return result;
    }

    public static ActivityResult createGenericActivity(
            Map<String, String> activityAttributes) throws Exception {
        ActivityResult result = new ActivityResult();
        ActivityType activity = ActivityType.Factory.newInstance();
        ActivityInformationType activityInfo = ActivityInformationType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ACTIVITY_GENERIC);

        // set activity id
        if (activityAttributes.containsKey(KomaduClientConstants.ACTIVITY_ID)) {
            activityInfo.setActivityID(activityAttributes.get(KomaduClientConstants.ACTIVITY_ID));
            knownAttributes.add(KomaduClientConstants.ACTIVITY_ID);
            result.setActivityId(activityAttributes.get(KomaduClientConstants.ACTIVITY_ID));
        } else {
            throw new Exception(KomaduClientConstants.ACTIVITY_ID + " missing..");
        }

        activityInfo.setAttributes(createAttributes(activityAttributes, knownAttributes));
        activity.setActivityInformation(activityInfo);
        result.setActivity(activity);
        return result;
    }

    public static ActivityResult createWorkflowActivity(
            Map<String, String> activityAttributes) throws Exception {
        ActivityResult result = new ActivityResult();
        ActivityType activity = ActivityType.Factory.newInstance();
        WorkflowInformationType workflow = WorkflowInformationType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ACTIVITY_WORKFLOW);
        // set workflow id
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_ID)) {
            workflow.setWorkflowID(activityAttributes.get(KomaduClientConstants.WORKFLOW_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_ID);
            result.setActivityId(activityAttributes.get(KomaduClientConstants.WORKFLOW_ID));
        } else {
            throw new Exception(KomaduClientConstants.WORKFLOW_ID + " missing..");
        }
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_NODE_ID)) {
            workflow.setWorkflowNodeID(activityAttributes.get(KomaduClientConstants.WORKFLOW_NODE_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_NODE_ID);
        }
        // Instance of
        if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_ID)) {
            InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
            instanceOf.setInstanceOfID(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_ID));
            knownAttributes.add(KomaduClientConstants.INSTANCE_OF_ID);
            if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_VERSION)) {
                instanceOf.setVersion(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_VERSION));
                knownAttributes.add(KomaduClientConstants.INSTANCE_OF_VERSION);
            }
            instanceOf.setCreationTime(Calendar.getInstance());
            workflow.setInstanceOf(instanceOf);
        }
        workflow.setAttributes(createAttributes(activityAttributes, knownAttributes));
        activity.setWorkflowInformation(workflow);
        result.setActivity(activity);
        return result;
    }

    public static ActivityResult createServiceActivity(
            Map<String, String> activityAttributes) throws Exception {
        ActivityResult result = new ActivityResult();
        ActivityType activity = ActivityType.Factory.newInstance();
        ServiceInformationType service = ServiceInformationType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ACTIVITY_SERVICE);
        // set workflow id
        if (activityAttributes.containsKey(KomaduClientConstants.SERVICE_ID)) {
            service.setServiceID(activityAttributes.get(KomaduClientConstants.SERVICE_ID));
            knownAttributes.add(KomaduClientConstants.SERVICE_ID);
            result.setActivityId(activityAttributes.get(KomaduClientConstants.SERVICE_ID));
        } else {
            throw new Exception(KomaduClientConstants.SERVICE_ID + " missing..");
        }
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_ID)) {
            service.setWorkflowID(activityAttributes.get(KomaduClientConstants.WORKFLOW_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_ID);
        }
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_NODE_ID)) {
            service.setWorkflowNodeID(activityAttributes.get(KomaduClientConstants.WORKFLOW_NODE_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_NODE_ID);
        }
        // Instance of
        if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_ID)) {
            InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
            instanceOf.setInstanceOfID(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_ID));
            knownAttributes.add(KomaduClientConstants.INSTANCE_OF_ID);
            if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_VERSION)) {
                instanceOf.setVersion(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_VERSION));
                knownAttributes.add(KomaduClientConstants.INSTANCE_OF_VERSION);
            }
            instanceOf.setCreationTime(Calendar.getInstance());
            service.setInstanceOf(instanceOf);
        }
        service.setAttributes(createAttributes(activityAttributes, knownAttributes));
        activity.setServiceInformation(service);
        result.setActivity(activity);
        return result;
    }

    public static ActivityResult createMethodActivity(
            Map<String, String> activityAttributes) throws Exception {
        ActivityResult result = new ActivityResult();
        ActivityType activity = ActivityType.Factory.newInstance();
        MethodInformationType method = MethodInformationType.Factory.newInstance();
        List<String> knownAttributes = new ArrayList<String>();
        knownAttributes.add(KomaduClientConstants.ACTIVITY_METHOD);
        // set workflow id
        if (activityAttributes.containsKey(KomaduClientConstants.METHOD_ID)) {
            method.setMethodID(activityAttributes.get(KomaduClientConstants.METHOD_ID));
            knownAttributes.add(KomaduClientConstants.METHOD_ID);
            result.setActivityId(activityAttributes.get(KomaduClientConstants.METHOD_ID));
        } else {
            throw new Exception(KomaduClientConstants.METHOD_ID + " missing..");
        }
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_ID)) {
            method.setWorkflowID(activityAttributes.get(KomaduClientConstants.WORKFLOW_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_ID);
        }
        if (activityAttributes.containsKey(KomaduClientConstants.SERVICE_ID)) {
            method.setServiceID(activityAttributes.get(KomaduClientConstants.SERVICE_ID));
            knownAttributes.add(KomaduClientConstants.SERVICE_ID);
        }
        if (activityAttributes.containsKey(KomaduClientConstants.WORKFLOW_NODE_ID)) {
            method.setWorkflowNodeID(activityAttributes.get(KomaduClientConstants.WORKFLOW_NODE_ID));
            knownAttributes.add(KomaduClientConstants.WORKFLOW_NODE_ID);
        }
        // Instance of
        if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_ID)) {
            InstanceOfType instanceOf = InstanceOfType.Factory.newInstance();
            instanceOf.setInstanceOfID(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_ID));
            knownAttributes.add(KomaduClientConstants.INSTANCE_OF_ID);
            if (activityAttributes.containsKey(KomaduClientConstants.INSTANCE_OF_VERSION)) {
                instanceOf.setVersion(activityAttributes.get(KomaduClientConstants.INSTANCE_OF_VERSION));
                knownAttributes.add(KomaduClientConstants.INSTANCE_OF_VERSION);
            }
            instanceOf.setCreationTime(Calendar.getInstance());
            method.setInstanceOf(instanceOf);
        }
        method.setAttributes(createAttributes(activityAttributes, knownAttributes));
        activity.setMethodInformation(method);
        result.setActivity(activity);
        return result;
    }

    public static AttributeType createAttribute(String name, String val) throws Exception {
        AttributeType att = AttributeType.Factory.newInstance();
        att.setProperty(name);
        att.setValue(val);
        return att;
    }

    private static AttributesType createAttributes(Map<String, String> fullList,
                                                   List<String> known) throws Exception {
        AttributesType attributes = AttributesType.Factory.newInstance();
        // create the attributes list by skipping known attributes
        List<AttributeType> attributeList = new ArrayList<AttributeType>();
        for (String key : fullList.keySet()) {
            if (!known.contains(key)) {
                attributeList.add(createAttribute(key, fullList.get(key)));
            }
        }
        attributes.setAttributeArray(attributeList.toArray(new AttributeType[attributeList.size()]));
        return attributes;
    }

}
