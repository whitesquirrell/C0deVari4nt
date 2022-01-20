# C0deVari4nt 
![C0deVari4nt](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/icon.png) 

## Description
C0deVari4nt is a variant analysis and visualisation tool that inspects codebases for similar vulnerabilities. It leverages CodeQL, a semantic code analysis engine, to query code based on user-controlled CodeQL query templates and passes the results to Neo4j for further exploration and visualisation. This enables quick and comprehensive variant analysis based on previous vulnerability reports. The Neo4j visualisation feature provides additional insight for developers into vulnerable code paths and allows them to effectively triage potential variants.

## Motivations
The Log4Shell incident in December 2021 highlighted the difficulties open-source developers face in responding to vulnerability reports. After the initial patch for CVE-2021-44228, which allowed unauthenticated remote attackers to take control of devices running vulnerable versions of Log4j 2, Apache released 3 additional patches to address related vulnerabilities and unmitigated edge cases.

Open-source developers often lack training in comprehensive code review and face problems in identifying variants of a vulnerability, leading to incomplete patches. Although CodeQL query suites exist to facilitate quick analysis of the codebase, the results returned from these suites may result in significant false positive rates. Furthermore, these suites rely on predefined queries which do not support variant analysis and are not customised for individual codebases. As such, open-source projects often respond to vulnerability reports in a piecemeal manner that misses potential variants.

C0deVari4nt provides a platform for developers to easily conduct variant analysis without the significant overhead of writing their own CodeQL queries. This gives developers the flexibility to customise CodeQL templates by providing codebase-specific information such as a particular source and sink of a vulnerability. The results will be visualised in a simplified Neo4j graph for developers to quickly identify potential variants. As such, developers will be able to effectively address entire classes of bugs from a single vulnerability report.

## Tool Components 
C0deVari4nt is built using python, CodeQL and Neo4j to create an interactive GUI application to take user input and showcase relationships between different vulnerable code paths.

C0deVari4nt consists of the following 3 main components:  
- **Variant-Inputs**: This module takes in a target CodeQL database zip file and user inputs of known source and sink functions to generate CodeQL queries to find bug variants. Alternatively, the module can generate queries from all source functions to Microsoft’s Security Development Lifecycle’s Banned String Copy functions. 
- **Variant-Query**: This module forms CodeQL query files from a set of predefined query templates using the inputted sources and sinks. The query files are then run on the provided target database to generate a sarif file object of potential vulnerable code paths.
- **Parse2Neo**: This module parses the extracted code paths to create nodes and relationships within the Neo4j interactive graph database. Nodes are categorised into their respective paths, sources and sinks through labels. The module is able to discern recurring steps between multiple code pathways and link them together to display any overlapping of steps.  

## Additional Features  
Currently, our tool uses a CLI interface built with Python to take user input. Since Neo4j supports integration with UI interfaces, we are looking to migrate the project to a desktop GUI application that will adopt Neo4j’s graph database view and also be able to query custom path perspectives relevant to CodeQL. In a way, our tool will work similarly to Bloodhound, an Active Directory path management solution also built upon Neo4j.

C0deVari4nt will be available as an open-source project to facilitate additional plugins and contributions in the form of query variant templates by the community to bring the tool to greater heights.

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

### Command-Line interface
![neo-1](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/CLI.png)  

## Simplifying CodeQL Results and Relationships between Nodes
The following depicts the CodeQL results for a query with recvfrom as a source, mempool_alloc as an additional taint step and memcpy as a sink:

![neo-1](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-1.png)  

This result yields a total of **180 nodes in more than 25 different paths** in Neo4j. Note that Blue nodes are sources and Red nodes are sinks: 

![neo-2](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-2.png)  

By putting this query through our tool, we were able to identify duplicate occurrences of each node, source and sink and merge the relationships of the nodes.  
This resulted in a significantly cleaner graph with a total of **11 unique nodes**:

![neo-3](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-3.png)  

The tool can further categorise each node into their different paths using Neo4j's built-in node labels:

![neo-4](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/neo-4.png)