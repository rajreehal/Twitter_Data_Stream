import React from 'react';
import { useState, useEffect } from 'react'
import AddKeyword from './../components/AddKeyword'
import Keywords from './../components/Keywords'
import './tracker.css'

function Tracker() {
    const [keywords, setKeywords] = useState([])
    const [loadpage, setLoadpage] = useState([])

    useEffect(() => {
        fetchKeywords();
    }, [loadpage])

    async function getData() {
        let res = await fetch('/api/getusersession', {
              method:'GET',
              credentials: 'include',
              headers: {
              'Content-Type':'application/json',
              },
              });
        return await res.json();
                
      }

    const fetchKeywords = () => {
        let user_data = ""
        let sesh = getData()
        sesh.then(function(result) {user_data = result["userinfo"]["sub"].substr(8)})
            .then(function() {
                fetch(`/api/get/${user_data}`, {
                method:'GET',
                headers: {
                'Content-Type':'application/json',
                },  
                })
                .then(resp => resp.json())
                .then(data => setKeywords(data))
                })
            .catch(err => {
                console.error("Keyword stream fetch failed.", err)
            })
    }   

    // Delete streams
    async function deleteStream(id) {
        await fetch(`/api/delete/${id}`, {
            method:'DELETE',
            mode: 'cors',
            headers: {
            'Content-Type':'application/json',
            },
        });
        setKeywords(keywords.filter((keyword) => keyword.id !== id))
        }

    // Add streams
    const addStream = (keyword) => {
        fetch('/api/add', {
            method:'POST',
            mode: 'cors',
            headers: {
            'Content-Type':'application/json',
            },
            body: JSON.stringify(keyword)
            })
            .then((res => {setLoadpage(res)}));
        }

    return (
        <div className="tracker">
            <div className="keyword-search">
                <p className='header'>Gossip Streams</p>
                <AddKeyword onAdd={addStream} keywords={keywords}/>
            </div>
            <div className='keyword-list'>
                {keywords.length > 0 ? <Keywords keywords={keywords} onDelete={deleteStream} />: <div className='not-streaming-message'> There is no gossip being tracked </div>}
            </div>
        </div>
  )
}

export default Tracker;