
# C0deVari4nt

## Overview
C0deVari4nt is a variant analysis and visualisation tool that scans the codebase for similar bugs. Variant analysis is the process of taking a known problem, such as a crashing bug or security vulnerability, and finding other occurrences (or "variants") of that problem in a codebase.
With C0deVari4nt, users will be able to:
- Query a codebase based on predefined vulnerable sources and sinks 
- Query a codebase based on user input sources and sinks
- Flag, filter and extract out potential variants of vulnerabilities found into a visualisation tool

## Tool Description
C0deVari4nt is a variant analysis and visualisation tool that inspects codebases for similar vulnerabilities. It leverages CodeQL, a semantic code analysis engine, to query code based on user-controlled CodeQL query templates and passes the results to Neo4j for further exploration and visualisation. This enables quick and comprehensive variant analysis based on previous vulnerability reports. The Neo4j visualisation feature provides additional insight for developers into vulnerable code paths and allows them to effectively triage potential variants. 

The Log4Shell incident in December 2021 highlighted the difficulties open-source developers face in responding to vulnerability reports. After the initial patch for CVE-2021-44228, which allowed unauthenticated remote attackers to take control of devices running vulnerable versions of Log4j 2, Apache released 3 additional patches to address related vulnerabilities and unmitigated edge cases.

Open-source developers often lack training in comprehensive code review and face problems in identifying variants of a vulnerability, leading to incomplete patches. Although CodeQL query suites exist to facilitate quick analysis of the codebase, the results returned from these suites may result in significant false positive rates. Furthermore, these suites rely on predefined queries which do not support variant analysis and are not customised for individual codebases. As such, open-source projects often respond to vulnerability reports in a piecemeal manner that misses potential variants.

C0deVari4nt provides a platform for developers to easily conduct variant analysis without the significant overhead of writing their own CodeQL queries. This gives developers the flexibility to customise CodeQL templates by providing codebase-specific information such as a particular source and sink of a vulnerability. The results will be visualised in a simplified Neo4j graph for developers to quickly identify potential variants. As such, developers will be able to effectively address entire classes of bugs from a single vulnerability report.

## Tool Details
C0deVari4nt is built using Python, CodeQL, and Neo4j to create an interactive GUI application that takes user input and showcases relationships between different vulnerable code paths.

C0deVari4nt consists of the following 3 main components:

- Variant-Inputs: This module takes in a target CodeQL database zip file and user inputs of known source and sink functions to generate CodeQL queries to find bug variants. Alternatively, the module can generate a query from all source functions to  Microsoft’s Security Development Lifecycle’s Banned String Copy functions.
- Variant-Query: This module forms CodeQL query files from a set of predefined query templates using the inputted sources and sinks. The query files are then run on the provided target database to generate a sarif file object of potentially vulnerable code paths.
- Parse2Neo: This module parses the extracted code paths to create nodes and relationships within the Neo4j interactive graph database. Nodes are categorised into their respective paths, sources, and sinks through labels. The module can discern recurring steps between multiple code pathways and link them together to display any overlapping of steps. 

Currently, our tool uses a CLI interface built with Python to take user input. Since Neo4j supports integration with UI interfaces, we are looking to migrate the project to a desktop GUI application that will adopt Neo4j’s graph database view and also be able to query custom path perspectives relevant to CodeQL. In a way, our tool will work similarly to Bloodhound, an Active Directory path management solution also built upon Neo4j.

C0deVari4nt will be available as an open-source project to facilitate additional plugins and contributions in the form of query variant templates by the community to bring the tool to greater heights.

## Implementation
### Generating Queryable CodeQL source codebase
- Developers will need to make their projects open source in Git repositories in order to use CodeQL to query the codebase. In future implementations, C0deVari4nt will help to generate CodeQL queryable codebase to allow users to keep their repositories private but at the same time be able to leverage on CodeQL to find bugs.

### Generating CodeQL Queries 
- Predefined CodeQL query templates will be used to query the codebase based on the user inputs.

### CodeQL results passed to Neo4j
- Our tool will be able to identify duplicate occurrences of each node, source and sink and merge the relationships of the nodes. This results in a much cleaner graph and allows developers to quickly identify potential variants.


