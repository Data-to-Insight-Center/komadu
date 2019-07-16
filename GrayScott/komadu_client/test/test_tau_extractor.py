import unittest
from komadu_client.parsers.tau_profile_parser import parse_tau_file

class TestTauParser(unittest.TestCase):

    def test_parse_bp_file(self):
        filename = "./resources/gray-scott/tau-metrics.bp"
        attributes = parse_tau_file(filename)
        actual = attributes.toxml("utf-8", element_name='ns1:attributes').decode('utf-8').replace('"', "'")
        print(actual)
