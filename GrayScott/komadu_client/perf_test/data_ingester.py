from komadu_client.util.util import get_experiment_name, get_workflow_name, get_attributes, get_node_id, \
    get_workflow_version
from komadu_client.models.model_creator import create_workflow_activity
from datetime import datetime
from komadu_client.models.ingest_models import activityActivityType, communicationType
from komadu_client.pubsub.komadu_connection import KomaduClient
from komadu_client.models.model_creator import create_workflow_activity, create_file_entity, get_activity_entity, get_attributes
from komadu_client.util.association_enums import AssociationEnum
import logging

komadu_conn = KomaduClient()
logger = logging.getLogger('codar-komadu-client.EventProcessor')


def send_workflow_instance_prov(username, machine, campaign_id, workflow_name, workflow_version, experiment, run, sim_node, analysis_node, workflow_attributes=None):
    workflow_id = get_workflow_id(username, campaign_id, experiment, run)

    # publishing a two node workflow
    send_workflow(machine, workflow_id, workflow_name, workflow_version, sim_node, analysis_node, workflow_attributes)

    # publishing input-workflow relationship
    send_input_file(sim_node, workflow_id, workflow_name, workflow_version, username, machine, filename=None)


def send_workflow(machine, workflow_id, workflow_name, workflow_version, sim_node, analysis_node, workflow_attributes=None):
    if not workflow_attributes:
        workflow_attributes = {
            "nprocs": 2
        }

    # Creating the input workflow
    simulation_node = create_workflow_activity(workflow_id, get_node_id(workflow_id, ""),
                                               get_node_id(workflow_id, sim_node),
                                               workflow_name, workflow_version, datetime.now(),
                                               machine, attributes=get_attributes(workflow_attributes))
    # todo: support more than two nodes
    analysis_node = create_workflow_activity(workflow_id, get_node_id(workflow_id, analysis_node),
                                             get_node_id(workflow_id, analysis_node), workflow_name,
                                             workflow_version, datetime.now(), machine)

    workflow_graph = get_activity_activity_type(simulation_node, analysis_node).toxml("utf-8",
                                                                 element_name='ns1:addActivityActivityRelationship').decode(
                'utf-8').replace('"', "'")
    komadu_conn.publish_data(workflow_graph)


def send_input_file(sim_node, workflow_id, workflow_name, workflow_version, username, machine, filename="inputFile"):
    """
    Sends the input file attached to the first node (sim node) of the workflow
    :param sim_node:
    :param workflow_id:
    :param workflow_name:
    :param workflow_version:
    :param username:
    :param machine:
    :param filename:
    :return:
    """
    workflow_node_id = get_node_id(workflow_id, sim_node)
    location = get_input_location(machine, username, workflow_id)

    # create the activity node and the entity node
    activity = create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                        workflow_name, workflow_version,
                                        datetime.now(), location)
    entity = create_file_entity(filename, workflow_id + "-input_file", location=location,
                                owner=username)
    # create the connection between the activity and the entity
    result = get_activity_entity(activity, entity, datetime.now(),
                                 activity.serviceInformation.serviceID,
                                 entity.file.fileURI, AssociationEnum.USAGE)
    logger.info("Publishing " + location + " to Komadu!")
    publish_activity_entity_relationship(result)


def get_activity_activity_type(node1, node2):
    model = activityActivityType()
    model.activity1 = node1
    model.activity2 = node2
    comm = communicationType()
    comm.informantActivityID = node1.serviceInformation.serviceID
    comm.informedActivityID = node2.serviceInformation.serviceID
    model.communication = comm
    return model


def get_input_location(machine, username, workflow_id):
    return machine + "://" + "home/" + username + "/" + workflow_id + "/input_file"


def publish_activity_entity_relationship(self, result):
    # publish the data to Komadu
    komadu_conn.publish_data(
        result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))


def get_workflow_id(username, campaign_id, experiment, run):
    return username + "_" + campaign_id + "_" + experiment + "_" + run
