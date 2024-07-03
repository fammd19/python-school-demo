import React from 'react';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import './App.css';
import Students from './components/Students';
import StudentsForm from './components/StudentsForm';
import StudentPage from './components/StudentPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route index path="/" element={<h1>HOME PAGE</h1>}/>
        <Route path="/students" element={<Students/>}/>
        <Route path="/students/new" element={<StudentsForm/>}/>
        <Route path="/students/:student_id" element={<StudentPage/>}/>
      </Routes>
    </Router>
  )
}

export default App;
