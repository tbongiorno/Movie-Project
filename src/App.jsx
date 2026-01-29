import { useState } from 'react'
import './App.css'
import Form from './form'

const formList = [
  {
    "key": 1,
    "title": "Login Here!",
    "question1": "Enter Username",
    "question2": "Enter Password",
  },
  {
    "key": 2,
    "title": "Sign Up Here!",
    "question1": "Enter Username",
    "question2": "Enter Password",
  },
  {
    "key": 3,
    "title": "Movie Searcher!",
    "question1": "Enter Movie Title",
    "question2": "",
  },
  {
    "key": 4,
    "title": "Location Searcher!",
    "question1": "Enter Location",
    "question2": "",
  },

]

function App() {
  const form = (
    <div>
      {formList.map((form) => (
        <Form
          title={form.title}
          q1={form.question1}
          q2={form.question2}
        />
      ))}
    </div>
    
  )
  return (
    <>
      <div>
        <h1>Hello</h1>
        { form }
      </div>
     
    </>
  )
}

export default App
