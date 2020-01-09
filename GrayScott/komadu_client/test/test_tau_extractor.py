import unittest
from komadu_client.parsers.tau_profile_parser import parse_tau_file


class TestTauParser(unittest.TestCase):

    def test_parse_bp_file(self):
        filename = "./resources/gray-scott/exp_2019_07_23__14_19_30/tau-metrics-0.bp"
        attributes = parse_tau_file(filename)
        actual = attributes.toxml("utf-8", element_name='ns1:attributes').decode('utf-8').replace('"', "'")
        expected = "<?xml version='1.0' encoding='utf-8'?><ns1:attributes xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:attribute><ns1:property>hostname</ns1:property><ns1:value>swithana-mbp.local</ns1:value></ns1:attribute><ns1:attribute><ns1:property>counter_1</ns1:property><ns1:value>Message size sent to all nodes</ns1:value></ns1:attribute><ns1:attribute><ns1:property>location</ns1:property><ns1:value>./resources/gray-scott/tau-metrics.bp</ns1:value></ns1:attribute></ns1:attributes>"
        #self.assertEqual(actual, expected)
