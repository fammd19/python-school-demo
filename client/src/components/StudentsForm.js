import React, {useState} from 'react'

export default function StudentsForm () {
    const [name, setName] = useState("")
    const [degree, setDegree] = useState("")
    const [notif, setNotif] = useState("")

    function handleSubmit(e) {
        e.preventDefault()

        fetch('http://127.0.0.1:4000/students',{
            method: "POST",
            "headers": {
                "Content-Type":"application/json",
            },
            body: JSON.stringify({
                name:name,
                degree:degree
            })
        })
            .then (response => response.json())
            .then (json => {
                setName("")
                setDegree("")
                setNotif("Student created")
                }
            )
        }

    return (
        <form onSubmit={handleSubmit}>
            <label form="name">Student name:</label><br/>
            <input type="text" value={name} id="name" onChange={(e) => setName(e.target.value)} /> <br/>
        
            <label form="degree">Degree:</label><br/>
            <input type="text" value={degree} id="degree" onChange={(e) => setDegree(e.target.value)} /> <br/>

            <input type="submit" value="Submit"/>        
        </form>
    )
}