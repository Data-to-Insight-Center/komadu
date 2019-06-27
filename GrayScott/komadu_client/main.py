import sys
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import queue
from komadu_client.util.constants import GRAYSCOTT_WORKFLOW, FOBS_FILE, BRUSSELATOR_WORKFLOW_NAME
from komadu_client.pubsub.komadu_connection import KomaduClient
from komadu_client.processors.codar_event_processor import GrayScottEventProcessor, BrusselatorEventProcessor
from komadu_client.parsers.fobs_parser import parse_fobs_json
from komadu_client.util.logger import logger

logger = logging.getLogger("codar.komadu.client.Main")


class ExperimentEventHandler(FileSystemEventHandler):
    """
    Handler class for detecting and processing the new files created in the polling directory.
    """

    def __init__(self, event_queue):
        self.event_queue = event_queue

    def on_created(self, event):
        file = event.is_directory
        if not file:
            self.event_queue.put(event)


class EventProcessor(threading.Thread):
    """
    This classes processes all the events and redirects the events to the correct event processor.
    ex: Grayscott events are processed by GrayScott event processor
    """

    def __init__(self, event_queue):
        super(EventProcessor, self).__init__()
        self.event_queue = event_queue
        logger.info("Event processor initialized!")
        self.komadu_conn = KomaduClient()
        self.grayscott_processor = GrayScottEventProcessor(self.komadu_conn)
        self.brusselator_processor = BrusselatorEventProcessor(self.komadu_conn)
        return

    def run(self):
        while True:
            item = self.event_queue.get()
            self.process_file_event(item)
        return

    def process_file_event(self, event):
        file_path = event.src_path
        event_content = file_path.split("/")
        filename = event_content[-1]
        file_extension = os.path.splitext(filename)[1]
        username = event_content[4]
        workflow_type = event_content[3]

        if str(filename).startswith("."):
            # ignore files starting with a '.'
            return

        # todo get the location
        username = "swithana"
        location = "summit"
        log_event = "Processing file: {} filepath: {} workflow_type {}"
        logger.debug(log_event.format(filename, file_path, workflow_type))

        if FOBS_FILE in file_path:
            logger.info("Processing the fobs file: {}".format(file_path))
            # init the workflow using the fobs.json file
            activity_activity = parse_fobs_json(file_path).toxml("utf-8",
                                                                 element_name='ns1:addActivityActivityRelationship').decode(
                'utf-8').replace('"', "'")
            self.komadu_conn.publish_data(activity_activity)

        elif GRAYSCOTT_WORKFLOW in file_path:
            self.grayscott_processor.process_event(username, filename, file_extension, file_path, location)

        elif BRUSSELATOR_WORKFLOW_NAME in file_path:
            self.grayscott_processor.process_event(username, filename, file_extension, file_path, location)


if __name__ == "__main__":
    data_queue = queue.Queue()

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = ExperimentEventHandler(data_queue)

    logger.info("Starting file polling service!")
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    event_processor = EventProcessor(data_queue)
    event_processor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
