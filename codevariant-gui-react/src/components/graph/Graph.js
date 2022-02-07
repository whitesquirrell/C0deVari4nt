import React, { useEffect } from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { Network } from "vis-network";
import {DataSet} from "vis-data";
import data from "../../data/vis.json";


function Graph () {
    const dispatch = useDispatch();

    const spawnNodes = (data) => {   
        
        // console.log(data)
        let nodes = []

        // for (var i = 0; i < data["nodes"].length; i ++){
        //     console.log(data["nodes"][i])
        // }

        nodes = new DataSet(data["nodes"])

        // var nodes = new DataSet([
        //     { id: 1, label: "Node: 1\nGroup: 1", group: "yes", labels: ["bruyhu", "dhjf"] },
        //     { id: 2, label: "Node: 2\nGroup: 1", group: "yes" },
        //     { id: 3, label: "Node: 3\nGroup: 1", group: 1 },
        //     { id: 4, label: "Node: 4\nGroup: 1", group: 1 },
        //     { id: 5, label: "Node: 5\nGroup: 2", group: 2 },
        //     {
        //         id: 6,
        //         label: "Node: 6\nGroup: 2\nCustom background",
        //         group: 2,
        //         color: { background: "#003d3d" },
        //     },
        //     {
        //         id: 7,
        //         label: "Node: 7\nGroup: 2\nCustom border",
        //         group: 2,
        //         color: { border: "#00d3d3" },
        //     },
        //     { id: 8, label: "Node: 8\nGroup: 2", group: 2 },
        //     { id: 9, label: "Node: 9\nGroup: 3", group: 3 },
        //     { id: 10, label: "Node: 10\nGroup: 3", group: 3 },
        //     { id: 11, label: "Node: 11\nGroup: 4", group: 4, bruh: "yes" },
        //     { id: 12, label: "Node: 12\nGroup: 4", group: 4 },
        // ])
        // var edges = new DataSet([
        //     { from: 1, to: 2 },
        //     { from: 2, to: 3 },
        //     { from: 3, to: 4 },
        //     { from: 4, to: 5 },
        //     { from: 5, to: 6 },
        //     { from: 6, to: 7 },
        //     { from: 7, to: 8 },
        //     { from: 8, to: 9 },
        //     { from: 9, to: 10 },
        //     { from: 10, to: 11 },
        //     { from: 11, to: 12 },
        //     { from: 12, to: 1 },
        // ]);
        let edges = new DataSet(data["edges"])

        // create a network
        var container = document.getElementById("mynetwork");
        var data = {
            nodes: nodes,
            edges: edges,
        };
        var options = {
            nodes: {
                shape: "dot",
                size: 30,
                font: {
                size: 32,
                color: "#ffffff",
                },
                borderWidth: 2,
            },
            edges: {
                width: 2,
                arrows: "to",
            },
            physics: false
        };
        var network = new Network(container, data, options);
        dispatch({type: "INIT_NETWORK", payload: network})
        dispatch({type: "NODES_DATASET", payload: nodes})
        dispatch({type: "INIT_NODE_OPTIONS", payload: network.body.nodes})

        network.on("click", (prop) => {
            let ids = prop.nodes;
            let clickedNodes = nodes.get(ids)
            console.log('clicked nodes:', clickedNodes[0]);
            dispatch({type: "SELECT_NODE", payload: clickedNodes[0]})
        })
    }

    useEffect(() => {
        spawnNodes(data)
    })
    
    return (
        <div id="mynetwork">
            
        </div>
    );
    
}
 
export default Graph;