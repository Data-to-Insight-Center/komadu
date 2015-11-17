package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class EndHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> endAttributes;

    public EndHandler(KomaduServiceStub stub,
                      Map<String, String> entityAttributes,
                      Map<String, String> activityAttributes,
                      Map<String, String> endAttributes) {
        this.entityAttributes = entityAttributes;
        this.activityAttributes = activityAttributes;
        this.endAttributes = endAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddActivityEntityRelationshipDocument activityEntity =
                    AddActivityEntityRelationshipDocument.Factory.newInstance();
            ActivityEntityType activityEntityType = ActivityEntityType.Factory.newInstance();

            ActivityResult activityResult = KomaduClientUtils.createActivity(activityAttributes);
            EntityResult entityResult = KomaduClientUtils.createEntity(entityAttributes);

            EndType end = KomaduClientUtils.createEnd(endAttributes,
                    entityResult.getEntityId(), activityResult.getActivityId());

            activityEntityType.setActivity(activityResult.getActivity());
            activityEntityType.setEntity(entityResult.getEntity());
            activityEntityType.setEnd(end);
            activityEntity.setAddActivityEntityRelationship(activityEntityType);
            // invoke
            stub.addActivityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
