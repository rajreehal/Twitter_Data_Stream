import { useEffect, useState } from 'react'
import Loader from './Loader'
import axios from 'axios';
import './../pages/tracker.css'

const Keyword = ({ keyword, onDelete }) => {
    const [isFetching, setIsFetching] = useState(false);
    const [keywordData, setKeywordData] = useState()

    useEffect(() => {
        fetch_KeywordData()
    }, [])

    function spinnerOnDelete() {
        setIsFetching(() => {setIsFetching(true)})
        onDelete(keyword.id)
    }

    const fetch_KeywordData = async () => {
        const res = await axios.post('http://localhost:3000/api/keywordData', {tsi_data: keyword});
        setKeywordData(res.data);
    }

    let stream_datetime = new Date(keyword.date)
    let currentDateTime = new Date()
    let date = (stream_datetime.toDateString()).slice(3)
    let time = (stream_datetime.toLocaleTimeString())
    let timeDiff = currentDateTime - stream_datetime

    if (isFetching) {
        return (<Loader class="keyword"/>)
    } else { return (
        <div className='streamed-keyword'>
            <div className='streamed-info'>
                <h3>{keyword.keyword}</h3>
                <div className="streamed-">
                    <p>Tweets: {keywordData}</p>
                    <p>Stream initiated: {date} {time}</p>
                    <p>Stream duration: {timeDiff}</p>
                </div>
            </div>
            <div className='streamed-endstream'>
                <button className="btn-endstream" onClick={() => spinnerOnDelete()}>
                    End stream
                </button>
            </div>
            <p>{keyword.geography}</p>
        </div>
        )
        
    }
    
}

export default Keyword