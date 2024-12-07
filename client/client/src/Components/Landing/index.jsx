import React from 'react'
import GraphVisualization from './GraphVisualization'
import "./style.css"

const Landing = ({data, keys}) => {
  return (
    <div className='landing-container'>
        <h1>ALL TECHNOLOGIES</h1>
        <div className='graph-container'>
            <GraphVisualization matrix={data} keys={keys}/>
        </div>
    </div>
  )
}

export default Landing
