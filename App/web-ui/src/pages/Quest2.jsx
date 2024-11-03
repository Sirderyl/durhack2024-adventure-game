import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import Vale from '../assets/Vale.jpg'

function Quest2({ location, quest }) {
 
    const [userInput, setUserInput] = useState("")
    const [actionTaken, setActionTaken] = useState("")
    const [outcome, setOutcome] = useState("")
    const navigate = useNavigate()

    async function handleSubmit(e) {
        e.preventDefault()

        fetch(`http://localhost:5000/response?story=self_worth&quest=meeting_the_fox&location=vale_of_shadows&input="` + userInput + `"`)
        .then(response => response.json())
        .then(data => {
            setActionTaken(data.action)
            setOutcome(data.outcome)
        })
        .catch(err => console.log(err))
    }

    function handleAdvance() {
        navigate("/the-broken-crown/quest3")
    }

    function handleKeyPress(e) {
        if (e.key === 'Enter') {
            handleSubmit(e)
        }
    }

  return (
    <>
        <img src={Vale} alt='Vale' height={400} width={400}/>
        <h3 style={{ whiteSpace: 'pre-line' }}>{location}</h3>
        <h4 style={{ whiteSpace: 'pre-line' }}>{quest}</h4>
        {outcome === "Invalid action" ? (
            <p style={{ whiteSpace: 'pre-line', color: 'red' }}>
                {outcome}. Try something else, what could you use to distract the fox? Try looking around the area.
            </p>
        ) : (
            <p style={{ whiteSpace: 'pre-line', color: 'lightgreen' }}>{outcome}</p>
        )}
        {actionTaken === "Throw a piece of raw meat" ? (
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

export default Quest2
