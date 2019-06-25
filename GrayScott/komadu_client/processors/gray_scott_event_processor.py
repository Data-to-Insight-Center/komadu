from datetime import datetime
from komadu_client.models.model_creator import create_workflow_activity, create_file_entity, get_activity_entity, \
    add_attributes_activity
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_INPUT_PARAMS_FILE, \
    GRAYSCOTT_WORKFLOW_VERSION, GRAYSCOTT_NODE1_NAME, CHEETAH_WALLTIME
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum
from komadu_client.util.logger import logger
import logging
from komadu_client.util.util import get_experiment_name, get_node_id
from abc import ABCMeta, abstractmethod

logger = logging.getLogger('codar-komadu-client.GrayScottEventProcessor')


class AbstractEventProcessor:
    """
    This is the abstract class for the event processor.
    Refer to the GrayScottEventProcessor
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_event(self, username, filename, file_extension, file_path, location): raise NotImplementedError()

    def get_wall_time_from_file(self, filename):
        with open(filename) as file:
            return file.readline().strip()

    def get_analysis_name_walltime(self, filename):
        return filename.split(".")[-1]


class GrayScottEventProcessor(AbstractEventProcessor):
    """
    Processes events related to the Gray Scott workflow.
    """

    def __init__(self, komadu_connetion):
        self.parser = InputParser()
        self.client = komadu_connetion

    def process_event(self, username, filename, file_extension, file_path, location):
        workflow_id = get_experiment_name(file_path)
        logger.info("Processing {} !".format(filename))

        if filename.lower() == GRAYSCOTT_INPUT_PARAMS_FILE:
            # settings.json file
            self._process_input_file(filename, file_path, location, workflow_id, username)

        elif CHEETAH_WALLTIME in file_path.lower():
            # process wall times for the workflow
            if GRAYSCOTT_NODE1_NAME in self.get_analysis_name_walltime(file_path):
                add_attributes_type = add_attributes_activity(workflow_id, GRAYSCOTT_NODE1_NAME, "completed_time",
                                                              self.get_wall_time_from_file(file_path))
                self.client.publish_data(
                    add_attributes_type.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))
            else:
                add_attributes_type = add_attributes_activity(workflow_id, self.get_analysis_name_walltime(file_path),
                                                              "completed_time", self.get_wall_time_from_file(file_path))
                self.client.publish_data(
                    add_attributes_type.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))

    def _process_input_file(self, filename, file_path, location, workflow_id, username):
        """
        When the settings.json file is detected. Create the complete workflow in Komadu (User-GS-PDF).
        """
        workflow_node_id = get_node_id(workflow_id, GRAYSCOTT_NODE1_NAME)
        input_params = self.parser.parse(file_path, GRAYSCOTT_WORKFLOW_NAME)
        # create the activity node and the entity node
        activity = create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                            GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,
                                            datetime.now(), location)
        entity = create_file_entity(filename, file_path, location=location, attributes=input_params)
        # create the connection between the activity and the entity
        result = get_activity_entity(activity, entity, datetime.now(),
                                     activity.serviceInformation.serviceID,
                                     entity.file.fileURI, AssociationEnum.GENERATION)
        # todo: fix this ns1
        logger.info("Publishing " + file_path + " to Komadu!")
        logger.debug(result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
        # publish the data to Komadu
        self.client.publish_data(
            result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
