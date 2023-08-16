import React, {useState} from 'react'
import {FaTwitter} from 'react-icons/fa'
import axios from 'axios';


function ReplyModal(props) {

    const [modal, setModal] = useState(false)
    const [reply, setReply] = useState('')

    const toggleModal = () => {
        setReply("")
        setModal(!modal)
    }

    if (modal) {
        document.body.classList.add('active-modal')
    } else {
        document.body.classList.remove('active-modal')
    }

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
    
    function tweetResponse() {
        let user = ""
        let sesh = getData()
        sesh.then(function(result) {user = result["userinfo"]["sub"].substr(8)})
            .then(function () {const req = axios.post('http://localhost:3000/api/post_tweet', {user_data: user, tweet_ids: props.tweet_ids, response: reply});
            const res = req
            res.then(console.log(res))
            toggleModal()
        })
    }

    return (
        <>
        <button className={props.className} onClick={toggleModal}> 
            {props.label} ({props.count})
        </button>
        {modal && (
            <div className="modal">
                <div className="overlay"></div>
                <div className="modal-content">
                    <h3>Reply to Tweets</h3>
                    <textarea className="reply-text" placeholder = "Type your response here" rows="7" cols="70" value={reply}
                    onChange={(e) => setReply(e.target.value)}></textarea>
                    <div>
                        <button className='btn tweet' onClick={tweetResponse}><FaTwitter /> Tweet Response</button>
                        <button className="btn" onClick={toggleModal} >Cancel</button>
                    </div>
                </div>
                
            </div>)}
        
        </>
    )
}

export default ReplyModal