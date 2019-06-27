import unittest
from komadu_client.parsers.fobs_parser import parse_fobs_json
from datetime import datetime


class TestFobsParser(unittest.TestCase):

    def test_fobs_parser_gray_scott(self):
        file_name = "./resources/gray-scott/codar.cheetah.fob.json"
        parsed_result = parse_fobs_json(file_name)

        parsed_result.activity1.serviceInformation.instanceOf.creationTime = datetime(2019, 10, 30, 18, 00)
        parsed_result.activity2.serviceInformation.instanceOf.creationTime = datetime(2019, 10, 30, 18, 00)

        actual = parsed_result.toxml("utf-8", element_name='ns1:addActivityActivityRelationship').decode('utf-8').replace('"', "'")
        expected = "<?xml version='1.0' encoding='utf-8'?><ns1:addActivityActivityRelationship xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:activity1><ns1:serviceInformation><ns1:workflowID>gray-scott</ns1:workflowID><ns1:workflowNodeID>gray-scott-simulation</ns1:workflowNodeID><ns1:attributes><ns1:attribute><ns1:property>node_layout</ns1:property><ns1:value>simulation=2, pdf_calc=1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>nprocs</ns1:property><ns1:value>2</ns1:value></ns1:attribute><ns1:attribute><ns1:property>total_nodes</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>launch_mode</ns1:property><ns1:value>default</ns1:value></ns1:attribute></ns1:attributes><ns1:instanceOf><ns1:instanceOfID>gray-scott</ns1:instanceOfID><ns1:version>1.0.0</ns1:version><ns1:creationTime>2019-10-30T18:00:00</ns1:creationTime></ns1:instanceOf><ns1:serviceID>gray-scott-simulation</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity1><ns1:activity2><ns1:serviceInformation><ns1:workflowID>gray-scott</ns1:workflowID><ns1:workflowNodeID>gray-scott-pdf_calc</ns1:workflowNodeID><ns1:instanceOf><ns1:instanceOfID>gray-scott</ns1:instanceOfID><ns1:version>1.0.0</ns1:version><ns1:creationTime>2019-10-30T18:00:00</ns1:creationTime></ns1:instanceOf><ns1:serviceID>gray-scott-pdf_calc</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity2><ns1:communication><ns1:informedActivityID>gray-scott-pdf_calc</ns1:informedActivityID><ns1:informantActivityID>gray-scott-simulation</ns1:informantActivityID></ns1:communication></ns1:addActivityActivityRelationship>"
        self.assertEqual(expected, actual, msg="Error in the fobs parser output for gray-scott")

    def test_fobs_parser_brusselator(self):
        file_name = "./resources/brusselator/codar.cheetah.fobs.json"
        parsed_result = parse_fobs_json(file_name)

        parsed_result.activity1.serviceInformation.instanceOf.creationTime = datetime(2019, 10, 30, 18, 00)
        parsed_result.activity2.serviceInformation.instanceOf.creationTime = datetime(2019, 10, 30, 18, 00)

        actual = parsed_result.toxml("utf-8", element_name='ns1:addActivityActivityRelationship').decode('utf-8').replace('"', "'")
        expected = "<?xml version='1.0' encoding='utf-8'?><ns1:addActivityActivityRelationship xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:activity1><ns1:serviceInformation><ns1:workflowID>brusselator</ns1:workflowID><ns1:workflowNodeID>brusselator-simulation</ns1:workflowNodeID><ns1:attributes><ns1:attribute><ns1:property>node_layout</ns1:property><ns1:value>simulation=2, norm_calc=1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>nprocs</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>total_nodes</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>launch_mode</ns1:property><ns1:value>default</ns1:value></ns1:attribute></ns1:attributes><ns1:instanceOf><ns1:instanceOfID>brusselator</ns1:instanceOfID><ns1:creationTime>2019-10-30T18:00:00</ns1:creationTime></ns1:instanceOf><ns1:serviceID>brusselator-simulation</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity1><ns1:activity2><ns1:serviceInformation><ns1:workflowID>brusselator</ns1:workflowID><ns1:workflowNodeID>brusselator-norm_calc</ns1:workflowNodeID><ns1:instanceOf><ns1:instanceOfID>brusselator</ns1:instanceOfID><ns1:creationTime>2019-10-30T18:00:00</ns1:creationTime></ns1:instanceOf><ns1:serviceID>brusselator-norm_calc</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity2><ns1:communication><ns1:informedActivityID>brusselator-norm_calc</ns1:informedActivityID><ns1:informantActivityID>brusselator-simulation</ns1:informantActivityID></ns1:communication></ns1:addActivityActivityRelationship>"
        self.assertEqual(expected, actual, msg="Error in the fobs parser output for Brusselator")


if __name__ == '__main__':
    unittest.main()
