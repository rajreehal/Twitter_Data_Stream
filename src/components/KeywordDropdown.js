import React from 'react';
import { useEffect, useState, useRef } from 'react'
import Select from 'react-select';

const KeywordDropdown = ({keywordChange}) => {
    const [keywords, setKeywords] = useState([])
    const [user, setUser] = useState()
    const keywordStreamIds = useRef()

    useEffect(() => {
        fetchKeywords()
    }, [])

    async function getData() {
        let res = await fetch('http://localhost:3000/api/getusersession', {
                method:'GET',
                credentials: 'include',
                headers: {
                'Content-Type':'application/json',
                },
                });
        return await res.json();
        }

    function fetchKeywords() {
        let user_data = ""
        let sesh = getData()
        sesh.then(function(result) {user_data = result["userinfo"]["sub"].substr(8)
                                    setUser(user_data)})
            .then(function() {
                fetch(`http://localhost:3000/api/getallkeywords/${user_data}`, {
                method:'GET',
                headers: {
                'Content-Type':'application/json',
                },  
                })
                .then(resp => resp.json())
                .then(function (data) {
                    if (data.length > 0) {
                        let ddValues = []
                        let ddValueStreamIDs = {}
                        for (var x in data) {
                            ddValues.push(data[x][0])
                            let values = (Object.entries(data[x][1]))
                            ddValueStreamIDs[values[0][0]] = values[0][1]
                        }
                        setKeywords(ddValues)
                        keywordStreamIds.current = ddValueStreamIDs
                    }})         
                })
            .catch(err => {
                console.error("Keyword stream fetch for failed.", err)
            })
    }
    
    return (
        <div className= 'keyword-dropdown'>
            <Select onChange={(e) => {keywordChange([e, user, keywordStreamIds.current])}} options={keywords} isMulti/>
        </div>
  )
}

export default KeywordDropdown