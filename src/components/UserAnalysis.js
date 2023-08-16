import React from 'react'
import { useState } from 'react'
import axios from 'axios'
import { TagCloud } from 'react-tagcloud'
import TweetTimeChart from './TweetTimeChart'

function UserAnalysis(props) {
    const [modal, setModal] = useState(false)
    const [wordCloud, setWordCloud] = useState([])
    const [tweetTimes, setTweetTimes] = useState([])

    const toggleModal = () => {
        setModal(true)
        wordCloudData()
    }

    const closeModal = () => {
        setModal(false)
    }

    if (modal) {
        document.body.classList.add('active-modal')
    } else {
        document.body.classList.remove('active-modal')
    }


    const wordCloudData = async () => {
        let res = await axios.post('http://localhost:3000/api/user100tweets', {"user_id": props.tweet.user_ID});
        let data = res.data;
        setWordCloud(data[0])
        setTweetTimes(data[1])
    }

    const options = {
        luminosity: 'dark',
        hue: '#00033C',
    }

    let created_at = new Date(props.tweet.user_created_at)
    let created_at_formatted = (created_at.toDateString()).slice(3)
    var followers_ratio = (props.tweet.user_followers/props.tweet.user_following).toFixed(2)
    return (
        <>
        <button className={props.className} onClick={toggleModal}> 
            {props.label}
        </button>
        {modal && (
            <div className="modal">
                <div className="overlay"></div>
                <div className="modal-content useranalysis">
                    <div className='useranalysis_image_name'>
                        <img className="user_img" src={props.tweet.profile_image_url} />
                        <div className="user_username">
                            <b>@{props.tweet.user_username}</b> 
                        </div>
                    </div>
                    <div  id={`${props.tweet.tweet_id}`}>
                        <div className="user_analysis">
                            <div className="description">
                                <h3>Information</h3>
                                <p>The most important piece here is the join date. The longer they have been on Twitter the better. Spam accounts and robots tend to get suspended after a couple of weeks.</p>
                            </div>
                            <div className="user_data">
                                <table>
                                    <tbody>
                                        <tr>
                                            <th style={{width:'35%'}}>Name</th>
                                            <th style={{width:'65%'}}>{props.tweet.user_username}</th>
                                        </tr>
                                        <tr>
                                            <td>Joined Twitter on</td>
                                            <td>{created_at_formatted}</td>
                                        </tr>
                                        <tr>
                                            <td>Location</td>
                                            <td>{props.tweet.user_location}</td>
                                        </tr>
                                        <tr>
                                            <td>Account Description</td>
                                            <td>{props.tweet.user_description}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div className='user_analysis'>
                            <div className="description">
                                <h3>Statistics</h3>
                                <p>More followers is good. A high followers ratio means that more people are following out of good will, not follow-back.</p>
                            </div>
                            <div className='user_data'>
                                <table>
                                    <tbody>
                                        <tr>
                                            <th style={{width:'35%'}}>Followers</th>
                                            <th style={{width:'65%'}}>{(props.tweet.user_followers).toLocaleString()}</th>
                                        </tr>
                                        <tr>
                                            <td>Following</td>
                                            <td>{(props.tweet.user_following).toLocaleString()}</td>
                                        </tr>
                                        <tr>
                                            <td>Tweets</td>
                                            <td>{(props.tweet.user_tweet_count).toLocaleString()}</td>
                                        </tr>
                                        <tr>
                                            <td>Followers Ratio</td>
                                            <td>{(followers_ratio).toLocaleString()}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                        <div>
                            <div className='user_analysis plots'>
                                <h3>Most Common Topics</h3>
                                <div>
                                    <TagCloud minSize={15} maxSize={25} tags={wordCloud} className="simple-cloud" colorOptions={options} />
                                </div>
                            </div>
                        </div>
                        <div>
                            <div className='user_analysis plots'>
                                <h3>Activity Time</h3>
                                <div>
                                    <TweetTimeChart data = {tweetTimes}/>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div>
                        <button className="btn" onClick={closeModal} >Close</button>
                    </div>
                </div>
                
            </div>)}
        
        </>
    )
}

export default UserAnalysis