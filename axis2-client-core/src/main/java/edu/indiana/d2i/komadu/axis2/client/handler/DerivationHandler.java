package edu.indiana.d2i.komadu.axis2.client.handler;

import edu.indiana.d2i.komadu.axis2.client.*;
import edu.indiana.d2i.komadu.axis2.client.result.EntityResult;

import java.util.Map;

public class DerivationHandler implements Runnable {

    KomaduServiceStub stub;
    KomaduClientConstants.Derivation derType;
    Map<String, String> usedAttributes;
    Map<String, String> generatedAttributes;
    Map<String, String> derivationAttributes;

    public DerivationHandler(KomaduServiceStub stub,
                             KomaduClientConstants.Derivation derType,
                             Map<String, String> usedAttributes,
                             Map<String, String> generatedAttributes,
                             Map<String, String> derivationAttributes) {
        this.usedAttributes = usedAttributes;
        this.derType = derType;
        this.generatedAttributes = generatedAttributes;
        this.derivationAttributes = derivationAttributes;
        this.stub = stub;
    }

    @Override
    public void run() {
        try {
            AddEntityEntityRelationshipDocument entityEntity =
                    AddEntityEntityRelationshipDocument.Factory.newInstance();
            EntityEntityType entityEntityType = EntityEntityType.Factory.newInstance();

            EntityResult usedResult = KomaduClientUtils.createEntity(usedAttributes);
            EntityResult generatedResult = KomaduClientUtils.createEntity(generatedAttributes);

            DerivationType derivation = KomaduClientUtils.createDerivation(derType,
                    derivationAttributes, usedResult.getEntityId(), generatedResult.getEntityId());

            entityEntityType.setEntity1(usedResult.getEntity());
            entityEntityType.setEntity2(generatedResult.getEntity());

            if (derivation instanceof RevisionType) {
                entityEntityType.setRevision((RevisionType) derivation);
            } else if (derivation instanceof QuotationType) {
                entityEntityType.setQuotation((QuotationType) derivation);
            } else if (derivation instanceof PrimarySourceType) {
                entityEntityType.setPrimarySource((PrimarySourceType) derivation);
            } else {
                entityEntityType.setDerivation(derivation);
            }

            entityEntity.setAddEntityEntityRelationship(entityEntityType);
            // invoke
            stub.addEntityEntityRelationship(entityEntity);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
