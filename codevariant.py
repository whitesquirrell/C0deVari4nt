from re import template
from art import *
from termcolor import *
import os
from parse2neo import Parse2Neo
from misc import Misc
import sys

DB_FILE_PATH = ""
filepath = ""
def display_bar():
    cprint("*" * 100)
    print()

def userInput():
    print("Please choose one of the following options")
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
                        chooseOptions1()
                        break
                    else:
                        chooseOptions2()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break

def chooseOptions1():
    print("Please choose one of the following options")
    print("1. Find all source functions to banned string copy functions")
    print("2. Find all calls to strcat without checking the size of the source string")
    print("3. Find all calls to strncat with the size of the source buffer as third argument")
    print("4. Find all cases with no bound checks on the return value of a call to snprintf")
    print("5. Find all calls to malloc, calloc or realloc without sufficient memory allocated to contain an instance of the type of the pointer\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT):")
            display_bar()
            if category == "" :
                raise Exception("END PROGRAM") 
            else:
                if (int(category) <1 or int(category)>5):
                    print("Invalid input, please enter a 1 to 5")
                else:
                    if (category == "1"):
                        bannedStringCopy()
                        break
                    elif (category == "2"):
                        dangerousStrcat()
                        break
                    elif (category == "3"):
                        dangerousStrncat()
                        break
                    elif (category == "4"):
                        dangerousSnprintf()
                        break
                    else:
                        dangerousMem()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break
    
def bannedStringCopy():
    with open (filepath + "\\templates\\2\\template1.txt","r") as file:
        template1 = file.read()
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery1.ql"
    with open (filename,'w') as file:
        file.writelines(template1)
    cprint("Starting CodeQL...","yellow")
    print("Finding all source functions to banned string copy functions")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery1.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def dangerousStrcat():
    with open (filepath + "\\templates\\2\\template2.txt","r") as file:
        template2 = file.read()
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery2.ql"
    with open (filename,'w') as file:
        file.writelines(template2)
    cprint("Starting CodeQL...","yellow")
    print("Finding all strcat functions without bound checks on the size of source string")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery2.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def dangerousStrncat():
    with open (filepath + "\\templates\\2\\template3.txt","r") as file:
        template3 = file.read()
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery3.ql"
    with open (filename,'w') as file:
        file.writelines(template3)
    cprint("Starting CodeQL...","yellow")
    print("Finding all strncat functions with the size of the source buffer as third argument")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery3.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def dangerousSnprintf():
    with open (filepath + "\\templates\\2\\template4.txt","r") as file:
        template4 = file.read()
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery4.ql"
    with open (filename,'w') as file:
        file.writelines(template4)
    cprint("Starting CodeQL...","yellow")
    print("Finding all cases with no bound checks on the return value of a call to snprintf")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery4.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def dangerousMem():
    with open (filepath + "\\templates\\2\\template5.txt","r") as file:
        template5 = file.read()
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery5.ql"
    with open (filename,'w') as file:
        file.writelines(template5)
    cprint("Starting CodeQL...","yellow")
    print("Finding all calls to malloc, calloc or realloc without sufficient memory allocated to contain an instance of the type of the pointer")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\2\\userQuery5.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def chooseOptions2():
    print("Please choose one of the following options")
    print("1. Query all sources to a dangerous sink")
    print("2. Query a specific source to a dangerous sink")
    print("3. Query a specific source to a dangerous sink (Tainted function)")
    print("4. Query a specific source to a dangerous sink (Tainted expression)\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT):")
            display_bar()
            if category == "" :
                raise Exception("END PROGRAM") 
            else:
                if (int(category) <1 or int(category)>5):
                    print("Invalid input, please enter a 1 to 5")
                else:
                    if (category == "1"):
                        customSink()
                        break
                    elif (category == "2"):
                        customSourceSink()
                        break
                    elif (category == "3"):
                        taintFunction()
                        break
                    else:
                        taintExpr()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break

