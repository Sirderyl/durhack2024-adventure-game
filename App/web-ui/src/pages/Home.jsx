import { useState } from 'react'
import '../App.css'
import Aeloria from '../assets/Aeloria.jpg'
import { Link } from 'react-router-dom'

function Home({ introduction, character_description }) {

  const [storyHasStarted, setStoryHasStarted] = useState(false)

  return (
    <>
      <img src={Aeloria} alt='Aeloria land' height={400} width={400}/>
      {!storyHasStarted && (
        <>
            <h4>Introduction: {introduction}</h4>
            <h5>Your character: {character_description}</h5>
            <button value="Start Story" onClick={() => setStoryHasStarted(true)}><Link to="/the-broken-crown/quest1">Start Story</Link></button>
        </>
      )}
    </>
  )
}

export default Home
