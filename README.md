# C0deVari4nt 
A tool that automates the process of variant analysis through CodeQL queries and Neo4j visualisation

## CodeQL
There will be a few predefined CodeQL query templates that we will be leveraging on
1. User inputs vulnerable source, sink and sink argument. C0deVari4nt will use this information to query the CodeQL template and pass the results to Neo4j.
2. User inputs vulnerable sink and argument. C0deVarin4t will use this information to search for all source expressions to the vulnerable sink and pass the results to Neo4j.

## Neo4j
- Install neo4j locally on computer and create database `CodeVariant` with password `codevariant`
- Start the CodeVariant instance
- Run the C0deVariant tool and input your options
- Once the tool has finished analysing your input, run `MATCH (n) RETURN n` in neo4j at http://localhost:7474/browser/ to get all nodes

## Run C0deVari4nt
- `python3 codevariant.py C:\Users\asien\Downloads\xebd_accel-ppp_cpp-srcVersion_1b8711cf75a7c278d99840112bc7a396398e0205-dist_codeql-bundle-linux64-20211202-1530398226.zip`
