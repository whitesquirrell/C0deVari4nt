from re import template
from art import *
from termcolor import *
import os

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
    print("2. Query a specific source to a dangerous sink\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT):")
            if category == "" :
                raise Exception("END PROGRAM") 
            else:
                if (int(category) <1 or int(category)>2):
                    print("Invalid input, please enter a 1 or 2")
                else:
                    if (category == "1"):
                        customSink()
                        break
                    else:
                        customSourceSink()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            break
    
def customSink():
    print("\nPlease fill up the dangerous sink function: ")
    description = input("Description (Vuln Type): ")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    queryThirdTem(sink,arg)

def queryThirdTem(sink,arg):
    with open ("template3.txt","r") as file:
        template3 = file.read()
    template3 = template3.replace("memcpy", sink).replace("2", arg)
    filepath = os.path.dirname(__file__)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery3.ql"
    with open (filename,'w') as file:
        file.writelines(template3)
    os.system("codeql query run --database=xebd_accel-ppp_cpp\\xebd_accel-ppp_1b8711c vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery3.ql")

def customSourceSink():
    print("\nPlease fill up the the source and sink function of your bug: ")
    description = input("Description (Vuln Type): ")
    source = input ("Source Function(eg recv): ")
    sink = input ("Sink Function(eg memcpy): ")
    arg = input("Vuln sink argument(starts from 0): ")
    querySecondTem(source,sink,arg)    

def querySecondTem(source,sink,arg):
    with open ("template2.txt","r") as file:
        template2 = file.read()
    template2 = template2.replace("read", source).replace("memcpy", sink).replace("2", arg)
    filepath = os.path.dirname(__file__)
    filename = filepath + "\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql"
    with open (filename,'w') as file:
        file.writelines(template2)
    os.system("codeql query run --database=xebd_accel-ppp_cpp\\xebd_accel-ppp_1b8711c vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql")

if __name__ == "__main__":
    cprint("=====================================\n Hello Welcome! Presenting you...\n=====================================\n", "blue")
    tprint("C0deVari4nt")
    display_bar()
    inputValue = userInput()

