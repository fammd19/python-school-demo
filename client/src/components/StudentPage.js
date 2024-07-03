import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'

export default function StudentPage() {
    const [student, setStudent] = (null)
    const {student_id} = useParams()

    useEffect( () => {
        fetch('/student/'+student_id)
        .then( response => response.json())
        .then(json => {setStudent(json)})
    }, [])
    return (
        <React.Fragment>
            {
                student
                ?
                <>
                    <h1>{student.name}</h1>
                    <h2>{student.degree}</h2>
                    <h3>Courses enrolled</h3>
                    {
                        student.enrolments.length>0
                        ?
                        <ul>
                            {student.enrolments.map (enrolment => {
                                <li>{enrolment.course.title}</li>
                            })}
                        </ul>
                        :
                        <p>No course enrolled</p>
                    }
                </>
                :
                null
            }
            
        </React.Fragment>

    )}