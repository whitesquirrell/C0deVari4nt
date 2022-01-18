from inspect import currentframe
import json
import os
from py2neo import Graph, Node, Relationship, NodeMatcher, GraphService
import glob
from neo4j import GraphDatabase

dirname = os.path.dirname(__file__)


class Parse2Neo():
    context_width = 20

    def __init__(self, db_filepath: str) -> None:
        self.db_filepath = db_filepath

        self.graph = Graph("bolt://localhost:7687", auth = ("neo4j", "codevariant"))
        self.reset_graph()

        self.read_sarif()

        for i, flow in enumerate(self.code_flows):
            node_list = self.parse_code_flow(flow)
            self.create_nodes(node_list, i + 1)

        # self.init_node_colours()

        # note that cache deleted it's gonna take a lot longer
        self.del_database_cache()

    
    def get_node(self, label: str, location: str):
        # matcher = NodeMatcher(self.graph)

        # return matcher.match(label, location=location).first()
        return self.graph.nodes.match(label, location=location).first()



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
        

    def run_command_native(self, command):
        driver = GraphDatabase.driver("bolt://localhost:7687", auth = ("neo4j", "codevariant"))

        with driver.session() as session:
            session.run(command)

    # def init_node_colours(self):
    #     # tx = self.graph.begin()
    #     # tx.run(":style")
    #     gs = GraphService("bolt://localhost:7687")
    #     print(gs.config)


    def parse_code_flow(self, code_flow):
        locations = code_flow["threadFlows"][0]["locations"]

        final = []
        for i in locations:
            
            file_path = i["location"]["physicalLocation"]["artifactLocation"]["uri"]
            file_line = i["location"]["physicalLocation"]["region"]["startLine"]

            # file_path = file_path.replace("file:/", "")

            if "file:/" in file_path:
                src_root = self.db_filepath
                file_path = file_path.replace("file:/", "")
            else: src_root = self.db_filepath + "/opt/src/"

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

    def create_nodes(self, node_list, path_count: int):

        prev_node = None
        # path_count = 1
        for i, node in enumerate(node_list):

            location = f"{node['file_path']}:{node['file_line']}"

            # check if same node exists yet
            existing_node = self.get_node("Step", location)
            if existing_node:
                current_node = existing_node
            else:
                current_node = Node(
                    "Step",
                    name = node["code_line"],
                    location = location,
                    target = node["message"]
                    # context = node["code_context"]
                )

            # current_node = Node(
            #     "Step",
            #     name = node["code_line"],
            #     location = location,
            #     target = node["message"]
            #     # context = node["code_context"]
            # )
            
            node_labels = [f"Path-{path_count}"]
            

            if i == 0:
                
                node_labels += ["Source", f"Path-{path_count} Source"]
                # print(current_node["location"])
                # current_node.update_labels(["Step", "Source"])
                # current_node.update_labels(node_labels)

                # print(path_count)
                # path_count += 1
            elif i == len(node_list) - 1:
                # current_node.update_labels(["Step", "Sink"])
                node_labels += ["Sink", f"Path-{path_count} Sink"]
            
            # print(current_node['location'])
            # print(current_node['name'])
            
            # print(path_count)
            # print(node_labels)
            # print(i)

            # print()

            current_node.update_labels(node_labels)

            # print(current_node.labels)
            # print(prev_node)
            # print(current_node)
            # print()

            # print(prev_node)
            # print(current_node)
            # print("=======================================")

            self.graph.push(current_node)

            if prev_node:
                # print(prev_node["location"])
                if prev_node["location"] != current_node["location"]:
                    # self.graph.create(current_node)

                    self.graph.create(Relationship(
                        prev_node,
                        "Flows into",
                        current_node
                    ))
                    prev_node = current_node
            else:
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
    # node = obj.get_node("Step", "accel-pppd/radius/packet.c:142")
    # print(node)