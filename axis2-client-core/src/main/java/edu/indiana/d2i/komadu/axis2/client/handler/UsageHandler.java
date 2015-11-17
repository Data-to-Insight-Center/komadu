package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class UsageHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> usageAttributes;

    public UsageHandler(KomaduServiceStub stub,
                        Map<String, String> entityAttributes,
                        Map<String, String> activityAttributes,
                        Map<String, String> usageAttributes) {
        this.entityAttributes = entityAttributes;
        this.activityAttributes = activityAttributes;
        this.usageAttributes = usageAttributes;
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

            UsageType usage = KomaduClientUtils.createUsage(usageAttributes,
                    entityResult.getEntityId(), activityResult.getActivityId());

            activityEntityType.setActivity(activityResult.getActivity());
            activityEntityType.setEntity(entityResult.getEntity());
            activityEntityType.setUsage(usage);
            activityEntity.setAddActivityEntityRelationship(activityEntityType);
            // invoke
            stub.addActivityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}