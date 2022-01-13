import json
import os
from py2neo import Graph, Node, Relationship

dirname = os.path.dirname(__file__)

class Parse2Neo():
    def __init__(self) -> None:
        self.read_sarif()

        self.graph = Graph("bolt://localhost:7687", auth = ("neo4j", "codevariant"))
        self.reset_graph()
        

        for flow in self.code_flows:
            node_list = self.parse_code_flow(flow)
            self.create_nodes(node_list)

        # os.remove(os.path.join(dirname, 'out.json'))


    def read_sarif(self):
        with open(os.path.join(dirname, 'out.json')) as f:
            json_file = json.load(f)

        # self.code_flows = json_file["runs"][0]["results"][0]["codeFlows"]

        self.code_flows = []
        for result in json_file["runs"][0]["results"]:
            # for flow in result["codeFlows"]:
            self.code_flows += [result["codeFlows"][0]]


    def reset_graph(self):
        self.graph.run('''
            MATCH (n)
            OPTIONAL MATCH (n)-[r]-()
            WITH n,r LIMIT 50000
            DELETE n,r
            RETURN count(n) as deletedNodesCount
            ''')


    def parse_code_flow(self, code_flow):
        locations = code_flow["threadFlows"][0]["locations"]

        final = []
        for i in locations:

            node = {
                "file_path": i["location"]["physicalLocation"]["artifactLocation"]["uri"],
                "file_line": i["location"]["physicalLocation"]["region"]["startLine"],
                "message": i["location"]["message"]["text"]
            }

            final += [node]

        return final

    def create_nodes(self, node_list):
        prev_node = None
        for i, node in enumerate(node_list):
            label = "Step"
            if i == 0: label = "Source"
            elif i == len(node_list) - 1: label = "Sink"

            current_node = Node(
                label,
                name = node["message"],
                location = f"{node['file_path']}:{node['file_line']}"
            )
            self.graph.create(current_node)

            if prev_node:
                self.graph.create(Relationship(
                    prev_node,
                    "Flows into",
                    current_node
                ))

            prev_node = current_node



if __name__ == "__main__":
    obj = Parse2Neo()