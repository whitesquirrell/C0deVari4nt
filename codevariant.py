from art import *
from termcolor import *
import os


def display_bar():
    cprint("*" * 100, "yellow")
    print()

def userInput():
    print("1. Run Code base against predefined vulnerable sources and sinks")
    print("2. Run Code base against sources and sinks of your choice\n")
    while True:
        try:
            category = input("Please input your choice of action (ENTER TO EXIT): ")
            if category == "" : #If user types ENTER
                raise Exception("END PROGRAM") #Raise an exception that will end the program
            else:
                if (int(category) <1 or int(category)>2):
                    print("Invalid input, please enter a 1 or 2")
                else:
                    if (category == "1"):
                        predefinedDS()
                        break
                    else:
                        customDS()
                        break
        except ValueError:
            print("Invalid input, please enter a number")
        except:
            runProgram = False
            break

def predefinedDS():
    print("Run the code base against our vuln sources and sinks")

def customDS():
    print("Please fill up the the source and sink function of your bug: \n")
    description = input("Description (Vuln Type): ")
    source = input ("Source Function: ")
    sink = input ("Sink Function (strcpy, strncpy, strcat, scanf, sprintf, gets, fgets, memcpy): ")
    while sink not in ["strcpy", "strncpy", "strcat", "scanf", "sprintf", "gets", "fgets", "memcpy"]:
        print("Invalid Input")
        return
    print(description + "\n" + source + "\n" + sink + "\n")
    queryfile(source,sink)

def queryfile(source,sink):
    with open ("template2.txt","r") as file:
        template2 = file.readlines()
    template2[12] = f'source.asExpr().(FunctionCall).getTarget().hasGlobalName("{source}")'
    if sink == "memcpy":
        template2[16] = f'exists(FunctionCall fc | fc.getTarget().hasName("memcpy") and sink.asExpr() = fc.getArgument(2))'
    filename = "C:\\Users\\chloe\\Documents\\ACC_GovTech\\BlackHat_Arsenal\\CodeVariant\\vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql"
    with open (filename,'w') as file:
        file.writelines(template2)
    os.system("codeql query run --database=xebd_accel-ppp_cpp-srcVersion_1b8711cf75a7c278d99840112bc7a396398e0205-dist_codeql-bundle-linux64-20211202-1530398226\\xebd_accel-ppp_1b8711c vscode-codeql-starter\\codeql-custom-queries-cpp\\userQuery.ql")

cprint("=====================================\n Hello Welcome! Presenting you...\n=====================================\n", "blue")
tprint("C0deVari4nt")
display_bar()
inputValue = userInput()

