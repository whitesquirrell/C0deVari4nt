import React, { useEffect } from 'react';
import {useSelector, useDispatch} from 'react-redux'
import {DataSet} from "vis-data";

import "../../css/hud.css"
import data from "../../data/vis.json";

function HUD () {
    const dispatch = useDispatch();

    const activeNode = useSelector((state) => {
        return state.activeNode
    })

    const network = useSelector((state) => {
        return state.network
    })

    const visNodes = useSelector((state) => {
        return state.visNodes
    })

    const initialNodeOptions = useSelector((state) => {
        return state.initialNodeOptions
    })


    const generatePropsTable = () => {
        if (activeNode){
            return (
                <table id='prop-table' className=''>
                    <tbody>
                        <tr>
                            <th>id</th>
                            <th>{activeNode.id}</th>
                        </tr>
                        <tr>
                            <th>code</th>
                            <th>{activeNode.code_line}</th>
                        </tr>
                        <tr>
                            <th>location</th>
                            <th>{`${activeNode.file_path}:${activeNode.file_line}`}</th>
                        </tr>
                        <tr>
                            <th>labels</th>
                            <th>{activeNode.all_labels}</th>
                        </tr>
                    </tbody>
                </table>      
            )
        }   
    }

    const selectPath = (path) => {
        if(path == "Step"){
            let new_nodes = new DataSet(data["nodes"])
            let edges = new DataSet(data["edges"])
            network.setData({
                nodes: new_nodes,
                edges: edges
            })
            dispatch({type: "NODES_DATASET", payload: new_nodes})
            return
        }

        let nodes = network.body.nodes;
        console.log(nodes)

        let nodesToUpdate = [];

        for (const [key, val] of Object.entries(nodes)){
            if(! isNaN(key)){
                // console.log(key, val);
                
                // console.log(val['options'])
                let options = val['options'];
                let nodeLabels = val['options']['all_labels'];
                nodeLabels = nodeLabels.split(", ");

                // console.log(nodeLabels)
                if (nodeLabels.includes(`${path} Source`)){
                    options['color'] = {
                        "background": "#89ECB7", "border": "#2DC775",
                        "highlight": {"background": "#A4A3A3", "border": "#686565"}
                    }
                }
                else if (nodeLabels.includes(`${path} Sink`)){
                    options['color'] = {
                        "background": "#EC8989", "border": "#DF5959",
                        "highlight": {"background": "#A4A3A3", "border": "#686565"}
                    }
                }
                else if (nodeLabels.includes(path)){
                    // console.log(key, val)
                    options['color'] = {
                        "background": "#899EEC", "border": "#5875e0",
                        "highlight": {"background": "#A4A3A3", "border": "#686565"}
                    }
                    // console.log("changed colour for ", key)
                }
                else{
                    options['color'] = {
                        "background": "#F6EDB5", "border": "#E9D86F",
                        "highlight": {"background": "#A4A3A3", "border": "#686565"}
                    }
                }
                nodesToUpdate.push(options)
            }
        }

        visNodes.update(nodesToUpdate)
    }


    const generatePathsButtons = () => {
        let maxPaths = data["max-paths"]

        let pathButtons = []
        for(let i = 1; i <= maxPaths; i ++){
            pathButtons.push(<div className='label-button path-label-button'
                onClick={() => {selectPath(`Path-${i}`)}}
            >
                <p className=''>{`Path-${i}`}</p>
            </div>)
        }
        return pathButtons
    }

    const generateLabelButtons = () => {

        return (<div id='label-buttons-container' className=''>
                    <div className='label-button step-label-button'
                        onClick={() => {selectPath("Step")}}
                    >
                        <p className=''>*</p>
                    </div>
                    <div className='label-button source-label-button'
                        onClick={() => {selectPath("Source")}}
                    >
                        <p className=''>Source</p>
                    </div>
                    <div className='label-button sink-label-button'
                        onClick={() => {selectPath("Sink")}}
                    >
                        <p className=''>Sink</p>
                    </div>
                    {generatePathsButtons()}
                </div>)
    }

    return (
        <div id='node-props' className=''>
            <div>
                <p className='section-title'>Paths</p>

                {generateLabelButtons()}

            </div>

            <div>
                <p className='section-title'>Properties</p>
                {generatePropsTable()}
            </div>
            
        </div>
    )
}

export default HUD