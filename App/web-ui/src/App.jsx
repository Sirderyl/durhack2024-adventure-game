import { Routes, Route } from 'react-router-dom'
import { useEffect, useState } from 'react'
import Home from './pages/Home'
import Quest1 from './pages/Quest1'
import Quest2 from './pages/Quest2'
import Quest3 from './pages/Quest3'
import Quest4 from './pages/Quest4'
import Quest5_final from './pages/Quest5_final'
import Ending from './pages/Ending'
import './App.css'
import { LOCALHOST } from './settings.json'

function App() {
  const [story, setStory] = useState('self_worth')

  const [title, setTitle] = useState("")
  const [introduction, setIntroduction] = useState("")
  const [character_description,setCharacter_description] = useState("")
  const [locations, setLocations] = useState("")
  const [quests, setQuests] = useState({})


  useEffect(() => {
    fetch(LOCALHOST + `/story/${story}`)
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
          quest={quests.journey_begins?.description}
          actions={quests.journey_begins?.actions} />}
        />
        <Route path='/the-broken-crown/quest2'
          element={<Quest2 location={locations.vale_of_shadows?.description} 
          quest={quests.meeting_the_fox?.description}
          actions={quests.meeting_the_fox?.actions} />}
        />
        <Route path='/the-broken-crown/quest3'
          element={<Quest3 location={locations.vale_of_shadows?.description} 
          quest={quests.facing_the_mirror?.description}
          actions={quests.facing_the_mirror?.actions} />}
        />
        <Route path='/the-broken-crown/quest4'
          element={<Quest4 location={locations.vale_of_shadows?.description} 
          quest={quests.the_sad_bard?.description}
          actions={quests.the_sad_bard?.actions} />}
        />
        <Route path='/the-broken-crown/quest5'
          element={<Quest5_final location={locations.vale_of_shadows?.description} 
          quest={quests.finding_the_crown?.description}
          actions={quests.finding_the_crown?.actions} />}
        />
        <Route path='/the-broken-crown/ending' element={<Ending />} />
      </Routes>
    </div>
  )
}

export default App
