import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [title, setTitle] = useState("")
  const [introduction, setIntroduction] = useState("")
  const [character_description,setCharacter_description] = useState("")
  const [location, setLocation] = useState("")
  const [storyHasStarted, setStoryHasStarted] = useState(false)
  

  useEffect(() => {
    fetch("http://127.0.0.1:5000/story/self_worth")
    .then(response => response.json())
    .then(data => {
      setTitle(data.title)
      setIntroduction(data.introduction)
      setCharacter_description(data.character_description)
      setLocation(data.locations.ravenwood.description)
    })
    .catch(err => console.log(err))
  })

  return (
    <>
      <h1>{title}</h1>
      <h4>{!storyHasStarted && introduction}</h4>
      <h5>{!storyHasStarted && character_description}</h5>
      <p>{storyHasStarted && location}</p>
      <input
        type='button'
        value='Start Story'
        onClick={(e) => setStoryHasStarted(true)}
      />
    </>
  )
}

export default App
