import React from 'react';
import { BarChart, Bar, XAxis, Tooltip, ResponsiveContainer } from 'recharts';

function TweetTimeChart(props) {
    const data = props.data

  return (
    <div className='timeChart'> 
        <div className='timeChart-contatiner'>
            <BarChart width={720} height={200} data={data}>
                <Bar dataKey="count" fill="#465FDB" />
                <Tooltip />
                <XAxis dataKey="time" />
            </BarChart>
        </div>
    </div>
  )
}

export default TweetTimeChart