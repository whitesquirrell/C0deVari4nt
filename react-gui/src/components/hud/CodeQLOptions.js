import React, { useEffect, useState } from 'react';
import {useSelector, useDispatch} from 'react-redux'

import "../../css/codeqloptions.css"

function CodeQLOptions(){

    const [showOptions, setShowOptions] = useState(false)

    const [selectedDatabase, setSelectedDatabase] = useState("accel-ppp")
    const [selectedOption, setSelectedOption] = useState(1)
    const [selectedCategory, setSelectedCategory] = useState(1)
    const [selectedSource, setSelectedSource] = useState("recvfrom")
    const [selectedSourceArg, setSelectedSourceArgIndex] = useState(1)
    const [selectedSink, setSelectedSink] = useState("memcpy")
    const [selectedSinkArgIndex, setSelectedSinkArgIndex] = useState(2)
    const [selectedTaint, setSelectedTaint] = useState("mempool_alloc")

    const displayOptions = () => {
        if(showOptions){
            return (<div id='ql-options' className=''>
                <div className='options-field-container'>
                    <p className='section-label' className=''>CodeQL Database</p>
                    {/* <label for="file-upload" className="custom-file-upload red">
                        <i className="fa fa-cloud-upload"></i> Upload Database Zip
                    </label>
                    <input id="file-upload" type="file"/> */}
                    <select className='custom-select'
                        onChange={(e) => {setSelectedDatabase(e.target.value)}}
                    >
                        <option value='accel-ppp'>Accel-PPP</option>
                    </select>
                </div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Option</p>
                    <select className='custom-select'
                        onChange={(e) => {setSelectedOption(e.target.value)}}
                    >
                        <option value='1'>1</option>
                        <option value='2'>2</option>
                    </select>
                </div>
                <span className='div-line'></span>
                {displaySubOptions()}
                <div className='options-field-container'>
                    <a className='options-btn'
                        onClick={() => {setShowOptions(false)}}
                    >Close</a>
                    <a className='options-btn'
                        onClick={sendQLOptions}
                    >Apply</a>
                </div>
            </div>)
        }else{
            return(<div className="hamburger-lines"
                onClick={() => {setShowOptions(true)}}
            >
                <span className="line"></span>
                <span className="line"></span>
                <span className="line"></span>
            </div>)
        }
    }


    const sendQLOptions = () => {
        console.log(selectedDatabase)
        console.log(selectedSource)
    }

    const displaySubOptions = () => {
        if(selectedOption == 1){
            return (<div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Category</p>
                    <select className='custom-select'
                        onClick={(e) => {setSelectedCategory(e.target.value)}}
                    >
                        <option value='1'>Find all source functions to banned string copy functions</option>
                        <option value='2'>Find all calls to strcat without checking the size of the source string</option>
                        <option value='3'>Find all calls to strncat with the size of the source buffer as third argument</option>
                        <option value='4'>Find all cases with no bound checks on the return value of a call to snprintf</option>
                        <option value='5'>Find all calls to malloc, calloc or realloc without sufficient memory allocated to contain an instance of the type of the pointer</option>
                    </select>
                </div>
            </div>)
        }else if (selectedOption == 2){
            return (<div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Source</p>
                    <input type="text" placeholder='recvfrom'
                        onChange={(e) => {setSelectedSource(e.target.value)}}
                    />
                </div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Source Arg Index</p>
                    <input type="text" placeholder='1'
                        onChange={(e) => {setSelectedSourceArgIndex(e.target.value)}}
                    />
                </div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Sink</p>
                    <input type="text" placeholder='memcpy'
                        onChange={(e) => {setSelectedSink(e.target.value)}}
                    />
                </div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Sink Arg Index</p>
                    <input type="text" placeholder='2'
                        onChange={(e) => {setSelectedSinkArgIndex(e.target.value)}}
                    />
                </div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Taint Function</p>
                    <input type="text" placeholder='mempool_alloc'
                        onChange={(e) => {setSelectedTaint(e.target.value)}}
                    />
                </div>
            </div>)
        }
    }
    
    return (<div id='options-container' className=''>
        {displayOptions()}
    </div>)
}

export default CodeQLOptions