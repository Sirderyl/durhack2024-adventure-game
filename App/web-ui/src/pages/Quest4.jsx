import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import Bard from '../assets/Bard.jpg'
import { LOCALHOST } from '../settings.json'

function Quest4({ location, quest, actions }) {
 
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

        fetch(LOCALHOST + `/response?story=self_worth&quest=the_sad_bard&location=vale_of_shadows&input="` + userInput + `"`)
        .then(response => response.json())
        .then(data => {
            setActionTaken(data.action)
            setOutcome(data.outcome)
        })
        .catch(err => console.log(err))
    }

    function handleAdvance() {
        navigate("/the-broken-crown/quest5")
    }

    function handleKeyPress(e) {
        if (e.key === 'Enter') {
            handleSubmit(e)
        }
    }

  return (
    <>
        <img src={Bard} alt='Bard' height={400} width={400}/>
        <h3 style={{ whiteSpace: 'pre-line' }}>{location}</h3>
        <h4 style={{ whiteSpace: 'pre-line' }}>{quest}</h4>
        {outcome === "Invalid action" ? (
            <p style={{ whiteSpace: 'pre-line', color: 'red' }}>
                {outcome}. Try something else, will you encourage the bard, agree with his opinion, or let him drag you down?
            </p>
        ) : (
            <p style={{ whiteSpace: 'pre-line', color: 'lightgreen' }}>{outcome}</p>
        )}
        {actionTaken === "Give the bard words of encouragement" ? (
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

export default Quest4
