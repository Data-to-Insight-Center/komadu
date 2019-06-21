import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
import queue


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
    def __init__(self,  event_queue):
        super(EventProcessor, self).__init__()
        self.event_queue = event_queue
        logging.info("Event processor initialized!")
        return

    def run(self):
        while True:
            item = self.event_queue.get()
            self.process_file_event(item)
        return

    def process_file_event(self, event):
        file_path = event.src_path
        event_content = file_path.split("/")
        file_name = event_content[-1]
        username = event_content[4]
        workflow_type = event_content[3]
        log_event = "Processing file: {} from user: {} for the workflow type: {} filepath: {}"
        logging.debug(log_event.format(file_name, username, workflow_type, event_content))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    data_queue = queue.Queue()

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = ExperimentEventHandler(data_queue)

    logging.debug("Starting file polling service!")
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
