from re import template
from art import *
from termcolor import *
import os
from parse2neo import Parse2Neo
from misc import Misc
import sys

DB_FILE_PATH = ""

def display_bar():
    cprint("*" * 100)
    print()

def userInput():
    print("1. Run Code base against predefined vulnerable sources and sinks")
    print("2. Run Code base against sources and sinks of your choice\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT): ")
            display_bar()
            if category == "" :
                raise Exception("END PROGRAM") 
            else:
                if (int(category) <1 or int(category)>2):
                    print("Invalid input, please enter a 1 or 2")
                else:
                    if (category == "1"):
                        predefinedDS()
                        break
                    else:
                        chooseOptions()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break

def predefinedDS():
    print("Run the code base against our vuln sources and sinks")

def chooseOptions():
    print("Please choose one of the following options")
    print("1. Query all sources to a dangerous sink")
    print("2. Query a specific source to a dangerous sink")
    print("3. Query a specific source to a dangerous sink (Tainted source)\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT):")
            if category == "" :
                raise Exception("END PROGRAM") 
            else:
                if (int(category) <1 or int(category)>3):
                    print("Invalid input, please enter a 1 or 2")
                else:
                    if (category == "1"):
                        customSink()
                        break
                    elif (category == "2"):
                        customSourceSink()
                        break
                    else:
                        taintSource()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break

def customSourceSink():
    print("\nPlease fill up the the source and sink function of your bug: ")
    # description = input("Description (Vuln Type): ")
    source = input ("Source Function(eg recv): ")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    queryFirstTem(source,sink,arg)    

def queryFirstTem(source,sink,arg):
    with open ("template1.txt","r") as file:
        template1 = file.read()
    template1 = template1.replace("read", source).replace("memcpy", sink).replace("2", arg)
    filepath = os.path.dirname(os.path.abspath(__file__))
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql"
    with open (filename,'w') as file:
        file.writelines(template1)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def customSink():
    print("\nPlease fill up the dangerous sink function: ")
    # description = input("Description (Vuln Type): ")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    querySecondTem(sink,arg)

def querySecondTem(sink,arg):
    with open ("template2.txt","r") as file:
        template2 = file.read()
    template2 = template2.replace("memcpy", sink).replace("2", arg)
    filepath = os.path.dirname(os.path.abspath(__file__))
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery2.ql"
    # print(template2)
    with open (filename,'w') as file:
        file.writelines(template2)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery2.ql")
    # os.system(f"codeql query run --database={DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery2.ql") # this works
    cprint("CodeQL has successfully analysed your codebase.\n", "yellow")

def taintSource():
    print("\nPlease fill up the the source and sink function of your bug: ")
    source = input ("Source Function(eg recvfrom): ")
    sourceArg = input ("Source Function Argument (starts from 0): ")
    taintSource = input("Tainted function(eg source -> tainted function -> sink): ")
    sink = input ("Sink Function(eg memcpy): ")
    sinkArg = input("Vuln sink argument(starts from 0): ")
    queryThirdTem(source,sourceArg,taintSource,sink,sinkArg)    

def queryThirdTem(source,sourceArg,taintSource,sink,sinkArg):
    with open ("template3.txt","r") as file:
        template3 = file.read()
    template3 = template3.replace("recvfrom", source).replace("1", sourceArg)
    template3 = template3.replace("mempool_alloc", taintSource)
    template3 = template3.replace("memcpy", sink).replace("2", sinkArg)
    filepath = os.path.dirname(os.path.abspath(__file__))
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery3.ql"
    # print(template3)
    with open (filename,'w') as file:
        file.writelines(template3)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery3.ql")
    cprint("CodeQL has successfully analysed your codebase.\n", "yellow")


if __name__ == "__main__":
    cprint("=====================================\n Hello Welcome! Presenting you...\n=====================================\n", "blue")
    tprint("C0deVari4nt")

    # extract file from first arg of code (must be zip file)
    file = sys.argv[-1]

    cprint("Unpacking your database zip archive into databases/. Please wait for a few minutes.", "yellow")
    cprint("If it takes too long, delete your databases folder and try again.", "red")
    misc = Misc()
    DB_FILE_PATH = misc.unzip_database_file(file)


    display_bar()
    inputValue = userInput()
    
    cprint("Parsing CodeQL data to neo4j...ensure your server is running.", "red")
    Parse2Neo(DB_FILE_PATH)
    cprint("Head to http://localhost:7474/browser/ to view your updated graph.", "yellow")