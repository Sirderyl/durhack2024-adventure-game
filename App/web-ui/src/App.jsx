import { Routes, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'
import Home from './pages/Home'
import Quest1 from './pages/Quest1'
import Quest2 from './pages/Quest2'
import Quest3 from './pages/Quest3'
import './App.css'

function App() {
  const [story, setStory] = useState('self_worth')

  const [title, setTitle] = useState("")
  const [introduction, setIntroduction] = useState("")
  const [character_description,setCharacter_description] = useState("")
  const [locations, setLocations] = useState("")
  const [quests, setQuests] = useState({})


  useEffect(() => {
    fetch(`http://localhost:5000/story/${story}`)
    .then(response => response.json())
    .then(data => {
      setTitle(data.title)
      setIntroduction(data.introduction)
      setCharacter_description(data.character_description)
      setLocations(data.locations)
      setQuests(data.quests)
    })
    .catch(err => console.log(err))
  }, [story])


  return (
    <div className='App'>
      <h1>{title}</h1>
      <Routes>
        <Route path='/the-broken-crown' element={<Home introduction={introduction}
        character_description={character_description} />} />
        <Route path='/the-broken-crown/quest1'
          element={<Quest1 location={locations.ravenwood?.description}
          quest={quests.journey_begins?.description} />}
        />
        <Route path='/the-broken-crown/quest2'
          element={<Quest2 location={locations.vale_of_shadows?.description} 
          quest={quests.meeting_the_fox?.description} />}
        />
        <Route path='/the-broken-crown/quest3'
          element={<Quest3 location={locations.vale_of_shadows?.description} 
          quest={quests.facing_the_mirror?.description} />}
        />
      </Routes>
    </div>
  )
}

export default App
