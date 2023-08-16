import { useState } from 'react';
import Loader from './Loader';
import './../pages/tracker.css'

const AddKeyword = ({ onAdd, keywords }) => {
    const [keyword, setKeyword] = useState('')
    const [geography, setGeography] = useState('')
    const [isFetching, setIsFetching] = useState(false);

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
    
    const onSubmit = (e) => {
        
        e.preventDefault()
        
        if(!keyword) {
            alert('Please add a keyword to stream')
            return
        }

        if (keywords.length > 2) {
            alert('Only 3 keywords/phrases can be streamed concurrently.')
            return
        }
        
        setIsFetching(() => {setIsFetching(true)})
        let sessionUser = ""
        function getSessionUser() {
            let sesh = getData()
            sesh.then(function(result) {sessionUser = (result["userinfo"]["sub"].substr(8))})
                .then(function() {onAdd({keyword, geography, sessionUser})})
                .then(function() {
                    setKeyword('')
                    setGeography('')
                    console.log(isFetching)
                    setTimeout(function () {
                        setIsFetching(() => {setIsFetching(false)})
                      }, 2500)
                    
                })
        }
        getSessionUser()
    }

    if (isFetching) {
        return <Loader class="lds-ring"/>
    } else {return (
        <form className='add-form' onSubmit={onSubmit}>
            <div className='form-control'>
                <label>Keyword</label>
                <input type='text' placeholder=' Add keyword' value={keyword} onChange={(e) => setKeyword(e.target.value)}/>
            </div>
            <div className='form-control'>
                <label>Location</label>
                <input type='text' placeholder=' Add bounding box' value={geography} onChange={(e) => setGeography(e.target.value)}/>
            </div>
            <div className='btn-container'>
                <input type='submit' value='Start Streaming' className='btn'/>
            </div>
        </form>
    )
    }
    
    
}

export default AddKeyword