import React, {useEffect, useState} from 'react'
import Graph from './Graph'
import "./style.css"
import { Link, useParams } from 'react-router-dom'

const Tech = ({data, keys}) => {
    const {tech} = useParams();
    const [selectedOption, setSelectedOption] = useState("Yearly");
    let Date = [{
      "jan": 2302,
      "february": 2500,
      "march": 3000,
      "april": 3100,
      "may": 4000,
      "june": 6000,
      "july": 9000,
      "august": 10000,
      "september": 10001,
      "october": 12000,
      "november": 13000,
      "december": 16000,
    }
    , {
      "jan": 1500,
      "february": 1800,
      "march": 2100,
      "april": 2500,
      "may": 3000,
      "june": 3500,
      "july": 4200,
      "august": 4900,
      "september": 5500,
      "october": 6000,
      "november": 7000,
      "december": 8000
    }
    
    , {
      "jan": 1200,
      "february": 1400,
      "march": 1800,
      "april": 2300,
      "may": 2900,
      "june": 3600,
      "july": 4300,
      "august": 5000,
      "september": 6000,
      "october": 7000,
      "november": 8500,
      "december": 9500
    }
    
    , {
      "jan": 2000,
      "february": 2500,
      "march": 3100,
      "april": 3800,
      "may": 4500,
      "june": 5300,
      "july": 6200,
      "august": 7500,
      "september": 8500,
      "october": 9500,
      "november": 11000,
      "december": 12500
    }
    
    , {
      "jan": 1000,
      "february": 1300,
      "march": 1700,
      "april": 2100,
      "may": 2700,
      "june": 3400,
      "july": 4200,
      "august": 5100,
      "september": 6100,
      "october": 7200,
      "november": 8500,
      "december": 10000
    }
    
    , {
      "jan": 500,
      "february": 800,
      "march": 1200,
      "april": 1700,
      "may": 2300,
      "june": 3000,
      "july": 3800,
      "august": 4700,
      "september": 5700,
      "october": 6800,
      "november": 8000,
      "december": 9300
    }
    ]
    let date = Date[Math.floor(Math.random() * Date.length)]
    // useEffect(() => {
    //   date = Date[Math.floor(Math.random() * Date.length)]
    // }, [])

    const [related, setRelated] = useState();
    const getRelated = () => {
      const index = keys.findIndex((item) => item == tech);
      let Related = []
      data[index].map((e, i) => {
        if(e){
          if(i !==index){
            Related.push(keys[i])
          }
        }
      })
      setRelated(Related)
    }

    useEffect(() => {
      getRelated();
    }, [])


  const handleChange = (event) => {
    const value = event.target.value;
    setSelectedOption(value);
  };
  return (
    <div className='container'>
        <div className='heading-container'>
        <div style={{left: 40, position: 'absolute', fontSize: "1.5rem"}}>
            <Link to="/" style={{backgroundColor: "#fff", border: "2px solid #333"}}>{"<"}</Link>
        </div>
            <h1>{tech.toUpperCase()}</h1>
            <div style={{right: 40, position: 'absolute'}}>

        <label htmlFor="timeframe" style={{ marginRight: "10px" }}>
        Select Timeframe:
      </label>
      <select
        id="timeframe"
        value={selectedOption}
        onChange={handleChange}
        style={{ padding: "5px", fontSize: "16px", borderRadius: "10px" }}
        >
        <option value="Yearly">Yearly</option>
        <option value="Monthly">Monthly</option>
        <option value="Weekly">Weekly</option>
      </select>
            </div>
          </div>
        {date && <Graph data={date}/>}
        <h2 style={{marginLeft: "2rem"}}>Related Technologies</h2>
        <ul>
            {
                related && related.map((e, i) => (
                    <li id={i}>
                        <Link to={`/${e}`}>
                            {e}
                        </Link>
                    </li>
                ))
            }
        </ul>
    </div>
  )
}

export default Tech
