import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import Forge from '../assets/Forge.jpg'
import { LOCALHOST } from '../settings.json'

function Quest1({ location, quest, actions }) {
 
    const [userInput, setUserInput] = useState("")
    const [actionTaken, setActionTaken] = useState("")
    const [outcome, setOutcome] = useState("")
    const navigate = useNavigate()

    async function handleSubmit(e) {
        e.preventDefault()

        if(userInput === "list actions") {
            let actionList = ""
            Object.keys(actions).forEach(action => {
                actionList += action + "\n"
            })
            setOutcome(actionList)
            return
        }

        fetch(LOCALHOST + `/response?story=self_worth&quest=journey_begins&location=ravenwood&input="` + userInput + `"`)
        .then(response => response.json())
        .then(data => {
            setActionTaken(data.action)
            setOutcome(data.outcome)
        })
        .catch(err => console.log(err))
    }

    function handleAdvance() {
        navigate("/the-broken-crown/quest2")
    }

    function handleKeyPress(e) {
        if (e.key === 'Enter') {
            handleSubmit(e)
        }
    }

  return (
    <>
        <img src={Forge} alt='Forge' height={400} width={400}/>
        <h3 style={{ whiteSpace: 'pre-line' }}>{location}</h3>
        <h4 style={{ whiteSpace: 'pre-line' }}>{quest}</h4>
        {outcome === "Invalid action" ? (
            <p style={{ whiteSpace: 'pre-line', color: 'red' }}>
                {outcome}. Try something else, perhaps there is someone waiting to speak with you.
            </p>
        ) : (
            <p style={{ whiteSpace: 'pre-line', color: 'lightgreen' }}>{outcome}</p>
        )}
        {actionTaken === "Talk to blacksmith" ? (
            <button onClick={() => handleAdvance()}>Advance</button>
        ) : (
            <>
                <input type="text"
                    placeholder="Enter your answer here"
                    onChange={(e) => setUserInput(e.target.value)}
                    onKeyDown={(e) => handleKeyPress(e)}
                    />
                <button style={{ marginLeft: '10px' }} onClick={(e) => handleSubmit(e)}>Submit</button>
            </>
        )}
    </>
  )
}

export default Quest1