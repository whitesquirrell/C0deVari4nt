
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

        # for i, flow in enumerate(self.code_flows):
        #     node_list = self.parse_code_flow(flow)
        #     self.create_nodes(node_list, i + 1)
        self.show_all_paths()

        # self.show_one_path(19)

        # note that cache deleted it's gonna take a lot longer
        self.del_database_cache()


    def show_all_paths(self):
        for i, flow in enumerate(self.code_flows):
            node_list = self.parse_code_flow(flow)
            self.create_nodes(node_list, i + 1)


    def show_one_path(self, path_num: int):
        matcher = NodeMatcher(self.graph)
        nodes = matcher.match(f"Path-{path_num}").all()

        self.reset_graph()
        
        for node in nodes:
            print(node)
            self.graph.create(node)

        # print(nodes)

    def get_node(self, label: str, location: str):
        return self.graph.nodes.match(label, location=location).first()



    def read_sarif(self):
        with open(os.path.join(dirname, 'out.json')) as f:
            json_file = json.load(f)


        self.code_flows = []
        for result in json_file["runs"][0]["results"]:
            # for flow in result["codeFlows"]:

            try:
                for i in result["codeFlows"]:
                    self.code_flows += [i]
            except:
                # pass if the result dont have a codeflow (means is just header)
                pass


    def reset_graph(self):
        self.graph.delete_all()
        

    def run_command_native(self, command):
        driver = GraphDatabase.driver("bolt://localhost:7687", auth = ("neo4j", "codevariant"))

        with driver.session() as session:
            session.run(command)


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

            with open(src_root + file_path, encoding="UTF8") as f:
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
                    target = node["message"],
                    path = path_count,
                    context = node["code_context"]
                )

            # current_node = Node(
            #     "Step",
            #     name = node["code_line"],
            #     location = location,
            #     target = node["message"]
            #     # context = node["code_context"]
            # )
            
            node_labels = [f"Path-{path_count}"]
            # node_labels = []
            

            if i == 0:
                
                node_labels += ["Source", f"Path-{path_count} Source"]

            elif i == len(node_list) - 1:
                # current_node.update_labels(["Step", "Sink"])
                node_labels += ["Sink", f"Path-{path_count} Sink"]
            

            current_node.update_labels(node_labels)


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
            for f in files:
                os.remove(f)
        except:
            pass



if __name__ == "__main__":
    obj = Parse2Neo("databases\\xebd_accel-ppp_1b8711c")
    # node = obj.get_node("Step", "accel-pppd/radius/packet.c:142")
    # print(node)
    # obj.show_one_path(19)