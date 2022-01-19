# C0deVari4nt 
![C0deVari4nt](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/icon.png) 

## Description
C0deVari4nt is a variant analysis and visualisation tool that scans the codebase for similar bugs. It leverages CodeQL, a semantic code analysis engine, to query code based on predefined CodeQL query templates and parses the results to Neo4j for easy visualisation. This enhances the process of variant analysis by allowing developers to query their codebase based on bugs reported without having to learn CodeQL. The additional feature of parsing CodeQL results to Neo4j also gives developers additional visibility of their codebase and improves the process of variant analysis. 


## Requirements
### Libraries
`pip install -r requirements.txt`

### CodeQL
- Download your codebase via LGTM

### Neo4j
- Install neo4j locally and create database `CodeVariant` with password `codevariant`
- Start the CodeVariant instance

## Run
- `python3 codevariant.py <zip file path>`
- Run `MATCH (n) RETURN n` at http://localhost:7474/browser/ to get all nodes

## Usage
### Run Codebase against predefined vulnerable sources and sinks
1. Query all source functions to banned string functions based on Microsoft's Security Development Lifecycle (SDL) Banned Function Calls
    1. Developer wants to check codebase against Microsoft's Security Development Lifecycle (SDL) Banned Function Calls

### Run Codebase against sources and sinks of your choice (based on the bug you want to find)
1. Query user input source, sink and sink argument. 
    1. Developer knows the source and sink information
2. Query all source expressions to user input sink and argument.
    1. Developer only knows the sink function and argument.
3. Query user input vulnerable source and sink information whereby the source is tainted.
    1. Developer is trying to find a bug whereby the user input variable is tainted. For instance, developer is trying to find paths whereby the `recvfrom` function value is used in `memcpy` sizeof Argument. However, these 2 nodes are not connected as the variable holding the `recvfrom` value is dereferenced and stored in another variable before the memcpy function. If we were to use the first query, no results will be returned. Instead, we can force the 2 nodes to connect by using `isAdditionalTaintStep` in this query template to catch the tainted source.

## Tool Components 
CodeVariant is built using python, CodeQL and Neo4j to create an interactive GUI application to take user input and showcase relationships between different vulnerable code paths.

CodeVariant consists of the following 3 main components:  
- **Variant-Inputs**: This module takes in a target CodeQL database zip file and user inputs of known source and sink functions to generate CodeQL queries to find bug variants. Alternatively, the module is able to generate queries based on Microsoft’s Security Development Lifecycle’s Banned Function Calls to a user-defined sink.
- **Variant-Query**: This module forms CodeQL query files from a set of predefined query templates using the inputted sources and sinks. The query files are then run on the provided target database to generate a sarif file object of potential vulnerable code paths.
- **Parse2Neo**: This module parses the extracted code paths to create nodes and relationships within the Neo4j interactive graph database. Nodes are categorised into their respective paths, sources and sinks through labels. The module is able to discern recurring steps between multiple code pathways and link them together to display any overlapping of steps.  



## Additional Features  
Although CodeQL query suites exist to facilitate quick analysis of the codebase, the results returned from these suites may not be vulnerable code. The query suites also rely on predefined queries which do not support variant analysis.

Currently, our tool uses a CLI interface built with Python to take user input. Since Neo4j supports integration with UI interfaces, we are looking to migrate the project to a desktop GUI application that will adopt Neo4j’s graph database view and also be able to query custom path perspectives relevant to CodeQL. In a way, our tool will work similarly to Bloodhound, an Active Directory path management solution also built upon Neo4j.

CodeVariant will be available as an open-source project to facilitate additional plugins and contributions in the form of query variant templates by the community to bring the tool to greater heights.

## Project Motivations  
The generation of CodeQL queries takes up too much time. What if someone reported a critical bug in the source code database of an enterprise and developers need a fast and easy way to quickly scan the code database for similar vulnerabilities? For now, there is no straightforward way since the developer will have to first learn how to use CodeQL, generate queries and scan the database. By then, black hat hackers may have already exploited similar bugs in the code. For instance, the recent Log4j attack serves as a good example. After the vulnerability was uncovered, cybersecurity researchers kicked in to identify vulnerable applications, detect potential attacks, and patch codes. However, even after patching, attackers were still able to find new ways and techniques to exploit this vulnerability. This clearly shows the importance of our tool for variant analysis.


## Simplifying CodeQL Results and Relationships between Nodes
![neo-1](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-1.png)  

The above depicts the codeql result paths returned for a query with recvfrom as a source and memcpy as a sink, with an additional taint step check for mempool_alloc. Approximately **180 steps** in **more than 25 different paths** were returned.  

Below is a representation of how the above results looks like in neo4j without any filtering of data. Note that Blue nodes are sources and Red nodes are sinks  

![neo-2](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-2.png)  

By putting this query through our tool, we were able to identify duplicate occurrences of each node, source and sink and merge the relationships of the nodes together.  

The result was a total of **11 unique nodes** merged with the different paths that could be taken from a source to a sink.  

![neo-3](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-3.png)  

The tool is able to further categorise each node into their different paths using Neo4j's built in node labels.

![neo-4](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-4.png)