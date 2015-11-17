package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class InvalidationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> invalidationAttributes;

    public InvalidationHandler(KomaduServiceStub stub,
                               Map<String, String> entityAttributes,
                               Map<String, String> activityAttributes,
                               Map<String, String> invalidationAttributes) {
        this.entityAttributes = entityAttributes;
        this.activityAttributes = activityAttributes;
        this.invalidationAttributes = invalidationAttributes;
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

            InvalidationType invalidation = KomaduClientUtils.createInvalidation(invalidationAttributes,
                    entityResult.getEntityId(), activityResult.getActivityId());

            activityEntityType.setActivity(activityResult.getActivity());
            activityEntityType.setEntity(entityResult.getEntity());
            activityEntityType.setInvalidation(invalidation);
            activityEntity.setAddActivityEntityRelationship(activityEntityType);
            // invoke
            stub.addActivityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}