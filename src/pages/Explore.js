import React from 'react';
import { useState, useEffect, useRef} from 'react';
import axios from 'axios';
import KeywordDropdown from '../components/KeywordDropdown';
import TweetList from '../components/TweetList';
import Data from '../components/Data';
import './Explore.css';


function Explore() {

    // User Session Data
    const user = useRef()

    // Dropdown/Checkbox variables
    const [dropdownSelected, setDropdownSelected] = useState([])
    const [selectedKeywords, setSelectedKeywords] = useState([])
    const toReply = useRef([])

    // Tweet exposure variables
    const [tweetcount_he, settweetcount_he] = useState()
    const [avgfollowers_he, setavgfollowers_he] = useState()
    const [tweetcount_me, settweetcount_me] = useState()
    const [avgfollowers_me, setavgfollowers_me] = useState()
    const [tweetcount_le, settweetcount_le] = useState()
    const [avgfollowers_le, setavgfollowers_le] = useState()

    // Tweet variables
    const [tweets, setTweets] = useState([])
    const [pageNumber, setPageNumber] = useState(0)
    const tweetsOnPage = useRef([])

    // Tweets & Data toggle
    const [tweetOrData, setTweetOrData] = useState(true)

    useEffect(() => {
        let user_data = ""
        let sesh = getData()
        sesh.then(function(result) {user_data = result["userinfo"]["sub"].substr(8)
                                    user.current=user_data})
            .then(function() {
                setStates() 
                updateTweetsOnDowndown()
            })

    }, [])

    useEffect(() => {
        if (dropdownSelected === "yes") {
            setStates() 
            updateTweetsOnDowndown()} 
    }, [selectedKeywords])

    useEffect(() => {
        if (toReply.current.length > 0) {
            for (var id of toReply.current) {
                var cb = document.getElementById(`${id}`)
                if (cb) {
                    cb.checked = 1
                }
            }
        }
    }, [pageNumber, tweets])

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

    const fetchTweets_he = async () => {
        const res = await axios.post('http://localhost:3000/api/tweets_he', {tsi_data: selectedKeywords});
        setTweets(res.data);
    }
    const fetchTweets_me = async () => {
        const res = await axios.post('http://localhost:3000/api/tweets_me', {tsi_data: selectedKeywords});
        setTweets(res.data);
    }
    const fetchTweets_le = async () => {
        const res = await axios.post('http://localhost:3000/api/tweets_le', {tsi_data: selectedKeywords});
        setTweets(res.data);
    }

    const handleDropdownKeyword = (e) => {
        let ddValues = []
        if (e[0].length > 0) {
            for (var x in e[0]) {
                ddValues.push(e[2][e[0][x].value])
            }
            setSelectedKeywords(ddValues)
            setDropdownSelected("yes")
        }   else {
            setSelectedKeywords([])
            setDropdownSelected("yes")
        }
    }

    const setStates = async () =>  {
        const dropdownupdate = await axios.post("http://localhost:3000/api/dropdownupdate", {data: [selectedKeywords, user.current]})
        setavgfollowers_le(dropdownupdate.data[0]['AVG(user_followers)'])
        settweetcount_le(dropdownupdate.data[0]['COUNT(user_followers)'])
        setavgfollowers_me(dropdownupdate.data[1]['AVG(user_followers)'])
        settweetcount_me(dropdownupdate.data[1]['COUNT(user_followers)'])
        setavgfollowers_he(dropdownupdate.data[2]['AVG(user_followers)'])
        settweetcount_he(dropdownupdate.data[2]['COUNT(user_followers)'])
    }

    const updateTweetsOnDowndown = async () => {
        const dropdowntweetupdate = await axios.post("http://localhost:3000/api/dropdowntweetupdate", {data: [selectedKeywords, user.current]})
        setTweets(dropdowntweetupdate.data)  
    }

    const changePage = ({selected}) => {
        setPageNumber(selected);
    };

    const triggerTweetsOrData = () => {
        setTweetOrData(!tweetOrData)
    }
    
    return <div className='explore-container'>
        <div className="gossip">
            <div className="title-container">
                <button className="title-button">Gossip</button>
            </div>
            <KeywordDropdown keywordChange={handleDropdownKeyword}/>
            <div className='tweet-container high'>
                <div className='tweet-subcontainer' onClick={fetchTweets_he}>
                    <h3>High Exposure</h3>
                    <p> Number of tweets: {parseInt(tweetcount_he).toLocaleString()}</p>
                    <p> Average followers: {parseInt(avgfollowers_he).toLocaleString()}</p>
                </div>
            </div>
            <div className='tweet-container medium' onClick={fetchTweets_me}>
                <div className='tweet-subcontainer'>
                    <h3>Medium Exposure</h3>
                    <p> Number of tweets: {parseInt(tweetcount_me).toLocaleString()}</p>
                    <p> Average followers: {parseInt(avgfollowers_me).toLocaleString()}</p>
                </div>
            </div>
            <div className='tweet-container low' onClick={fetchTweets_le}>
                <div className='tweet-subcontainer'>
                    <h3>Low Exposure</h3>
                    <p> Number of tweets: {parseInt(tweetcount_le).toLocaleString()}</p>
                    <p> Average followers: {parseInt(avgfollowers_le).toLocaleString()}</p>
                </div>
            </div>
        </div>
        <div className="visuals">
            <div className="title-container">
                <button className={tweetOrData ? "title-button td active" : "title-button td"} onClick={triggerTweetsOrData}>Tweets</button>
                |
                <button className={tweetOrData ? "title-button td" : "title-button td active"} onClick={triggerTweetsOrData}>Users</button>
            </div>
            
            {tweetOrData ?  <TweetList 
                                tweets = {tweets} 
                                toReply = {toReply}
                                tweetsOnPage = {tweetsOnPage}
                                pageNumber = {pageNumber} 
                                changePage={changePage}/> : 
                            <Data 
                                tsi_data = {selectedKeywords}
                                user = {user.current}/>}
        </div>
    </div>;
}

export default Explore;

// Add map of tweets, unique authors, # of tweets by author, author profiles, timeline, 
// For list of tweets, clients can view followers, likes/tweet, and exposure (we calulate)