def customSourceSink():
    print("Please fill up the the source and sink information of your bug")
    source = input ("Source Function(eg recv): ")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    queryFirstTem(source,sink,arg)    

def queryFirstTem(source,sink,arg):
    with open (filepath + "\\templates\\1\\template1.txt","r") as file:
        template1 = file.read()
    template1 = template1.replace("read", source).replace("memcpy", sink).replace("2", arg)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery1.ql"
    with open (filename,'w') as file:
        file.writelines(template1)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery1.ql")
    cprint("CodeQL has successfully analysed your codebase", "yellow")

def customSink():
    print("Please fill up the sink information")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    querySecondTem(sink,arg)

def querySecondTem(sink,arg):
    with open (filepath + "\\templates\\1\\template2.txt","r") as file:
        template2 = file.read()
    template2 = template2.replace("memcpy", sink).replace("2", arg)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery2.ql"
    with open (filename,'w') as file:
        file.writelines(template2)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery2.ql")
    cprint("CodeQL has successfully analysed your codebase.\n", "yellow")

def taintFunction():
    print("Please fill up the the source, tainted function and sink information of your bug")
    source = input ("Source Function(eg recvfrom): ")
    sourceArg = input ("Source Function Argument (starts from 0): ")
    taintFunction = input("Tainted function(eg source -> tainted function -> sink): ")
    sink = input ("Sink Function(eg memcpy): ")
    sinkArg = input("Vuln sink argument(starts from 0): ")
    queryThirdTem(source,sourceArg,taintFunction,sink,sinkArg)    

def queryThirdTem(source,sourceArg,taintFunction,sink,sinkArg):
    with open (filepath + "\\templates\\1\\template3.txt","r") as file:
        template3 = file.read()
    template3 = template3.replace("recvfrom", source).replace("1", sourceArg)
    template3 = template3.replace("mempool_alloc", taintFunction)
    template3 = template3.replace("memcpy", sink).replace("2", sinkArg)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery3.ql"

    with open (filename,'w') as file:
        file.writelines(template3)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery3.ql")
    cprint("CodeQL has successfully analysed your codebase.\n", "yellow")

def taintExpr():
    print("Please fill up the the source and sink information of your bug")
    source = input ("Source Function(eg recvfrom): ")
    sourceArg = input ("Source Function Argument (starts from 0): ")
    sink = input ("Sink Function(eg memcpy): ")
    sinkArg = input("Vuln sink argument(starts from 0): ")
    queryForthTem(source,sourceArg,sink,sinkArg)    

def queryForthTem(source,sourceArg,sink,sinkArg):
    with open (filepath + "\\templates\\1\\template4.txt","r") as file:
        template4 = file.read()
    template4 = template4.replace("recvfrom", source).replace("1", sourceArg)
    template4 = template4.replace("memcpy", sink).replace("2", sinkArg)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery4.ql"

    with open (filename,'w') as file:
        file.writelines(template4)
    cprint("Starting CodeQL...","yellow")
    os.system(f"codeql database analyze --format=sarif-latest --output=out.json {DB_FILE_PATH} vscode-codeql-starter\\codeql-custom-queries-cpp\\1\\userQuery4.ql")
    cprint("CodeQL has successfully analysed your codebase.\n", "yellow")


if __name__ == "__main__":
    cprint("=====================================\n Hello Welcome! Presenting you...\n=====================================\n", "blue")
    tprint("C0deVari4nt")
    # extract file from first arg of code (must be zip file)
    file = sys.argv[-1]
    filepath = os.path.dirname(os.path.abspath(__file__))
    cprint("Unpacking your database zip archive into databases/. Please wait for a few minutes.", "yellow")
    cprint("If it takes too long, delete your database folder and try again.", "red")
    misc = Misc()
    DB_FILE_PATH = misc.unzip_database_file(file)
    display_bar()
    inputValue = userInput()
    cprint("Parsing CodeQL data to neo4j...ensure your server is running.", "red")
    Parse2Neo(DB_FILE_PATH)
    cprint("Head to http://localhost:7474/browser/ to view your updated graph.", "yellow")