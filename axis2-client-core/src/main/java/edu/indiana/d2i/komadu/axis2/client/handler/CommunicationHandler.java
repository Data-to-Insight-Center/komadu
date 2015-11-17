package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;

import java.util.Map;

public class CommunicationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> informantAttributes;
    Map<String, String> informedAttributes;
    Map<String, String> communicationAttributes;

    public CommunicationHandler(KomaduServiceStub stub,
                                Map<String, String> informantAttributes,
                                Map<String, String> informedAttributes,
                                Map<String, String> communicationAttributes) {
        this.informantAttributes = informantAttributes;
        this.informedAttributes = informedAttributes;
        this.communicationAttributes = communicationAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddActivityActivityRelationshipDocument activityActivity =
                    AddActivityActivityRelationshipDocument.Factory.newInstance();
            ActivityActivityType activityActivityType = ActivityActivityType.Factory.newInstance();

            ActivityResult informantResult = KomaduClientUtils.createActivity(informantAttributes);
            ActivityResult informedResult = KomaduClientUtils.createActivity(informedAttributes);

            CommunicationType communication = KomaduClientUtils.createCommunication(communicationAttributes,
                    informantResult.getActivityId(), informedResult.getActivityId());

            activityActivityType.setActivity1(informantResult.getActivity());
            activityActivityType.setActivity2(informedResult.getActivity());
            activityActivityType.setCommunication(communication);
            activityActivity.setAddActivityActivityRelationship(activityActivityType);
            // invoke
            stub.addActivityActivityRelationship(activityActivity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}