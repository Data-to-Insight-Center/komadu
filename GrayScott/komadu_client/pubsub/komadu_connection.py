#!/usr/bin/env python
"""
Komadu Client.

Usage:
  komadu-client.py notify <file>
  komadu-client.py query <file>

Options:
  -h --help     Show this screen.
"""

import pika
import os
import time
from docopt import docopt
from lxml import etree
from komadu_client.util.constants import BASE_EXCHANGE, BASE_QUEUENAME, BASE_ROUTINGKEY, SAXON_COMMAND, CLIENT_ID
import logging


class KomaduClient:
    """
    The connection client to Komadu using Python via RabbitMQ
    """
    _LOG = logging.getLogger(__name__)

    def __init__(self):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.parameters = pika.ConnectionParameters('localhost',
                                                    5672,
                                                    '/',
                                                    self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def publish_data(self, data):
        logging.debug("publishing :" + data)
        self.channel.basic_publish(exchange=BASE_EXCHANGE + '_Notification',
                                   routing_key=BASE_ROUTINGKEY + '_Notification',
                                   body=data)

    def execute_command(self, notify, file):
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters('localhost',
                                               5672,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        # get the content of the file
        data = self.get_file(arguments['<file>'], notify, CLIENT_ID)

        if notify:
            channel.basic_publish(exchange=BASE_EXCHANGE + '_Notification',
                                  routing_key=BASE_ROUTINGKEY + '_Notification',
                                  body=data)
        else:
            queue_name = BASE_QUEUENAME + 'QueryResponse'
            channel.queue_bind(exchange=BASE_EXCHANGE + "QueryResponse", queue=queue_name, routing_key=CLIENT_ID)
            channel.basic_publish(exchange=BASE_EXCHANGE + 'QueryRequest', routing_key=BASE_ROUTINGKEY + 'QueryRequest',
                                  body=data)
            channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
            channel.start_consuming()

        print("Executed %r" % file)
        connection.close()

    def callback(self, ch, method, properties, body):
        xmlContent = etree.fromstring(body)
        tree = etree.ElementTree(xmlContent)
        root = tree.getroot()
        content = etree.ElementTree(root[0][0])
        content.write('output.xml', pretty_print=True, xml_declaration=True)
        time.sleep(3)
        os.system(SAXON_COMMAND)
        quit()

    def get_file(self, file, notify, client_id):
        in_file = open(file, "rb")
        data = str.encode("")

        # appending the response queue
        if not notify:
            data = str.encode(client_id + "#")
        data += in_file.read()
        in_file.close()
        return data


if __name__ == '__main__':
    arguments = docopt(__doc__, version="1.0")
    client = KomaduClient()
    client.execute_command(arguments['notify'], arguments['<file>'])
