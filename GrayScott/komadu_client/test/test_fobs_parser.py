import unittest
from komadu_client.parsers.fobs_parser import parse_fobs_json


class TestFobsParser(unittest.TestCase):

    def test_fobs_parser(self):
        file_name = "/Users/swithana/codar/campaigns/gray-scott/experimentGroup2/run-000/codar.cheetah.fob.json"
        parsed_result = parse_fobs_json(file_name)
        print(parsed_result.toxml("utf-8", element_name='ns1:activity').decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
