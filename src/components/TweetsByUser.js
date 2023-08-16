import React, {useState} from 'react'
import {FaTwitter} from 'react-icons/fa'
import axios from 'axios';

function TweetsByUser(props) {

    const [modal, setModal] = useState(false)
    const [tweets, setTweets] = useState([])

    const toggleModal = () => {
        setModal(true)
        userTweetData()
    }

    const closeModal = () => {
        setModal(false)
    }

    if (modal) {
        document.body.classList.add('active-modal')
    } else {
        document.body.classList.remove('active-modal')
    }

    const userTweetData = async () => {
        let res = await axios.post('http://localhost:3000/api/tweetsbyuser', {"data": [props.tweet.user_ID, props.tsi_data]});
        let data = res.data;
        console.log(data)
        setTweets(data)
    }

  return (
    <>
        <button className={props.className} onClick={toggleModal}> 
            {props.label}
        </button>
        {modal && (
            <div className="modal">
                <div className="overlay"></div>
                <div className="modal-content tweetsbyuser">
                    {tweets.map(tweet =>
                        <div key={tweet.tweet_id} className='tweet'>
                            <div className='tweet_username_and_checkbox'>
                                <img className="tweet_img" src={tweet.profile_image_url} />
                                <div className="tweet_name_username">
                                    <b>{tweet.user_name}</b>
                                    <p>@{tweet.user_username}</p>  
                                </div>  
                            </div>
                            <p className="tweet_user_followers">Followers: {(tweet.user_followers).toLocaleString()}</p>
                            <p>Tweet: {tweet.tweet_text}</p>
                            <div className="container_buttons_date">
                                <a className="btn tweet" href={`https://www.twitter.com/${tweet.user_username}/status/${tweet.tweet_id}`} target="_blank" rel="noreferrer noopener">
                                    <FaTwitter /> Go to Tweet
                                </a>
                            </div>
                        
                        </div>)}
                    <div>
                        <button className="btn" onClick={closeModal} >Close</button>
                    </div>
                </div>
                
            </div>)}
        
        </>
  )
}

export default TweetsByUser