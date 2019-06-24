from komadu_client.models.model_creator import ModelCreator
from datetime import datetime
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_INPUT_PARAMS_FILE, \
    GRAYSCOTT_WORKFLOW_VERSION, GRAYSCOTT_NODE1_NAME
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum
from komadu_client.util.logger import logger
import logging
from komadu_client.util.util import get_experiment_name
from abc import ABCMeta, abstractmethod


logger = logging.getLogger('codar-komadu-client.GrayScottEventProcessor')


class AbstractEventProcessor:
    """
    This is the abstract class for the event processor.
    Refer to the GrayScottEventProcessor
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_event(self, username, filename, file_extension, file_path, location): return


class GrayScottEventProcessor(AbstractEventProcessor):
    """
    Processes events related to the Gray Scott workflow.
    """

    def __init__(self, komadu_connetion):
        self.modeler = ModelCreator()
        self.parser = InputParser()
        self.client = komadu_connetion

    def process_event(self, username, filename, file_extension, file_path, location):
        workflow_id = get_experiment_name(file_path)

        if filename.lower() == GRAYSCOTT_INPUT_PARAMS_FILE:
            self._process_input_file(filename, file_path, location, workflow_id, username)

    def _process_input_file(self, filename, file_path, location, workflow_id, username):
        """
        When the settings.json file is detected. Create the complete workflow in Komadu (User-GS-PDF).
        """
        workflow_node_id = workflow_id + "-" + GRAYSCOTT_NODE1_NAME
        input_params = self.parser.parse(file_path, GRAYSCOTT_WORKFLOW_NAME)
        activity = self.modeler.create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                                         GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,
                                                         datetime.now(), location)
        entity = self.modeler.create_file_entity(filename, file_path, location=location, attributes=input_params)
        result = self.modeler.get_activity_entity(activity, entity, datetime.now(),
                                                  activity.serviceInformation.serviceID,
                                                  entity.file.fileURI, AssociationEnum.GENERATION)
        # todo: fix this ns1
        logger.info("Publishing " + file_path + " to Komadu!")
        logger.debug(result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
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
