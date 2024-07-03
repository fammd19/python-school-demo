import React, {useState, useEffect} from 'react'

export default function Students() {
    const [students, setStudents] = useState([])

    useEffect( () => {
       fetch('http://127.0.0.1:4000/students')
        .then (response => response.json())
        .then(json => {
            setStudents(json);
            console.log(json);
        })
    }, [])

    return (
        <>
            <h1>Students</h1>
            {
                students.length>0
                ?
                (<ul>
                    {
                        students.map( student => 
                            <li key={student.id}>{student.name}</li>
                        )
                    }
                </ul>)
                :
                <p>Uh oh</p>
            }
        </>
    )
}