from komadu_client.models.query_models import getActivityGraphRequestType


class QueryModeler:

    def get_activity_graph_request(self, activity_uri, granularity="FINE"):
            query = getActivityGraphRequestType()
            query.activityURI = activity_uri
            query.informationDetailLevel = granularity
            return query
