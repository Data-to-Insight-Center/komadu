from datetime import datetime
from komadu_client.models.model_creator import create_workflow_activity, create_file_entity, get_activity_entity, \
    add_attributes_activity, get_attributes
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_INPUT_PARAMS_FILE, \
    GRAYSCOTT_WORKFLOW_VERSION, SIMULATION_NODE_NAME, CHEETAH_WALLTIME, STATUS_JSON
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum
from komadu_client.util.logger import logger
import logging
from komadu_client.util.util import get_experiment_name, get_node_id, parse_json_file, flatten_dict
from abc import ABCMeta, abstractmethod
from os import path, sep
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

    def get_file_extension(self, filename):
        return filename.split(".")[-1]

    def process_experiment_completion(self, file_path, workflow_id):
        # process wall times for the workflow
        if SIMULATION_NODE_NAME in self.get_file_extension(file_path):
            add_attributes_type = add_attributes_activity(workflow_id, SIMULATION_NODE_NAME, "completed_time",
                                                          self.get_wall_time_from_file(file_path))
            self.client.publish_data(
                add_attributes_type.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))
        else:
            add_attributes_type = add_attributes_activity(workflow_id, self.get_file_extension(file_path),
                                                          "completed_time", self.get_wall_time_from_file(file_path))
            self.client.publish_data(
                add_attributes_type.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))
            self.update_statuses(file_path, workflow_id)


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

        elif self.get_file_extension(file_path.lower()) == "txt":
            # skip .txt files
            pass
        elif CHEETAH_WALLTIME in file_path.lower():
            self.process_experiment_completion(file_path, workflow_id)

    def _process_input_file(self, filename, file_path, location, workflow_id, username):
        """
        When the settings.json file is detected. Create the complete workflow in Komadu (User-GS-PDF).
        """
        workflow_node_id = get_node_id(workflow_id, SIMULATION_NODE_NAME)
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

    def update_statuses(self, file, workflow_id):
        # get the status file from the directory above
        status_file = path.dirname(path.dirname(file)) + sep + STATUS_JSON
        logger.info("########## Processing the status file: " + status_file)
        data = parse_json_file(status_file)
        for run in data:
            if run in workflow_id:
                attributes = get_attributes(flatten_dict(data[run]))
                activity_update = add_attributes_activity(workflow_id, SIMULATION_NODE_NAME, None, None, attributes=attributes)
                self.client.publish_data(activity_update.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))
