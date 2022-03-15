import json
import os
from flask import jsonify

filepath = os.path.dirname(os.path.abspath(__file__))


class Parse2Vis():
    context_width = 20

    def __init__(self, db_filepath: str) -> None:
        self.db_filepath = db_filepath

        self.read_sarif()



    def read_sarif(self):
        with open(filepath + "/out.json") as f:
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


    def gen_vis_data(self):
        all_nodes = []
        node_labels = []
        all_rs = []

        for path_count, flow in enumerate(self.code_flows):
            node_list = self.parse_code_flow(flow)

            prev_node_id = None
            for i, node in enumerate(node_list):
                # new node doesnt exist yet
                if not node in all_nodes:
                    all_nodes += [node]
                    node_labels += [{"Step"}]
                    # node_count += 1
                
                # node alr exists

                # get if of alr existing node
                ids = all_nodes.index(node) + 1

                # add r/s
                if prev_node_id and prev_node_id != ids:
                    new_rs = {"from": prev_node_id, "to": ids}
                    if not new_rs in all_rs:
                        all_rs += [new_rs]
                prev_node_id = ids

                # add node labels
                index = all_nodes.index(node)

                node_labels[index].add(f"Path-{path_count + 1}")

                if i == 0:
                    node_labels[index].add("Source")
                    node_labels[index].add(f"Path-{path_count + 1} Source")
                elif i == len(node_list) - 1:
                    node_labels[index].add("Sink")
                    node_labels[index].add(f"Path-{path_count + 1} Sink")

        max_path = len(self.code_flows)

        for label, node in zip(node_labels, all_nodes):
            index = all_nodes.index(node)
            all_nodes[index]["id"] = index + 1


            if "Source" in list(label):
                all_nodes[index]["group"] = "Source"
                all_nodes[index]["color"] = {"background": "#89ECB7", "border": "#2DC775"}
                all_nodes[index]["label"] = "Source"
            elif "Sink" in list(label):
                all_nodes[index]["group"] = "Sink"
                all_nodes[index]["color"] = {"background": "#EC8989", "border": "#DF5959"}
                all_nodes[index]["label"] = "Sink"
            else:
                all_nodes[index]["group"] = "Step"
                all_nodes[index]["color"] = {"background": "#F6EDB5", "border": "#E9D86F"}
                all_nodes[index]["label"] = "Step"
           
            # all_nodes[index]["label"] = list(label)[0]

            all_nodes[index]['color']['highlight'] = {"background": "#A4A3A3", "border": "#686565"}

            all_labels = list(label)
            all_labels.sort()
            all_nodes[index]["all_labels"] = ", ".join(all_labels)
        

        # print(all_nodes)
        # print(max_path)

        final = {
            "nodes": all_nodes,
            "edges": all_rs,
            "max-paths": max_path
        }

        # print(final)

        # with open("codevariant-gui-react/src/data/vis.json", "w") as outfile:
        #     json.dump(final, outfile)
        return final


    def parse_code_flow(self, code_flow):
        locations = code_flow["threadFlows"][0]["locations"]

        final = []
        for i in locations:
            
            file_path = i["location"]["physicalLocation"]["artifactLocation"]["uri"]
            file_line = i["location"]["physicalLocation"]["region"]["startLine"]

            # file_path = file_path.replace("file:/", "")

            if "file:/" in file_path:
                src_root = self.db_filepath + "/"
                file_path = file_path.replace("file:/", "")
            else: src_root = self.db_filepath + "/opt/src/"

            # print(file_path)
            with open(src_root + file_path, encoding="UTF8") as f:
                data = f.readlines()
                code_line = data[file_line - 1]

                code_context = data[file_line - self.context_width:file_line + self.context_width]

            node = {
                "file_path": file_path,
                "file_line": file_line,
                # "message": i["location"]["message"]["text"],
                "code_line": code_line.strip()
                # "code_context": code_context
            }
            final += [node]

        return final




if __name__ == "__main__":
    obj = Parse2Vis("databases\\xebd_accel-ppp_1b8711c")