## User Flow
1. Run the tool with the database zip file as an argument
2. User is prompted on whether they want to query predefined sources and sinks or input their own sources and sinks

	![](https://i.imgur.com/G9D3BhQ.png)
	- If the user chooses option 1, our tool will run a query to find all source expressions to the following Microsoft Security Development Lifecycle of Banned string copy functions (More templates to be implemented) 

	- If the user chooses option 2, the user will be prompted to choose one of the 3 options based on the following:
		- Query user input source, sink and sink argument.
			- Developer knows the source and sink information
		- Query all source expressions to user input sink and argument.
			- Developer only knows the sink function and argument.
		- Query user input vulnerable source and sink information whereby the source is tainted.
			- Developer is trying to find a bug whereby the user input variable is tainted. For instance, the developer is trying to find paths whereby the `recvfrom` function value is used in `memcpy` sizeof Argument. However, these 2 nodes are not connected as the variable holding the `recvfrom` value is dereferenced and stored in another variable before the memcpy function. If we were to use the first query, no results will be returned. Instead, we can force the 2 nodes to connect by using `isAdditionalTaintStep` in this query template to catch the tainted source.

3. After the user has chosen their options, our tool will edit the CodeQL predefined templates accordingly and run them.

4. Once CodeQL has successfully analysed the codebase, the data will be stored in a JSON file in SARIF format. Further filtering of the JSON file will be done and duplicated nodes and paths will be removed and displayed in Neo4j. 
	![](https://i.imgur.com/wtlGhWU.png)

## Command-line interface:
![](https://i.imgur.com/aZpHuXW.png)

## Case Study
We tested our tool on Accel-PPP codebase and managed to obtain 3 CVEs from it. Via manual code review we realised that there is a memory corruption vulnerability from `mempool_alloc` to `recvfrom` and to `memcpy` whereby user input `len` is copied into a fixed buffer `&attr->val.integer` without any bound checks. Using this information, we used the first query to input the source as `mempool_alloc` and sink as `memcpy`. From the simplified results returned by the graph, we were able to find another vulnerability in the same file. This time, user input `len` is copied into another fixed sized buffer `&attr->val.ipv6prefix.prefix`
![](https://i.imgur.com/XPV9aFq.png)

## Simplifying CodeQL Results and Relationships between Nodes
The following depicts the CodeQL results for a query with `recvfrom` as a source, `mempool_alloc` as an additional taint step and `memcpy` as a sink:
![](https://i.imgur.com/MpcFuRK.png)


This result yields a total of **180 nodes** in more than 25 different paths in Neo4j. Note that Blue nodes are sources and Red nodes are sinks:
![](https://i.imgur.com/b2RwljZ.png)

By putting this query through our tool, we were able to identify duplicate occurrences of each node, source and sink and merge the relationships of the nodes. This resulted in a significantly cleaner graph with a total of **11 unique nodes**:
![](https://i.imgur.com/h2zpwlw.png)

The tool can further categorise each node into their different paths using Neo4j's built-in node labels:
![](https://i.imgur.com/q3Jzro5.png)


## Limitations
### Lack of sufficient CodeQL query templates
- For now, we will be relying on a few query templates. However, C0deVari4nt will be available as an open-source project to facilitate additional plugins and contributions in the form of query variant templates by the community.
### Predefined Vulnerable sources and sinks
- We will be relying on Microsoft’s Security Development Lifecycle (SDL) Banned Function Calls for predefined vulnerable sources and sinks. In the long run, we will conduct a study of all CVEs and extract relevant sources and sinks to generate CodeQL queries via machine learning.
### Targeted on C codebase
- Currently, our tool is targeted at C/C++ codebases but this will be expanded in the long run.

## References
- Berger, A., 2021. What is Log4Shell? The Log4j vulnerability explained (and what to do about it). [online] Dynatrace news. Available at: <https://www.dynatrace.com/news/blog/what-is-log4shell/> [Accessed 20 January 2022].
- Freebuf 2021. CodeQL from entry to abandonment. [online] Available at: <https://www.freebuf.com/articles/web/283795.html> [Accessed 20 January 2022].
- Codeql Analyzing data flow in C and C++ — CodeQL. [online] Available at: <https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-cpp/#analyzing-data-flow-in-cpp> [Accessed 20 January 2022].
- Menzel, G. and Lanning, S., 2021. Variant Analysis - DZone Refcardz. [online] dzone.com. Available at: <https://dzone.com/refcardz/variant-analysis-1#:~:text=Variant%20analysis%20is%20the%20process,that%20problem%20in%20a%20codebase.> [Accessed 20 January 2022].

## Acknowledgement
- Chloe Ong - https://www.linkedin.com/in/chloe-ong-wt/
- Loh Kar Wei - https://www.linkedin.com/in/kar-wei-loh/
