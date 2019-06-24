from komadu_client.models.model_creator import ModelCreator
from datetime import datetime
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_INPUT_PARAMS_FILE, \
    GRAYSCOTT_WORKFLOW_VERSION
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum
import logging


class GrayScottEventProcessor:
    """
    Processes events related to the Gray Scott workflow.
    """
    _LOG = logging.getLogger(__name__)

    def __init__(self, komadu_connetion):
        self.modeler = ModelCreator()
        self.parser = InputParser()
        self.client = komadu_connetion

    def process_event(self, username, filename, file_extension, file_path, location):
        # todo: parse the workflow ID (expriment ID)
        workflow_id = "grayscott_workflow-30"
        workflow_node_id = "grayscott-30"

        if filename.lower() == GRAYSCOTT_INPUT_PARAMS_FILE:
            self._process_input_file(file_path, location, workflow_id, workflow_node_id)

    def _process_input_file(self, file_path, location, workflow_id, workflow_node_id):
        input_params = self.parser.parse(file_path, GRAYSCOTT_WORKFLOW_NAME)
        activity = self.modeler.create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                                         GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,
                                                         datetime.now(), location)
        entity = self.modeler.create_file_entity("settings.json", "summit/sachith/adios2/settings.json",
                                                 attributes=input_params)
        result = self.modeler.get_activity_entity(activity, entity, datetime.now(),
                                                  activity.serviceInformation.serviceID,
                                                  entity.file.fileURI, AssociationEnum.GENERATION)
        # todo: fix this ns1
        logging.info("Publishing " + file_path + " to Komadu!")
        print(result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
        self.client.publish_data(
            result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))

    def get_workflow_node(self, filename, location, workflow_id, workflow_node_id):
        """
        Generate the Grayscott workflow node
        :param filename:
        :param location:
        :return:
        """

        return self.modeler.create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                                     GRAYSCOTT_WORKFLOW_NAME,
                                                     GRAYSCOTT_WORKFLOW_VERSION, datetime.now(), location)

    def create_file_entity(self, filename, file_uri, attributes=None):
        return self.modeler.create_file_entity(filename, file_uri, attributes)