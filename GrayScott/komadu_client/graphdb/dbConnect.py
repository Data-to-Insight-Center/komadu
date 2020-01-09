from neo4j import GraphDatabase
from komadu_client.graphdb.queries import CREATE_USER, READ_USER


class Database(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_friendships(self):
        with self._driver.session() as db:
            result = db.run("MATCH (user:User)-[:Created]->(camp:Codesign) RETURN user.name, camp.name;")
        # result = tx.run("MATCH (user:User)-[:Created]->(camp:Codesign) RETURN user.name, camp.name;")
        for record in result:
            print("{} Created {}".format(record["user.name"], record["camp.name"]))

    def run_fobs_init_graph_query(self, query):
        """
        Creates the initial graph for the fobs information
        :param query:
        :return:
        """
        with self._driver.session() as session:
            session.write_transaction(self.run_init_fobs_graph, query)

    def add_user(self, name):
        with self._driver.session() as session:
            session.write_transaction(self.create_user_node, name)
            return session.read_transaction(self.match_user_node, name)

    # Units of work

    @staticmethod
    def create_user_node(tx, name):
        return tx.run(CREATE_USER, name=name).single().value()

    @staticmethod
    def match_user_node(tx, name):
        result = tx.run(READ_USER, name=name)
        return result.single()[0]

    @staticmethod
    def run_init_fobs_graph(tx, query):
        return tx.run(query).single()




