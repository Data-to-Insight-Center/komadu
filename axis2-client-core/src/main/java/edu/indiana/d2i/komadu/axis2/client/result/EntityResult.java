package edu.indiana.d2i.komadu.axis2.client.result;

import edu.indiana.d2i.komadu.axis2.client.EntityType;

public class EntityResult {

    private EntityType entity;
    private String entityId;

    public EntityType getEntity() {
        return entity;
    }

    public void setEntity(EntityType entity) {
        this.entity = entity;
    }

    public String getEntityId() {
        return entityId;
    }

    public void setEntityId(String entityId) {
        this.entityId = entityId;
    }

}
