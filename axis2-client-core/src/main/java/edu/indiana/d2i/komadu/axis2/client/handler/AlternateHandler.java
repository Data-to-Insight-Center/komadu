package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class AlternateHandler implements Runnable {

    KomaduServiceStub stub;
    Map<String, String> alt1Attributes;
    Map<String, String> alt2Attributes;

    public AlternateHandler(KomaduServiceStub stub,
                            Map<String, String> alt1Attributes,
                            Map<String, String> alt2Attributes) {
        this.alt1Attributes = alt1Attributes;
        this.alt2Attributes = alt2Attributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddEntityEntityRelationshipDocument activityEntity =
                    AddEntityEntityRelationshipDocument.Factory.newInstance();
            EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

            EntityResult alt1Result = KomaduClientUtils.createEntity(alt1Attributes);
            EntityResult alt2Result = KomaduClientUtils.createEntity(alt2Attributes);
            AlternateType alternate = AlternateType.Factory.newInstance();
            alternate.setAlternate1ID(alt1Result.getEntityId());
            alternate.setAlternate2ID(alt2Result.getEntityId());

            entityEntityType.setEntity1(alt1Result.getEntity());
            entityEntityType.setEntity2(alt2Result.getEntity());
            entityEntityType.setAlternate(alternate);
            activityEntity.setAddEntityEntityRelationship(entityEntityType);
            // invoke
            stub.addEntityEntityRelationship(activityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}

