from komdu_python_client.models.models import entityType, fileType, activityType, serviceInformationType, instanceOfType,\
    usageType, activityEntityType


class ModelCreator:
    def create_file_entity(self, filename, file_uri, attributes=None, location=None, created_date=None, owner=None,
                           size=None):
        entity = entityType()
        file = fileType()
        file.fileName = filename
        file.fileURI = file_uri
        if created_date is not None:
            file.createDate = created_date
        if owner is not None:
            file.ownerDN = owner
        if size is not None:
            file.size = size

        entity.file = file
        if location is not None:
            entity.location = location
        if attributes is not None:
            entity.attributes = attributes
        return entity

    def create_workflow_activity(self, workflow_id, node_id, service_id, instance_workflow, instance_version,
                                 instance_creation_time, location, attributes=None):
        activity = activityType()
        activity.location = location

        instance_of = instanceOfType()
        instance_of.creationTime = instance_creation_time
        instance_of.instanceOfID = instance_workflow
        instance_of.version = instance_version

        service_info = serviceInformationType()
        service_info.instanceOf = instance_of
        service_info.serviceID = service_id
        service_info.workflowID = workflow_id
        service_info.workflowNodeID = node_id
        if attributes is not None:
            service_info.attributes = attributes

        activity.serviceInformation = service_info
        return activity

    def addActivityEntity(self, activity, entity, timestamp, activity_id, entity_id):

        relationship = activityEntityType()
        relationship.activity = activity
        relationship.entity = entity

        usage = usageType()
        usage.activityID = activity_id
        usage.entityID = entity_id
        usage.timestamp = timestamp

        relationship.usage = usage
        return relationship
