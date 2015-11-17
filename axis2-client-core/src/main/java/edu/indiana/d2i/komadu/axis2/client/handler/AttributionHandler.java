package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.AgentResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class AttributionHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> agentAttributes;
    Map<String, String> attributionAttributes;

    public AttributionHandler(KomaduServiceStub stub,
                              Map<String, String> entityAttributes,
                              Map<String, String> agentAttributes,
                              Map<String, String> attributionAttributes) {
        this.entityAttributes = entityAttributes;
        this.agentAttributes = agentAttributes;
        this.attributionAttributes = attributionAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddAgentEntityRelationshipDocument agentEntity =
                    AddAgentEntityRelationshipDocument.Factory.newInstance();
            AgentEntityType agentEntityType = AgentEntityType.Factory.newInstance();

            AgentResult agentResult = KomaduClientUtils.createAgent(agentAttributes);
            EntityResult entityResult = KomaduClientUtils.createEntity(entityAttributes);

            AttributionType attribution = KomaduClientUtils.createAttribution(attributionAttributes,
                    entityResult.getEntityId(), agentResult.getAgentId());

            agentEntityType.setAgent(agentResult.getAgent());
            agentEntityType.setEntity(entityResult.getEntity());
            agentEntityType.setAttribution(attribution);
            agentEntity.setAddAgentEntityRelationship(agentEntityType);
            // invoke
            stub.addAgentEntityRelationship(agentEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
