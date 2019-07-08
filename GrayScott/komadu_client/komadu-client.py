#!/usr/bin/env python
"""
A standalone Komadu Client which uses xml files as input to query/notify Komadu.

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
        channel.exchange_declare(BASE_EXCHANGE + "QueryResponse", "direct")
        channel.queue_declare(queue_name)
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