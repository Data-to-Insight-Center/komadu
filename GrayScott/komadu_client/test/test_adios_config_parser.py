import unittest
from komadu_client.parsers.adios_config_parser import parse_adios2xml


class TestAdios2ConfigParser(unittest.TestCase):

    def test_adios2_parser(self):
        file_name = "./resources/gray-scott/adios2.xml"
        result = parse_adios2xml(file_name).toxml("utf-8", element_name='ns1:attributes').decode('utf-8').replace('"', "'")
        expected = "<?xml version='1.0' encoding='utf-8'?><ns1:attributes xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:attribute><ns1:property>SimulationOutput_BPFile_RendezvousReaderCount</ns1:property><ns1:value>0</ns1:value></ns1:attribute><ns1:attribute><ns1:property>SimulationOutput_BPFile_QueueLimit</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>SimulationOutput_BPFile_QueueFullPolicy</ns1:property><ns1:value>Discard</ns1:value></ns1:attribute><ns1:attribute><ns1:property>SimulationOutput_U_zfp_accuracy</ns1:property><ns1:value>0.00001</ns1:value></ns1:attribute><ns1:attribute><ns1:property>SimulationOutput_V_zfp_accuracy</ns1:property><ns1:value>0.00001</ns1:value></ns1:attribute><ns1:attribute><ns1:property>PDFAnalysisOutput_BPFile_RendezvousReaderCount</ns1:property><ns1:value>1</ns1:value></ns1:attribute><ns1:attribute><ns1:property>PDFAnalysisOutput_BPFile_QueueLimit</ns1:property><ns1:value>5</ns1:value></ns1:attribute><ns1:attribute><ns1:property>PDFAnalysisOutput_BPFile_QueueFullPolicy</ns1:property><ns1:value>Block</ns1:value></ns1:attribute><ns1:attribute><ns1:property>IsosurfaceOutput</ns1:property><ns1:value>BPFile</ns1:value></ns1:attribute></ns1:attributes>"
        self.assertEqual(expected, result, msg="Error in the adios2 parser output")


if __name__ == '__main__':
    unittest.main()
