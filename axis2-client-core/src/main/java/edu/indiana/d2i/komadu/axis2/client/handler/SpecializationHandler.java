package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class SpecializationHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> specificAttributes;
    Map<String, String> generalAttributes;

    public SpecializationHandler(KomaduServiceStub stub,
                                 Map<String, String> specificAttributes,
                                 Map<String, String> generalAttributes) {
        this.specificAttributes = specificAttributes;
        this.generalAttributes = generalAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddEntityEntityRelationshipDocument activityEntity =
                    AddEntityEntityRelationshipDocument.Factory.newInstance();
            EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

            EntityResult specificResult = KomaduClientUtils.createEntity(specificAttributes);
            EntityResult generalResult = KomaduClientUtils.createEntity(generalAttributes);
            SpecializationType specialization = SpecializationType.Factory.newInstance();
            specialization.setSpecificEntityID(specificResult.getEntityId());
            specialization.setGeneralEntityID(generalResult.getEntityId());

            entityEntityType.setEntity1(specificResult.getEntity());
            entityEntityType.setEntity2(generalResult.getEntity());
            entityEntityType.setSpecialization(specialization);
            activityEntity.setAddEntityEntityRelationship(entityEntityType);
            // invoke
            stub.addEntityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
