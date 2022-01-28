import React, { useEffect } from 'react';
import {useSelector} from 'react-redux'

import "../../css/hud.css"

function HUD () {


    const activeNode = useSelector((state) => {
        return state.activeNode
    })


    const generatePropsTable = () => {
        console.log(activeNode)
        if (activeNode){
            return (
                <table id='prop-table' className='red'>
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
                            <th>{activeNode.all_labels.join(", ")}</th>
                        </tr>
                    </tbody>
                </table>      
            )
        }
        
    }

    return (
        <div id='node-props' className='red'>
            <p className='section-title'>Properties</p>
            {generatePropsTable()}
        </div>
    )
}

export default HUD