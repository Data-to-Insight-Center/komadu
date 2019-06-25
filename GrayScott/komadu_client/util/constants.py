# Communication constants for Komadu
BASE_EXCHANGE = "KomaduExchange"
BASE_ROUTINGKEY = "KomaduKey"
BASE_QUEUENAME = "KomaduQueue"
CLIENT_ID = "test1"
SAXON_COMMAND = "java -jar samples/visualization/saxon9he.jar -s:output.xml " \
                "-xsl:samples/visualization/xslt/pipeline_xml2csv.xsl"

# RabbitMQ settings
RABBITMQ_USERNAME = "guest"
RABBITMQ_PWD = "guest"
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_PATH = "/"


# Grayscott constants
GRAYSCOTT_WORKFLOW = "gray-scott"
GRAYSCOTT_WORKFLOW_NAME = "grayscott"
GRAYSCOTT_NODE1_NAME = "simulation"
GRAYSCOTT_INPUT_PARAMS_FILE = "settings.json"
GRAYSCOTT_WORKFLOW_VERSION = "1.0.0"


CHEETAH_WALLTIME = "walltime"