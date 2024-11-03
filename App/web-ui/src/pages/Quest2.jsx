import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import Forge from '../assets/Forge.jpg'

function Home({ location, quest }) {
 
    const [userInput, setUserInput] = useState("")
    const [actionTaken, setActionTaken] = useState("")
    const [outcome, setOutcome] = useState("")
    const navigate = useNavigate()

    async function handleSubmit(e) {
        e.preventDefault()

        fetch("http://localhost:5000/response?story=self_worth&quest=journey_begins&location=ravenwood&input=" + userInput)
        .then(response => response.json())
        .then(data => {
            setActionTaken(data.action)
            setOutcome(data.outcome)
            if (data.action === "Talk to blacksmith") {
                navigate("/the-broken-crown/quest2")
            }
        })
        .catch(err => console.log(err))
    }

  return (
    <>
        <img src={Forge} alt='Forge' height={400} width={400}/>
        <h3>{location}</h3>
        <h4>{quest}</h4>
        {actionTaken !== "Talk to blacksmith" && <p>{outcome}</p>}
        <input type="text" placeholder="Enter your answer here" onChange={(e) => setUserInput(e.target.value)} />
        <button style={{ marginLeft: '10px' }} onClick={(e) => handleSubmit(e)}>Submit</button>
    </>
  )
}

export default Home
