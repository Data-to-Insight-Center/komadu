from datetime import datetime
from komadu_client.models.model_creator import create_workflow_activity, create_file_entity, get_activity_entity, \
    add_attributes_activity, get_attributes
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_INPUT_PARAMS_FILE, STATUS_JSON, \
    GRAYSCOTT_WORKFLOW_VERSION, SIMULATION_NODE_NAME, CHEETAH_WALLTIME, SIMULATION_STD_ERR, \
    SIMULATION_STDOUT, GRAYSCOTT_OUTPUT_FILE, BRUSSELATOR_WORKFLOW_NAME, BRUSSELATOR_WORKFLOW_VERSION
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum
from komadu_client.util.logger import logger
import logging
from komadu_client.util.util import get_experiment_name, get_node_id, parse_json_file, flatten_dict
from abc import ABCMeta, abstractmethod
from os import path, sep

logger = logging.getLogger('codar-komadu-client.EventProcessor')


class AbstractEventProcessor:
    """
    This is the abstract class for the event processor.
    Refer to the GrayScottEventProcessor
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_event(self, username, filename, file_extension, file_path, location):
        raise NotImplementedError()

    def update_statuses(self, file, workflow_id):
        """
        Update the status of the workflow completion (successful/failed)
        :param file:
        :param workflow_id:
        :return:
        """
        # get the status file from the directory above
        status_file = path.dirname(path.dirname(file)) + sep + STATUS_JSON
        logger.info("Processing the status file: " + status_file)
        data = parse_json_file(status_file)
        for run in data:
            if run in workflow_id:
                attributes = get_attributes(flatten_dict(data[run]))
                activity_update = add_attributes_activity(workflow_id, SIMULATION_NODE_NAME, None, None,
                                                          attributes=attributes)
                self.client.publish_data(
                    activity_update.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8'))

    def process_workflow_completion(self, file_path, location, workflow_id, workflow_name, workflow_version):
        """
        Gets triggered when the walltime files are created in Codar.
        :param file_path:
        :param location:
        :param workflow_id:
        :param workflow_name:
        :param workflow_version:
        :return:
        """
        # add the completion times for the workflow
        self.process_workflow_completion_times(file_path, workflow_id)
        logger.info("Processing {} !".format(file_path))
        workflow_node_id = get_node_id(workflow_id, SIMULATION_NODE_NAME)
        activity = create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                            workflow_name, workflow_version,
                                            datetime.now(), location)
        self.process_std_out(file_path, activity, workflow_node_id)
        logger.info("Processing std out/error")

    def get_wall_time_from_file(self, filename):
        with open(filename) as file:
            return file.readline().strip()

    def get_file_extension(self, filename):
        return filename.split(".")[-1]

    def process_workflow_completion_times(self, file_path, workflow_id):
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

            # process the final statuses file (codar.workflow.status.json)
            self.update_statuses(file_path, workflow_id)

    def process_std_out(self, file_path, activity, activity_id):
        """
        Processes the standard output and error and sends to Komadu
        :param file_path:
        :param activity: in ActivityType
        :param activity_id: id of the activity
        :return:
        """
        std_out = path.dirname(file_path) + sep + SIMULATION_STDOUT
        std_err = path.dirname(file_path) + sep + SIMULATION_STD_ERR
        # with open(std_out) as f1:
        #     out_file_content = f1.read()
        #
        # with open(std_err) as f2:
        #     err_file_content = f2.read()
        #
        # std_out_attributes = get_attributes({"content": out_file_content})
        # std_err_attributes = get_attributes({"content": err_file_content})

        stdout_entity = create_file_entity("std-out", activity_id + "-stdout", location=str(std_out))
        stderr_entity = create_file_entity("std-err", activity_id + "-stderr", location=str(std_err))
        activity_entity_stdout = get_activity_entity(activity, stdout_entity, datetime.now(), activity_id,
                                                     stdout_entity.file.fileURI, AssociationEnum.GENERATION)
        activity_entity_stderr = get_activity_entity(activity, stderr_entity, datetime.now(), activity_id,
                                                     stderr_entity.file.fileURI, AssociationEnum.GENERATION)
        self.client.publish_data(
            activity_entity_stderr.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
        self.client.publish_data(
            activity_entity_stdout.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))


class GrayScottEventProcessor(AbstractEventProcessor):
    """
    Processes events related to the Gray Scott workflow.
    """

    def __init__(self, komadu_connetion):
        self.parser = InputParser()
        self.client = komadu_connetion

    def process_event(self, username, filename, file_extension, file_path, location):
        workflow_id = get_experiment_name(file_path)

        if filename.lower() == GRAYSCOTT_INPUT_PARAMS_FILE:
            # settings.json file
            logger.info("Processing {} !".format(filename))
            self._process_input_file(filename, file_path, location, workflow_id, username)

        elif self.get_file_extension(file_path.lower()) == "txt":
            # skip .txt files
            pass
        elif filename.lower() == GRAYSCOTT_OUTPUT_FILE:
            # gs.bp
            logger.info("Processing {} !".format(filename))
            self._process_output_file(filename, file_path, location, workflow_id, username)
        elif CHEETAH_WALLTIME in file_path.lower():
            self.process_workflow_completion(file_path, location, workflow_id, GRAYSCOTT_WORKFLOW_NAME,
                                             GRAYSCOTT_WORKFLOW_VERSION)

    def _process_input_file(self, filename, file_path, location, workflow_id, username):
        """
        When the settings.json file is detected add that to the provenance
        """
        workflow_node_id = get_node_id(workflow_id, SIMULATION_NODE_NAME)
        input_params = self.parser.parse(file_path, GRAYSCOTT_WORKFLOW_NAME)
        # create the activity node and the entity node
        activity = create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                            GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,
                                            datetime.now(), location)
        entity = create_file_entity(filename, workflow_id + "-" + filename, location=file_path, attributes=input_params,
                                    owner=username)
        # create the connection between the activity and the entity
        result = get_activity_entity(activity, entity, datetime.now(),
                                     activity.serviceInformation.serviceID,
                                     entity.file.fileURI, AssociationEnum.USAGE)
        logger.info("Publishing " + file_path + " to Komadu!")
        self._publish_activity_entity_relationship(result)

    def _process_output_file(self, filename, file_path, location, workflow_id, username):
        """
        When the gs.bp is detected add that to the workflow (simulation -> gs.bp)
        """
        workflow_node_id = get_node_id(workflow_id, SIMULATION_NODE_NAME)
        # create the activity node and the entity node
        activity = create_workflow_activity(workflow_id, workflow_node_id, workflow_node_id,
                                            GRAYSCOTT_WORKFLOW_NAME, GRAYSCOTT_WORKFLOW_VERSION,
                                            datetime.now(), location)
        entity = create_file_entity(filename, workflow_id + "-" + filename, location=file_path, owner=username)
        # create the connection between the activity and the entity
        result = get_activity_entity(activity, entity, datetime.now(),
                                     activity.serviceInformation.serviceID,
                                     entity.file.fileURI, AssociationEnum.GENERATION)
        logger.info("Publishing " + file_path + " to Komadu!")
        self._publish_activity_entity_relationship(result)

    def _publish_activity_entity_relationship(self, result):
        # todo: fix this ns1
        logger.debug(result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))
        # publish the data to Komadu
        self.client.publish_data(
            result.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))


class BrusselatorEventProcessor(AbstractEventProcessor):
    """
    Processes events related to the Brusselator workflow.
    """

    def __init__(self, komadu_connetion):
        self.parser = InputParser()
        self.client = komadu_connetion

    def process_event(self, username, filename, file_extension, file_path, location):
        workflow_id = get_experiment_name(file_path)
        logger.info("Processing {} !".format(filename))

        if self.get_file_extension(file_path.lower()) == "txt":
            # skip .txt files
            pass
        elif CHEETAH_WALLTIME in file_path.lower():
            self.process_workflow_completion(file_path, location, workflow_id, BRUSSELATOR_WORKFLOW_NAME,
                                             BRUSSELATOR_WORKFLOW_VERSION)
