import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import '../App.css'
import Aeloria from '../assets/Aeloria.jpg'
import { Link } from 'react-router-dom'

function Home({ introduction, character_description }) {

  const navigate = useNavigate()

  function handleAdvance() {
    navigate("/the-broken-crown/quest1")
  }

  return (
    <>
        <img src={Aeloria} alt='Aeloria land' height={400} width={400}/>
        <h4>Introduction: {introduction}</h4>
        <h5>Your character: {character_description}</h5>
        <button value="Start Story" onClick={handleAdvance}>Start Story</button>
    </>
  )
}

export default Home
