from komadu_client.models.ingest_models import entityType, fileType, activityType, serviceInformationType, \
    instanceOfType, \
    usageType, activityEntityType, generationType, addAttributesType
from komadu_client.util.association_enums import AssociationEnum
from komadu_client.util.util import get_node_id, get_attributes
from datetime import datetime

def create_file_entity(filename, file_uri, attributes=None, location=None, created_date=None, owner=None,
                       size=None):
    entity = entityType()
    file = fileType()
    file.fileName = filename
    file.fileURI = "file: " + str(file_uri)
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


def create_workflow_activity(workflow_id, node_id, service_id, instance_workflow, instance_version,
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


def get_activity_entity(self, activity, entity, timestamp, activity_id, entity_id, type=AssociationEnum.USAGE,
                        attributes=None):
    relationship = activityEntityType()
    relationship.activity = activity
    relationship.entity = entity

    if type is AssociationEnum.GENERATION:
        generation = generationType()
        self.__populate_relation(activity_id, entity_id, generation, timestamp, attributes)
        relationship.generation = generation
    elif type is AssociationEnum.USAGE:
        usage = usageType()
        self.__populate_relation(activity_id, entity_id, usage, timestamp, attributes)
        relationship.usage = usage

    return relationship


def __populate_relation(activity_id, entity_id, relation, timestamp, attributes=None):
    relation.activityID = activity_id
    relation.entityID = entity_id
    relation.timestamp = timestamp
    if attributes is not None:
        relation.attributes = attributes


def add_attributes_activity(workflow_id, node_id, key, value):
    workflow_node_id = get_node_id(workflow_id, node_id)

    new_attr_doc = addAttributesType()
    new_attr_doc.objectID = workflow_node_id
    new_attr_doc.objectType = "ACTIVITY"
    new_attr_doc.notificationTimestamp = datetime.now()
    new_attributes = {key: value}
    new_attr_doc.attributes = get_attributes(new_attributes)
    return new_attr_doc
