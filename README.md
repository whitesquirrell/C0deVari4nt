# C0deVari4nt 
![C0deVari4nt](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/icon.png) 

![Tool View](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/react-view.png) 


## Description
C0deVari4nt is a variant analysis and visualisation tool that inspects codebases for similar vulnerabilities. It leverages CodeQL, a semantic code analysis engine, to query code based on user-controlled CodeQL query templates and passes the results to our client interface built with vis.js and React for further exploration and visualisation. This enables quick and comprehensive variant analysis based on previous vulnerability reports. The vis.js visualisation feature provides additional insight for developers into vulnerable code paths and allows them to effectively triage potential variants.

## Motivations
The Log4Shell incident in December 2021 highlighted the difficulties open-source developers face in responding to vulnerability reports. After the initial patch for CVE-2021-44228, which allowed unauthenticated remote attackers to take control of devices running vulnerable versions of Log4j 2, Apache released 3 additional patches to address related vulnerabilities and unmitigated edge cases.

Open-source developers often lack training in comprehensive code review and face problems in identifying variants of a vulnerability, leading to incomplete patches. Although CodeQL query suites exist to facilitate quick analysis of the codebase, the results returned from these suites may result in significant false positive rates. Furthermore, these suites rely on predefined queries which do not support variant analysis and are not customised for individual codebases. As such, open-source projects often respond to vulnerability reports in a piecemeal manner that misses potential variants.

C0deVari4nt provides a platform for developers to easily conduct variant analysis without the significant overhead of writing their own CodeQL queries. This gives developers the flexibility to customise CodeQL templates by providing codebase-specific information such as a particular source and sink of a vulnerability. The results will be visualised in a simplified Neo4j graph for developers to quickly identify potential variants. As such, developers will be able to effectively address entire classes of bugs from a single vulnerability report.

## Tool Components 
C0deVari4nt is built using python, CodeQL, vis.js and React to create an interactive GUI application to take user input and showcase relationships between different vulnerable code paths.

![Tool Architecture](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/architecture.png) 

C0deVari4nt consists of the following 2 main components:  
- **Client Interface**: This component is built with React and the vis.js browser-based visualisation library. Users interact with this component to customise the CodeQL query and analyse CodeQL results through a graph visualisation view.
- **API Server**: This component is built upon the Python FastAPI web framework to receive requests from the client interface and run CodeQL commands against a list of CodeQL-ready database files. The server then returns the parsed data results back to the client interface.


More details of the client interface can be seen below:
![Tool Architecture](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/interface.png) 


# v1 Usage
## Setting up Database Folder
- cd into api-server directory and run `dbextractor.py <codeql db zip file>` to unzip the codeql database contents

## Running Backend Server
- cd into api-server
- download dependencies `pip install -r requirements.txt`
- run `uvicorn main:app --reload` to start local developmental server on port 8000

## Run React Interface
- cd into react-gui
- download dependencies `npm i`
- run `npm  start` to start local developmental server


## Using the Tool
![User Process](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/user-process.png) 

- input your query options into the options box and click apply
- wait a few seconds for backend to process the request
- use right properties box to isolate paths and view node properties

## Usage
### Run Codebase against predefined vulnerable sources and sinks
1. Query and find all source functions to banned string functions based on Microsoft's Security Development Lifecycle (SDL) Banned Function Calls
    1. Developer wants to check codebase against Microsoft's Security Development Lifecycle (SDL) Banned Function Calls
2. Query and find all strcat functions without bound checks on the source argument
    1. Developer wants to find all strcat function without bound check on the size of the source string
3. Query and find all strncpy functions without bound checks on the source argument
    1. Developer wants to find all strncpy function calls without bound check on the size of the source buffer  
4. Query and find all cases with no bound checks on the return value of a call to snprintf
    1. Developer wants to find all cases with no bound checks on the return value of a call to snprintf. Eg: When the operation reaches the end of the buffer and more than 1 char is discarded, the return value will be greater than the buffer size
5. Query and find all calls to malloc, calloc or realloc without sufficient memory allocated to contain an instance of the type of the pointer
    1. Developer wants to find all calls to malloc, calloc or realloc without sufficient memory allocated to contain an instance of the type of the pointer which may result in a buffer overflow

### Run Codebase against sources and sinks of your choice (based on the bug you want to find)
1. Query user input source, sink and sink argument. 
    1. Developer knows the source and sink information
2. Query all source expressions to user input sink and argument.
    1. Developer only knows the sink function and argument.
3. Query user input vulnerable source and sink information whereby the source is tainted.
    1. Developer is trying to find a bug whereby the user input variable is tainted. For instance, developer is trying to find paths whereby the `recvfrom` function value is used in `memcpy` sizeof Argument. However, these 2 nodes are not connected as the variable holding the `recvfrom` value is dereferenced and stored in another variable before the memcpy function. If we were to use the first query, no results will be returned. Instead, we can force the 2 nodes to connect by using `isAdditionalTaintStep` in this query template to catch the tainted source.

## Simplifying CodeQL Results and Relationships between Nodes
The following depicts the CodeQL results for a query with recvfrom as a source, mempool_alloc as an additional taint step and memcpy as a sink:

![neo-1](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/codevariant-1.png)  

This result yields a total of **180 nodes in 27 different code paths**. The results are portrayed in a simple neo4j interface below:

![neo-2](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/codevariant-2.png)  

By putting this query through our tool, we were able to identify duplicate occurrences of each node, source and sink and merge the relationships of the nodes.  
This resulted in a significantly cleaner graph with a total of **11 unique nodes** while still retaining all 27 unique code paths:

![neo-3](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/codevariant-3.png)  

The results can be further categorised into their respective paths through our path labelling feature:

![neo-4](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/codevariant-4.png)
