import json
import os
from py2neo import Graph, Node, Relationship
import glob

dirname = os.path.dirname(__file__)


class Parse2Neo():
    context_width = 20

    def __init__(self, db_filepath: str) -> None:
        self.db_filepath = db_filepath

        
        self.graph = Graph("bolt://localhost:7687", auth = ("neo4j", "codevariant"))
        self.reset_graph()

        self.read_sarif()

        for flow in self.code_flows:
            node_list = self.parse_code_flow(flow)
            self.create_nodes(node_list)

        # note that cache deleted it's gonna take a lot longer
        self.del_database_cache()
 


    def read_sarif(self):
        with open(os.path.join(dirname, 'out.json')) as f:
            json_file = json.load(f)

        # self.code_flows = json_file["runs"][0]["results"][0]["codeFlows"]

        self.code_flows = []
        for result in json_file["runs"][0]["results"]:
            # for flow in result["codeFlows"]:

            for i in result["codeFlows"]:
                try:
                    self.code_flows += [i]
                except:
                    # pass if the result dont have a codeflow (means is just header)
                    pass


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

        src_root = self.db_filepath + "/opt/src/"

        final = []
        for i in locations:
            file_path = i["location"]["physicalLocation"]["artifactLocation"]["uri"]
            file_line = i["location"]["physicalLocation"]["region"]["startLine"]

            # print(src_root + file_path)
            with open(src_root + file_path) as f:
                data = f.readlines()
                code_line = data[file_line - 1]

                code_context = data[file_line - self.context_width:file_line + self.context_width]


            node = {
                "file_path": file_path,
                "file_line": file_line,
                "message": i["location"]["message"]["text"],
                "code_line": code_line.strip(),
                "code_context": code_context
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
                name = node["code_line"],
                location = f"{node['file_path']}:{node['file_line']}",
                target = node["message"],
                context = node["code_context"]
            )
            self.graph.create(current_node)

            if prev_node:
                self.graph.create(Relationship(
                    prev_node,
                    "Flows into",
                    current_node
                ))

            prev_node = current_node


    def del_database_cache(self):
        db_folder = self.db_filepath
        try:
            files = glob.glob(os.path.join(dirname, db_folder + "/results/getting-started/codeql-extra-queries-cpp/*"))
            # os.remove(os.path.join(dirname, db_folder + "/results/getting-started/codeql-extra-queries-cpp/"))
            for f in files:
                os.remove(f)
        except:
            pass



if __name__ == "__main__":
    obj = Parse2Neo("databases\\xebd_accel-ppp_1b8711c")