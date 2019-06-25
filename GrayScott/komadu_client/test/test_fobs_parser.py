import unittest
from komadu_client.parsers.fobs_parser import parse_fobs_json


class TestFobsParser(unittest.TestCase):

    def test_fobs_parser(self):
        file_name = "./resources/gray-scott/codar.cheetah.fob.json"
        parsed_result = parse_fobs_json(file_name).toxml("utf-8", element_name='ns1:addActivityActivityRelationship')\
            .decode('utf-8').replace('"', "'")
        #expected = "<?xml version='1.0' encoding='utf-8'?><ns1:addActivityActivityRelationship xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:activity1><ns1:serviceInformation><ns1:workflowID>gray-scott</ns1:workflowID><ns1:workflowNodeID>gray-scott-simulation</ns1:workflowNodeID><ns1:attributes><ns1:attribute><ns1:property>node_layout</ns1:property><ns1:value>simulation=2, pdf_calc=1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>nprocs</ns1:property><ns1:value>2</ns1:value></ns1:attribute><ns1:attribute><ns1:property>total_nodes</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>launch_mode</ns1:property><ns1:value>default</ns1:value></ns1:attribute></ns1:attributes><ns1:instanceOf><ns1:instanceOfID>gray-scott</ns1:instanceOfID><ns1:version>1.0.0</ns1:version><ns1:creationTime>2019-06-25T09:38:42.137564</ns1:creationTime></ns1:instanceOf><ns1:serviceID>gray-scott-simulation</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity1><ns1:activity2><ns1:serviceInformation><ns1:workflowID>gray-scott</ns1:workflowID><ns1:workflowNodeID>gray-scott-pdf_calc</ns1:workflowNodeID><ns1:instanceOf><ns1:instanceOfID>gray-scott</ns1:instanceOfID><ns1:version>1.0.0</ns1:version><ns1:creationTime>2019-06-25T09:38:42.138809</ns1:creationTime></ns1:instanceOf><ns1:serviceID>gray-scott-pdf_calc</ns1:serviceID></ns1:serviceInformation><ns1:location>local</ns1:location></ns1:activity2><ns1:communication><ns1:informedActivityID>gray-scott-pdf_calc</ns1:informedActivityID><ns1:informantActivityID>gray-scott-simulation</ns1:informantActivityID></ns1:communication></ns1:addActivityActivityRelationship>"
        #self.assertEqual(expected, parsed_result, msg="Error in the fobs parser output")


if __name__ == '__main__':
    unittest.main()
