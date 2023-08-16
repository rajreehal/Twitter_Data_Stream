import React from 'react'
import { useState } from 'react';
import ClearButton from './ClearButton'
import ReplyModal from './ReplyModal'
import ReactPaginate from 'react-paginate';
import UserAnalysis from './UserAnalysis';
import {FaTwitter} from 'react-icons/fa'

function TweetList(props) {
    
    const tweetsPerPage = 10
    const pagesVisited = props.pageNumber * tweetsPerPage
    const [clearSelectedTweets, setclearSelectedTweets] = useState(false)
    const [count, setCounter] = useState(0)

    const select_tweet_for_response = (tweet) => {
        const checkbox = document.getElementById(`${tweet.tweet_id}`)
        const replyTweets = props.toReply.current
        setCounter(count => count + 1)
        if (checkbox.checked) {
            if (replyTweets.includes(tweet.tweet_id)) {
                props.toReply.current = replyTweets
            } else {
                replyTweets.push(tweet.tweet_id)
                props.toReply.current = replyTweets
            }
        } else {
            props.toReply.current = replyTweets.filter(t => t !== tweet.tweet_id)
        }    
        console.log(props.toReply.current)
    }

    const clearReplySelections = () => {
        if (props.toReply.current.length > 0) {
            for (var id of props.toReply.current) {
                var cb = document.getElementById(`${id}`)
                if (cb) {
                    cb.checked = 0
                }
            }
        }
        props.toReply.current = []
        console.log(props.toReply.current)
        setclearSelectedTweets(!clearSelectedTweets)
    }

    const displayTweets = props.tweets
        .slice(pagesVisited, pagesVisited + tweetsPerPage)
        .map(tweet => {
            let created_at = new Date(tweet.created_at)
            let created_at_formatted = (created_at.toDateString()).slice(3)
            return (
                <div key={tweet.tweet_id} className='tweet'>
                    <div className='tweet_username_and_checkbox'>
                        <img className="tweet_img" src={tweet.profile_image_url} />
                        <div className="tweet_name_username">
                            <b>{tweet.user_name}</b>
                            <p>@{tweet.user_username}</p>  
                        </div>  
                        <input className='tweet_checkbox' type="checkbox"
                        onChange={() => select_tweet_for_response(tweet)} id={`${tweet.tweet_id}`}>
                        </input>
                    </div>
                    <p className="tweet_user_followers">Followers: {(tweet.user_followers).toLocaleString()}</p>
                    <p>Tweet: {tweet.tweet_text}</p>
                    <div className="container_buttons_date">
                        <a className="btn tweet" href={`https://www.twitter.com/${tweet.user_username}/status/${tweet.tweet_id}`} target="_blank" rel="noreferrer noopener">
                            <FaTwitter /> Go to Tweet
                        </a>
                        <UserAnalysis label="User Analysis" 
                            className = "btn"
                            tweet = {tweet}/>
                        <p className="tweet_date">{created_at_formatted}</p>
                    </div>
                    
                </div>
            );
        })
    
    const pageCount = Math.ceil(props.tweets.length / tweetsPerPage);
    

  return (
    <>
        <div className="align-reply-btns">
                    <ClearButton 
                        label="Clear Selections" 
                        className = {props.toReply.current.length > 0 ? "btn reply clearselections" : "btn reply clearselections inactive"}
                        onClick={clearReplySelections}/>
                    <ReplyModal label="Reply to Tweets" 
                        className = {props.toReply.current.length > 5 ? "btn reply inactive overlimit" : (props.toReply.current.length > 0 ? "btn reply" : "btn reply inactive")} 
                        count = {props.toReply.current.length}
                        tweet_ids = {props.toReply}/>
        </div>
                {displayTweets}
                <ReactPaginate
                    previousLabel={"<"}
                    nextLabel={">"}
                    pageCount={pageCount}
                    onPageChange={props.changePage}
                    containerClassName={'paginationButtons'}
                    previousLinkClassName={'previousButton'}
                    nextLinkClassName={'nextButton'}
                    disabledClassName={'paginationDisable'}
                    activeClassName={'paginationActive'}
                />
    </>
  )
}

export default TweetList