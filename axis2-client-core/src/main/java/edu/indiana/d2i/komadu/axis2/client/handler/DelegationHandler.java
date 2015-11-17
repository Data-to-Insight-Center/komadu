package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.AgentResult;

import java.util.Map;

public class DelegationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> delegateAgentAttributes;
    Map<String, String> responsibleAgentAttributes;
    Map<String, String> delegationAttributes;

    public DelegationHandler(KomaduServiceStub stub,
                             Map<String, String> delegateAgentAttributes,
                             Map<String, String> responsibleAgentAttributes,
                             Map<String, String> delegationAttributes) {
        this.delegateAgentAttributes = delegateAgentAttributes;
        this.responsibleAgentAttributes = responsibleAgentAttributes;
        this.delegationAttributes = delegationAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddAgentAgentRelationshipDocument agentAgent = AddAgentAgentRelationshipDocument.Factory.newInstance();
            AgentAgentType agentAgentType = AgentAgentType.Factory.newInstance();
            // Delegate agent
            AgentResult delegateAgent = KomaduClientUtils.createAgent(delegateAgentAttributes);
            agentAgentType.setDelegateAgent(delegateAgent.getAgent());
            // Responsible agent
            AgentResult responsibleAgent = KomaduClientUtils.createAgent(responsibleAgentAttributes);
            agentAgentType.setResponsibleAgent(responsibleAgent.getAgent());
            // Delegation
            DelegationType delegation = KomaduClientUtils.createDelegation(delegationAttributes,
                    delegateAgent.getAgentId(), responsibleAgent.getAgentId());
            agentAgentType.setDelegation(delegation);

            agentAgent.setAddAgentAgentRelationship(agentAgentType);
            // execute
            stub.addAgentAgentRelationship(agentAgent);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}