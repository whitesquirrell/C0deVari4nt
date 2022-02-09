import React, { useEffect } from 'react';
import {useDispatch, useSelector} from 'react-redux'
import { Network } from "vis-network";
import {DataSet} from "vis-data";
// import data from "../../data/vis.json";


function Graph () {
    const dispatch = useDispatch();

    const visData = useSelector((state) => {
        return state.visData
    })

    const spawnNodes = () => {   
        if(visData){
            // console.log(data)
            let nodes = []

            nodes = new DataSet(visData["nodes"])

            let edges = new DataSet(visData["edges"])

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
                // console.log('clicked nodes:', clickedNodes[0]);
                dispatch({type: "SELECT_NODE", payload: clickedNodes[0]})
            })
        }
        
    }

    // useEffect(() => {
    //     spawnNodes(data)
    // })
    
    return (
        <div id="mynetwork">
            {spawnNodes()}
        </div>
    );
    
}
 
export default Graph;