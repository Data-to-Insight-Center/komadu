from datetime import datetime
from komadu_client.models.model_creator import ModelCreator
from komadu_client.parsers.input_parser import InputParser
from komadu_client.util.association_enums import AssociationEnum

modeler = ModelCreator()
parser = InputParser()


activity = modeler.create_workflow_activity("grayscott_workflow-2", "grayscott-2","grayscott-2", "grayscott_workflow", "1.0.0", datetime.now(), "summit")
result = parser.parse("/Users/swithana/git/komadu/GrayScott/komdu_python_client/samples/input/settings.json", "grayscott")
entity = modeler.create_file_entity("settings.json", "summit/sachith/adios2/settings.json", attributes=result)
relay = modeler.add_activity_entity(activity, entity, datetime.now(), activity.serviceInformation.serviceID, entity.file.fileURI, AssociationEnum.GENERATION)

# todo: can we remove the ns1? and add that automatically?
print(relay.toxml("utf-8", element_name='ns1:addActivityEntityRelationship').decode('utf-8'))

