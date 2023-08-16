import React from 'react'
import { useEffect, useState } from 'react';
import axios from 'axios';
import UserAnalysis from './UserAnalysis';
import TweetsByUser from './TweetsByUser';
import './Data.css'

function Data(props) {

  const [frequentTweeters, setFrequentTweeters] = useState([])
  const [popularTweeters, setPopularTweeters] = useState([])

  useEffect(() => {
    const dataLists = async () => {
        const popTweeters = await axios.post('http://localhost:3000/api/mostpopularusers', {data: [props.tsi_data, props.user]});
        const freqTweeters = await axios.post('http://localhost:3000/api/mostfrequenttweeter', {data: [props.tsi_data, props.user]});
        setPopularTweeters(popTweeters.data);
        setFrequentTweeters(freqTweeters.data)
    }
    dataLists();
    }, [props.tsi_data]);

  return (
    <div className='data-container'>
      <div className="popular-tweets">
        <h3 className="user_lists_headings">
          Most Popular Users
        </h3>
        {popularTweeters.map(user => 
          <div key={user["tweet_id"]} className="tweet popularusers">
            <div className='tweet_username_and_checkbox'>
                <img className="tweet_img" src={user["profile_image_url"]} />
                <div className="tweet_name_username">
                    <b>{user["user_name"]}</b>
                    <p>@{user["user_username"]}</p>  
                </div> 
                <TweetsByUser label="Tweets" 
                            className = "btn tweet"
                            tsi_data = {props.tsi_data}
                            tweet = {user}/> 
                <UserAnalysis label="User Analysis" 
                            className = "btn data"
                            tweet = {user}/>
                
            </div>
            <div className="user_lists_data">
                  <p>Number of tweets: {(user["user_followers"]).toLocaleString()}</p>
            </div>
          </div>)}
      </div>
      <div className="popular-users">
      <h3 className="user_lists_headings">
          Most Frequent Users
      </h3>
        {frequentTweeters.map(user => 
          <div key={user["tweet_id"]} className="tweet frequentusers">
            <div className='tweet_username_and_checkbox'>
                <img className="tweet_img" src={user["profile_image_url"]} />
                <div className="tweet_name_username">
                    <b>{user["user_name"]}</b>
                    <p>@{user["user_username"]}</p>  
                </div>
                <TweetsByUser label="Tweets" 
                            className = "btn tweet"
                            tsi_data = {props.tsi_data}
                            tweet = {user}/> 
                <UserAnalysis label="User Analysis" 
                            className = "btn data"
                            tweet = {user}/>
            </div>
            <div className="user_lists_data">
                  <p>Number of tweets: {user["COUNT(*)"]}</p>
            </div>
          </div>)}
      </div>
    </div>
  )
}

export default Data