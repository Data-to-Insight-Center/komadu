import unittest
from komadu_client.models.model_creator import add_attributes_activity
from datetime import datetime


class TestModelCreator(unittest.TestCase):

    def test_add_attributes_activity(self):
        result = add_attributes_activity("exp1-run-000", "sim", "completed_time", 0.34343)
        result.notificationTimestamp = datetime(2019, 10, 30, 18, 00)
        actual = result.toxml("utf-8", element_name='ns1:addAttributes').decode('utf-8').replace('"', "'")
        expected = "<?xml version='1.0' encoding='utf-8'?><ns1:addAttributes xmlns:ns1='http://komadu.d2i.indiana.edu'><ns1:objectType>ACTIVITY</ns1:objectType><ns1:objectID>exp1-run-000-sim</ns1:objectID><ns1:attributes><ns1:attribute><ns1:property>completed_time</ns1:property><ns1:value>0.34343</ns1:value></ns1:attribute></ns1:attributes><ns1:notificationTimestamp>2019-10-30T18:00:00</ns1:notificationTimestamp></ns1:addAttributes>"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
