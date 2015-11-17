package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.ActivityResult;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class GenerationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> entityAttributes;
    Map<String, String> activityAttributes;
    Map<String, String> generationAttributes;

    public GenerationHandler(KomaduServiceStub stub,
                             Map<String, String> entityAttributes,
                             Map<String, String> activityAttributes,
                             Map<String, String> generationAttributes) {
        this.entityAttributes = entityAttributes;
        this.activityAttributes = activityAttributes;
        this.generationAttributes = generationAttributes;
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

            GenerationType generation = KomaduClientUtils.createGeneration(generationAttributes,
                    entityResult.getEntityId(), activityResult.getActivityId());

            activityEntityType.setActivity(activityResult.getActivity());
            activityEntityType.setEntity(entityResult.getEntity());
            activityEntityType.setGeneration(generation);
            activityEntity.setAddActivityEntityRelationship(activityEntityType);
            // invoke
            stub.addActivityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
