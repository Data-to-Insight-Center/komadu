from datetime import datetime
from komadu_client.models.model_creator import ModelCreator
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum

modeler = ModelCreator()
parser = InputParser()


activity = modeler.create_workflow_activity("grayscott_workflow-2", "grayscott-2","grayscott-2", "grayscott_workflow", "1.0.0", datetime.now(), "summit")
result = parser.parse("/Users/swithana/git/komadu/GrayScott/komdu_python_client/samples/input/settings.json", "grayscott")
entity = modeler.create_file_entity("settings.json", "summit/sachith/adios2/settings.json", attributes=result)
relay = modeler.get_activity_entity(activity, entity, datetime.now(), activity.serviceInformation.serviceID, entity.file.fileURI, AssociationEnum.GENERATION)

# todo: can we remove the ns1? and add that automatically?
print(relay.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))


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
import sys
import cmd
import uuid
import os
import time
from docopt import docopt
from lxml import etree

# Communication constants
BASE_EXCHANGE = "KomaduExchange"
BASE_ROUTINGKEY = "KomaduKey"
BASE_QUEUENAME = "KomaduQueue"
CLIENT_ID = "test1"
SAXON_COMMAND = "java -jar samples/visualization/saxon9he.jar -s:output.xml " \
                "-xsl:samples/visualization/xslt/pipeline_xml2csv.xsl"


def execute_command(notify, file):
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # get the content of the file
    data = get_file(arguments['<file>'], notify, CLIENT_ID)

    if notify:
        channel.basic_publish(exchange=BASE_EXCHANGE + '_Notification', routing_key=BASE_ROUTINGKEY + '_Notification',
                              body=data)
    else:
        queue_name = BASE_QUEUENAME + 'QueryResponse'
        channel.queue_bind(exchange=BASE_EXCHANGE + "QueryResponse", queue=queue_name, routing_key=CLIENT_ID)
        channel.basic_publish(exchange=BASE_EXCHANGE + 'QueryRequest', routing_key=BASE_ROUTINGKEY + 'QueryRequest',
                              body=data)
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()

    print("Executed %r" % file)
    connection.close()


def callback(ch, method, properties, body):
    xmlContent = etree.fromstring(body)
    tree = etree.ElementTree(xmlContent)
    root = tree.getroot()
    content = etree.ElementTree(root[0][0])
    content.write('output.xml', pretty_print=True, xml_declaration=True)
    time.sleep(3)
    os.system(SAXON_COMMAND)
    quit()


def get_file(file, notify, client_id):
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
    execute_command(arguments['notify'], arguments['<file>'])