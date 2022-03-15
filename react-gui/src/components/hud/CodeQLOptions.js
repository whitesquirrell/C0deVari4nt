import React, { useEffect, useState } from 'react';
import {useSelector, useDispatch} from 'react-redux'

import "../../css/codeqloptions.css"

function CodeQLOptions(){

    const dispatch = useDispatch();

    const backendUrl = useSelector((state) => {
        return state.backendUrl
    })

    const [showOptions, setShowOptions] = useState(false)
    const [customQueryFields, setCustomQueryFields] = useState("1")

    const [selectedDatabase, setSelectedDatabase] = useState("accel-ppp")
    const [selectedOption, setSelectedOption] = useState(1)
    const [selectedCategory, setSelectedCategory] = useState(1)
    const [selectedSource, setSelectedSource] = useState("")
    const [selectedSourceArg, setSelectedSourceArgIndex] = useState("")
    const [selectedSink, setSelectedSink] = useState("")
    const [selectedSinkArgIndex, setSelectedSinkArgIndex] = useState("")
    const [selectedTaint, setSelectedTaint] = useState("")

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
                        value={selectedOption}
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

    const showCustomQueryFields = () => {
        switch(customQueryFields){
            case "1":
                return (<div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink</p>
                        <input type="text" placeholder='memcpy'
                            onChange={(e) => {setSelectedSink(e.target.value)}}
                            value={selectedSink}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink Arg Index</p>
                        <input type="text" placeholder='2'
                            onChange={(e) => {setSelectedSinkArgIndex(e.target.value)}}
                            value={selectedSinkArgIndex}
                        />
                    </div>
                </div>)
                break;
            case "2":
                return (<div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Source</p>
                        <input type="text" placeholder='recvfrom'
                            onChange={(e) => {setSelectedSource(e.target.value)}}
                            value={selectedSource}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink</p>
                        <input type="text" placeholder='memcpy'
                            onChange={(e) => {setSelectedSink(e.target.value)}}
                            value={selectedSink}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink Arg Index</p>
                        <input type="text" placeholder='2'
                            onChange={(e) => {setSelectedSinkArgIndex(e.target.value)}}
                            value={selectedSinkArgIndex}
                        />
                    </div>
                </div>)
                break;
            case "3":
                return (<div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Source</p>
                        <input type="text" placeholder='recvfrom'
                            onChange={(e) => {setSelectedSource(e.target.value)}}
                            value={selectedSource}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Source Arg Index</p>
                        <input type="text" placeholder='1'
                            onChange={(e) => {setSelectedSourceArgIndex(e.target.value)}}
                            value={selectedSourceArg}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Taint Function</p>
                        <input type="text" placeholder='mempool_alloc'
                            onChange={(e) => {setSelectedTaint(e.target.value)}}
                            value={selectedTaint}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink</p>
                        <input type="text" placeholder='memcpy'
                            onChange={(e) => {setSelectedSink(e.target.value)}}
                            value={selectedSink}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink Arg Index</p>
                        <input type="text" placeholder='2'
                            onChange={(e) => {setSelectedSinkArgIndex(e.target.value)}}
                            value={selectedSinkArgIndex}
                        />
                    </div>
                </div>)
                break;
            case "4":
                return (<div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Source</p>
                        <input type="text" placeholder='recvfrom'
                            onChange={(e) => {setSelectedSource(e.target.value)}}
                            value={selectedSource}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Source Arg Index</p>
                        <input type="text" placeholder='1'
                            onChange={(e) => {setSelectedSourceArgIndex(e.target.value)}}
                            value={selectedSourceArg}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink</p>
                        <input type="text" placeholder='memcpy'
                            onChange={(e) => {setSelectedSink(e.target.value)}}
                            value={selectedSink}
                        />
                    </div>
                    <div className='options-field-container'>
                        <p className='section-label' className=''>Sink Arg Index</p>
                        <input type="text" placeholder='2'
                            onChange={(e) => {setSelectedSinkArgIndex(e.target.value)}}
                            value={selectedSinkArgIndex}
                        />
                    </div>
                </div>)
                break;
        }
    }


    const sendQLOptions = () => {
        console.log("Sending POST req to backend")
        fetch(backendUrl + "/query/run", {
            method: "POST",
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                database: selectedDatabase,
                option: selectedOption,
                category: selectedCategory,
                custom_query: customQueryFields,
                source: selectedSource,
                source_index: selectedSourceArg,
                sink: selectedSink,
                sink_index: selectedSinkArgIndex,
                taint: selectedTaint
            })
        })
        .then(resp => resp.json())
        .then(resp => {
            dispatch({type: "SET_DATA", payload: resp})
            console.log("Received vis Data object")
            console.log(resp)
        })
    }

    const displaySubOptions = () => {
        if(selectedOption == 1){
            return (<div>
                <div className='options-field-container'>
                    <p className='section-label' className=''>Category</p>
                    <select className='custom-select'
                        onChange={(e) => {setSelectedCategory(e.target.value)}}
                        value={selectedCategory}
                    >
                        <option value='1' >Find all source functions to banned string copy functions</option>
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
                    <p className='section-label' className=''>Custom Query</p>
                    <select className='custom-select'
                        onChange={(e) => {setCustomQueryFields(e.target.value)}}
                        value={customQueryFields}
                    >
                        <option value='1' selected={customQueryFields=="1"}>Query all sources to a dangerous sink</option>
                        <option value='2' selected={customQueryFields=="2"}>Query a specific source to a dangerous sink</option>
                        <option value='3' selected={customQueryFields=="3"}>Query a specific source to a dangerous sink (Tainted function)</option>
                        <option value='4' selected={customQueryFields=="4"}>Query a specific source to a dangerous sink (Tainted expression)</option>
                    </select>
                </div>
                {showCustomQueryFields()}
            </div>)
        }
    }
    
    return (<div id='options-container' className=''>
        {displayOptions()}
    </div>)
}

export default CodeQLOptions