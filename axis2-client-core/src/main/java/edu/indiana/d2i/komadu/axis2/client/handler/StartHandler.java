package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class StartHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> startAttributes;

    public StartHandler(KomaduServiceStub stub,
                        Map<String, String> entityAttributes,
                        Map<String, String> activityAttributes,
                        Map<String, String> startAttributes) {
        this.entityAttributes = entityAttributes;
        this.activityAttributes = activityAttributes;
        this.startAttributes = startAttributes;
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

            StartType start = KomaduClientUtils.createStart(startAttributes,
                    entityResult.getEntityId(), activityResult.getActivityId());

            activityEntityType.setActivity(activityResult.getActivity());
            activityEntityType.setEntity(entityResult.getEntity());
            activityEntityType.setStart(start);
            activityEntity.setAddActivityEntityRelationship(activityEntityType);
            // invoke
            stub.addActivityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}