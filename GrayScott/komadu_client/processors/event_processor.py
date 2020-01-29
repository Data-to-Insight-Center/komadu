import os
import threading

from komadu_client.parsers.fobs_parser import parse_fobs_json
from komadu_client.graphdb.dbConnect import Database
from komadu_client.util.logger import logger
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW, FOBS_FILE, BRUSSELATOR_WORKFLOW_NAME
from komadu_client.pubsub.komadu_connection import KomaduClient
from komadu_client.processors.codar_event_processor import GrayScottEventProcessor, BrusselatorEventProcessor
import logging

logger = logging.getLogger("codar.komadu.client.EventProcessor")


class EventProcessor(threading.Thread):
    """
    This classes processes all the events and redirects the events to the correct event processor.
    ex: Grayscott events are processed by GrayScott event processor
    """

    def __init__(self, event_queue, workflow_name, machine, username):
        super(EventProcessor, self).__init__()
        self.event_queue = event_queue
        logger.info("Event processor initialized!")
        self.workflow_name = workflow_name
        self.machine = machine
        self.username = username

        # todo: read this from a property file
        graph_db_uri = "bolt://localhost:7687"
        graph_db_username = "neo4j"
        graph_db_password = "root"

        self.graphdb = Database(graph_db_uri, graph_db_username, graph_db_password)
        # self.komadu_conn = KomaduClient()
        self.komadu_conn = None
        # setting up the correct workflow processor
        if GRAYSCOTT_WORKFLOW in self.workflow_name:
            self.processor = GrayScottEventProcessor(self.komadu_conn, self.graphdb, self.machine, self.username)
        elif BRUSSELATOR_WORKFLOW_NAME in self.workflow_name:
            self.processor = BrusselatorEventProcessor(self.komadu_conn, self.graphdb, self.machine, self.username)
        return

    def run(self):
        while True:
            item = self.event_queue.get()
            self.process_file_event(item.src_path)
        return

    def process_file_event(self, file_path):
        event_content = file_path.split("/")
        filename = event_content[-1]
        file_extension = os.path.splitext(filename)[1]

        if str(filename).startswith("."):
            # ignore files starting with a '.'
            return

        # todo get the machine
        log_event = "Processing file: {} filepath: {} workflow_type {}"
        logger.debug(log_event.format(filename, file_path, self.workflow_name))

        if FOBS_FILE in file_path:
            logger.info("Processing the fobs file: {}".format(file_path))
            # init the workflow using the fobs.json file
            activity_activity, graph_query = parse_fobs_json(file_path)
            # activity_activity = activity_activity.toxml("utf-8", element_name='ns1:addActivityActivityRelationship').decode(
            #     'utf-8').replace('"', "'")
            # self.komadu_conn.publish_data(activity_activity)

            logger.info("Publishing the graph to the database")
            self.graphdb.run_fobs_init_graph_query(graph_query)

        self.processor.process_event(filename, file_extension, file_path)
