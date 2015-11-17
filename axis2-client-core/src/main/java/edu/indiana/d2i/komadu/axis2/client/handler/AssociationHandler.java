package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.AgentResult;

import java.util.Map;

public class AssociationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> agentAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> associationAttributes;

    public AssociationHandler(KomaduServiceStub stub,
                              Map<String, String> agentAttributes,
                              Map<String, String> activityAttributes,
                              Map<String, String> associationAttributes) {
        this.agentAttributes = agentAttributes;
        this.activityAttributes = activityAttributes;
        this.associationAttributes = associationAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddAgentActivityRelationshipDocument agentActivity =
                    AddAgentActivityRelationshipDocument.Factory.newInstance();
            AgentActivityType agentActivityType = AgentActivityType.Factory.newInstance();

            ActivityResult activityResult = KomaduClientUtils.createActivity(activityAttributes);
            agentActivityType.setActivity(activityResult.getActivity());
            AgentResult agentResult = KomaduClientUtils.createAgent(agentAttributes);
            agentActivityType.setAgent(agentResult.getAgent());
            AssociationType association = KomaduClientUtils.createAssociation(associationAttributes,
                    agentResult.getAgentId(), activityResult.getActivityId());
            agentActivityType.setAssociation(association);
            agentActivity.setAddAgentActivityRelationship(agentActivityType);
            // send notification to Komadu server
            stub.addAgentActivityRelationship(agentActivity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
