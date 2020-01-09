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
from komadu_client.processors.event_processor import EventProcessor
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import queue
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
