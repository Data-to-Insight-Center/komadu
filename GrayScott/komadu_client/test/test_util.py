import unittest
from komadu_client.util.util import get_experiment_info, get_attributes, get_workflow_name


class TestUtil(unittest.TestCase):

    def test_experiment_name(self):
        grayscott_name = "/Users/swithana/codar/campaigns/gray-scott/swithana/experimentGroup2/run-000/settings.json"
        experiment_name = get_experiment_info(grayscott_name)[0]
        self.assertTrue(experiment_name, "experimentGroup2-run-000")

        no_group_name = "/Users/swithana/codar/campaigns/gray-scott/swithana/experimentGroup2/group-env.sh"
        experiment_name = get_experiment_info(no_group_name)[0]
        self.assertTrue(experiment_name, "experimentGroup2")

    def test_get_attributes(self):
        dict_test = {
            "location": "summit",
            "nprocs": 2
        }
        attributes = get_attributes(dict_test)
        attr_str = attributes.toxml("utf-8", element_name='attributes').decode('utf-8')
        expected_result = "<?xml version='1.0' encoding='utf-8'?><attributes xmlns:ns1='http://komadu.d2i.indiana.edu'"\
                          "><ns1:attribute><ns1:property>location</ns1:property><ns1:value>summit</ns1:value>" \
                          "</ns1:attribute><ns1:attribute><ns1:property>nprocs</ns1:property><ns1:value>2</ns1:value>" \
                          "</ns1:attribute></attributes>"

        self.assertTrue(expected_result, attr_str)

    def test_get_workflow_name(self):
        example_file = "/Users/swithana/codar/campaigns/gray-scott/swithana/experimentGroup2/run-000/settings.json"
        workflow_name = get_workflow_name(example_file)
        self.assertTrue("gray-scott", workflow_name)


if __name__ == '__main__':
    unittest.main()
