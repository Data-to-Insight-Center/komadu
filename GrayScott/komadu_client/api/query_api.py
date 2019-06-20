from komadu_client.models.query_modeler import QueryModeler


class QueryAPI:

    def __init__(self):
        self.query_modeler = QueryModeler()

    def get_activity_graph(self, activity_uri, granularity="FINE"):
        """
        Returns the xml string for querying the activity graph
        :param activity_uri:
        :param granularity:
        :return:
        """
        result = self.query_modeler.get_activity_graph_request(activity_uri, granularity)
        return result.toxml("utf-8", element_name='ns1:getActivityGraphRequest').decode('utf-8')
