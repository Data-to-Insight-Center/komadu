import unittest
from komadu_client.util.util import get_experiment_name


class TestUtil(unittest.TestCase):

    def test_experiment_name(self):
        grayscott_name = "/Users/swithana/codar/campaigns/gray-scott/swithana/experimentGroup2/run-000/settings.json"
        experiment_name = get_experiment_name(grayscott_name)
        self.assertTrue(experiment_name, "experimentGroup2-run-000")

        no_group_name = "/Users/swithana/codar/campaigns/gray-scott/swithana/experimentGroup2/group-env.sh"
        experiment_name = get_experiment_name(no_group_name)
        self.assertTrue(experiment_name, "experimentGroup2")

if __name__ == '__main__':
    unittest.main()