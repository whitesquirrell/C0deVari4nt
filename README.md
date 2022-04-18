# C0deVari4nt 
![C0deVari4nt](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/icon.png) 

## Description
C0deVari4nt is a variant analysis and visualisation tool that inspects codebases for similar vulnerabilities. It leverages CodeQL, a semantic code analysis engine, to query code based on user-controlled CodeQL query templates and passes the results to our client interface built with vis.js and React for further exploration and visualisation. This enables quick and comprehensive variant analysis based on previous vulnerability reports. The vis.js visualisation feature provides additional insight for developers into vulnerable code paths and allows them to effectively triage potential variants.

![Tool View](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/react-view.png) 

## Motivations
The Log4Shell incident in December 2021 highlighted the difficulties open-source developers face in responding to vulnerability reports. After the initial patch for CVE-2021-44228, which allowed unauthenticated remote attackers to take control of devices running vulnerable versions of Log4j 2, Apache released 3 additional patches to address related vulnerabilities and unmitigated edge cases.

Open-source developers often lack training in comprehensive code review and face problems in identifying variants of a vulnerability, leading to incomplete patches. Although CodeQL query suites exist to facilitate quick analysis of the codebase, the results returned from these suites may result in significant false positive rates. Furthermore, these suites rely on predefined queries which do not support variant analysis and are not customised for individual codebases. As such, open-source projects often respond to vulnerability reports in a piecemeal manner that misses potential variants.

C0deVari4nt provides a platform for developers to easily conduct variant analysis without the significant overhead of writing their own CodeQL queries. This gives developers the flexibility to customise CodeQL templates by providing codebase-specific information such as a particular source and sink of a vulnerability. The results will be visualised in a graph database view powered by vis.js for developers to quickly identify potential variants. As such, developers will be able to effectively address entire classes of bugs from a single vulnerability report.

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
- Download dependencies `pip install -r requirements.txt`
- Run `uvicorn main:app --reload` to start local developmental server on port 8000

## Run React Interface
- cd into react-gui
- Download dependencies `npm i`
- Run `npm  start` to start local developmental server


## Using the Tool
![User Process](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/user-process.png) 

- Input your query options into the options box and click apply
- Wait a few seconds for backend to process the request
- Use right properties box to isolate paths and view node properties

## Usage
### Run Codebase against predefined vulnerable sources and sinks (Option 1) 
1. Find all source functions to banned string functions (based on Microsoft's Security Development Lifecycle (SDL) Banned Function Calls)
2. Find all calls to `strcat` functions without bound checks on the source argument
3. Find all calls to `strncpy` functions without bound checks on the source argument
4. Find all cases with no bound checks on the return value of a call to `snprintf`
    1. Eg: When the operation reaches the end of the buffer and more than 1 char is discarded, the return value will be greater than the buffer size
5. Find all calls to `malloc`, `calloc` or `realloc` without sufficient memory allocated to contain an instance of the type of the pointer

### Run Codebase against sources and sinks of your choice (Option 2)
1. Find all source expressions to a dangerous sink function
2. Find a specific source function to a dangerous sink function
3. Find a specific source function to a dangerous sink function (Tainted function)
    1. Use the `isAdditionalTaintStep` method to transfer taints between 2 disconnected functions
4. Find a specific source function to a dangerous sink function (Tainted expression)
    1. Use the `isAdditionalTaintStep` method to transfer taints between pointers which have the same values at runtime

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

![codevariant](https://github.com/whitesquirrell/C0deVari4nt/blob/main/images/codevariant.gif)
