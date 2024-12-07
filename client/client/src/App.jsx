import React, { useEffect, useState } from 'react'
import Landing from './Components/Landing'
import Tech from './Components/Tech'
import { Route, Routes } from 'react-router-dom';
import './app.css'
import axios from 'axios'

const App = () => {
  const [data, setData] = useState();
  const fetch = async () => {
    try {
      const data = await axios.get('http://10.96.4.69:5000/api/');
      console.log(data)
      setData(data.data);
    } catch (error) {
      console.log(error)
    }
  }
  useEffect(() => {
    fetch()
  }, [])
  return (
    <div>
      {!data?(<div style={{width: "100vw", height: "100vh", textAlign: 'center'}}><h1>"Loading..."</h1></div>):
      <Routes>
        <Route path="/" element={<Landing data={data.matrix} keys={data.keys}/>} />
        <Route path="/:tech" element={<Tech data={data.matrix} keys={data.keys} Date={data.date}/>} />
      </Routes>}
      {/* <Landing /> */}
        {/* <Tech related={["ts", "sql", "react", "express"]} lang="JS"/> */}
    </div>
  )
}

export default App
