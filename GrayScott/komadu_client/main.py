#!/usr/bin/env python
"""
A standalone Komadu connector that sends the notifications to Komadu via filesystem reading.

Usage:
  komaduConnect [--polling | --static] --workflow_type=<workflow_name> --user=<user_name> --machine=<machine_name> <location>

Options:
  -h --help             Show this screen.
  --polling             Start the connector in the polling mode (looks for file creations in real-time)
  --static              Start the connector in static mode (reads the current files and processes them)
  --workflow_type=<workflow_name>     Type of the workflow (ex: gray-scott)
  --user=<user_name>    Name of the user running the application
  --machine=<machine_name> Name of the machine where it's running at
  <location>            Directory of which to extract the data from
"""
import os
import time
import logging
import glob
from docopt import docopt
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
        dir = event.is_directory
        if not dir:
            self.event_queue.put(event)


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
        self.komadu_conn = KomaduClient()
        # setting up the correct workflow processor
        if GRAYSCOTT_WORKFLOW in self.workflow_name:
            self.processor = GrayScottEventProcessor(self.komadu_conn, self.machine, self.username)
        elif BRUSSELATOR_WORKFLOW_NAME in self.workflow_name:
            self.processor = BrusselatorEventProcessor(self.komadu_conn, self.machine, self.username)
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
            activity_activity = parse_fobs_json(file_path).toxml("utf-8",
                                                                 element_name='ns1:addActivityActivityRelationship').decode(
                'utf-8').replace('"', "'")
            self.komadu_conn.publish_data(activity_activity)

        self.processor.process_event(filename, file_extension, file_path)


def process_polling(path, workflow_name, machine, user):
    data_queue = queue.Queue()
    event_handler = ExperimentEventHandler(data_queue)

    logger.info("Starting file polling service!")
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    event_processor = EventProcessor(data_queue, workflow_name, machine, user)
    event_processor.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def process_static(path, workflow_name, machine, user):
    data_queue = queue.Queue()
    event_processor = EventProcessor(data_queue, workflow_name, machine, user)
    files = glob.glob(path + os.sep + "**", recursive=True)
    #
    # fob_json_list = []
    # for i in range(len(files)):
    #     if FOBS_FILE in files[i]:
    #         fob_json_list.append(files[i])
    #
    # if len(fob_json_list):
    #     for fob_file in fob_json_list:
    #         print("Processing... {}".format(fob_file))
    #         files.remove(fob_file)
    #         files.insert(0, fob_file)
    #
    # print(files)
    for file in files:
        event_processor.process_file_event(file)


if __name__ == "__main__":
    arguments = docopt(__doc__, version="1.0")

    if not arguments['--polling']:
        process_static(arguments["<location>"], arguments["--workflow_type"], arguments["--machine"], arguments["--user"])
    else:
        process_polling(arguments["<location>"], arguments["--workflow_type"],  arguments["--machine"], arguments["--user"])
