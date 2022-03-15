from art import *
from termcolor import *
import os

filepath = os.path.dirname(os.path.abspath(__file__))


def execute_fixed_templates(db: str, template_id: int):
    with open (filepath + f"\\templates\\2\\template{template_id}.txt","r") as file:
        template = file.read()
    filename = filepath + f"\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery{template_id}.ql"
    with open (filename,'w') as file:
        file.writelines(template)
    cprint("Starting CodeQL...","yellow")
    print("Finding all source functions to banned string copy functions")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {db} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery{template_id}.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")


class CustomQLQuery():
    def __init__(self, db) -> None:
        self.db = db

    def with_source_sink(self, source, sink, sink_ind):
        with open (filepath + "\\templates\\1\\template1.txt","r") as file:
            template1 = file.read()
        template1 = template1.replace("read", source).replace("memcpy", sink).replace("2", sink_ind)
        filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery1.ql"
        with open (filename,'w') as file:
            file.writelines(template1)
        cprint("Starting CodeQL...","yellow")
        os.system(f"codeql database analyze --format=sarif-latest --output=out.json {self.db} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery1.ql")
        cprint("CodeQL has successfully analysed your codebase", "yellow")

    def with_sink(self, sink, sink_ind):
        with open (filepath + "\\templates\\1\\template2.txt","r") as file:
            template2 = file.read()
        template2 = template2.replace("memcpy", sink).replace("2", sink_ind)
        filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery2.ql"
        with open (filename,'w') as file:
            file.writelines(template2)
        cprint("Starting CodeQL...","yellow")
        os.system(f"codeql database analyze --format=sarif-latest --output=out.json {self.db} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery2.ql")
        cprint("CodeQL has successfully analysed your codebase.\n", "yellow")

    def with_taint_func(self, source, source_ind, taint, sink, sink_ind):
        with open (filepath + "\\templates\\1\\template3.txt","r") as file:
            template3 = file.read()
        template3 = template3.replace("recvfrom", source).replace("1", source_ind)
        template3 = template3.replace("mempool_alloc", taint)
        template3 = template3.replace("memcpy", sink).replace("2", sink_ind)
        filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery3.ql"

        with open (filename,'w') as file:
            file.writelines(template3)
        cprint("Starting CodeQL...","yellow")
        os.system(f"codeql database analyze --format=sarif-latest --output=out.json {self.db} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery3.ql")
        cprint("CodeQL has successfully analysed your codebase.\n", "yellow")

    def with_taint_expr(self, source, source_ind, sink, sink_ind):
        with open (filepath + "\\templates\\1\\template4.txt","r") as file:
            template4 = file.read()
        template4 = template4.replace("recvfrom", source).replace("1", source_ind)
        template4 = template4.replace("memcpy", sink).replace("2", sink_ind)
        filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery4.ql"

        with open (filename,'w') as file:
            file.writelines(template4)
        cprint("Starting CodeQL...","yellow")
        os.system(f"codeql database analyze --format=sarif-latest --output=out.json {self.db} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery4.ql")
        cprint("CodeQL has successfully analysed your codebase.\n", "yellow")
