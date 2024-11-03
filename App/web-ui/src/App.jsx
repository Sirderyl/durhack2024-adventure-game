import { Routes, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'
import Home from './pages/Home'
import Quest1 from './pages/Quest1'
import './App.css'

function App() {

  const [title, setTitle] = useState("")
  const [introduction, setIntroduction] = useState("")
  const [character_description,setCharacter_description] = useState("")
  const [location, setLocation] = useState("")
  const [quests, setQuests] = useState({})
  

  useEffect(() => {
    fetch("http://localhost:5000/story/self_worth")
    .then(response => response.json())
    .then(data => {
      setTitle(data.title)
      setIntroduction(data.introduction)
      setCharacter_description(data.character_description)
      setLocation(data.locations.ravenwood.description)
      setQuests(data.quests)
    })
    .catch(err => console.log(err))
  }, [quests])
  

  return (
    <div className='App'>
      <h1>{title}</h1>
      <Routes>
        <Route path='/the-broken-crown' element={<Home introduction={introduction} 
        character_description={character_description} />} />
        <Route path='/the-broken-crown/quest1' element={<Quest1 location={location} quest={quests.journey_begins?.description} />} />
      </Routes>
    </div>
  )
}

export default App
