import React, {useState} from 'react';
import Documents from './Documents';
import '../styles/Pdfsearch.css'

const API = process.env.REACT_APP_BACKEND;

// En JSX no se puede usar statements como if, for o switch porque JSX se trata solo de azucar sintactico para la funcion call 

function Pdfsearch() {

    //STATES
    const [formData, setFormData] = useState({
        keyword: '',
        scope: '',
    })
    const [inform, setInform] = useState("");

    //HANDLERS
    const handleInputChange = (event) => {
        setFormData({
            ...formData, // Copia los datos del estado
            [event.target.name]: event.target.value
            })            
    }

    const handleSubmit = async (event) => {
        event.preventDefault();
        console.log(formData.keyword, formData.scope, formData.ignoreSpaces);
        const res = await fetch(`${API}/generate_inform`, {
            method: "POST",
            body: JSON.stringify(formData),
            headers: { "Content-Type": "application/json" }})
        const data = await res.json();
        console.log(data);
        setInform(data)
    };

    return(
        <div className='content-pdfsearch'>
            <h1 className="pdfapp-title">PDF search tool</h1>

                <form method="post" onSubmit={handleSubmit} className="pdfapp-form card card-body">
                    <div className="formulary-app">
                        <input
                            type="text"
                            onChange={handleInputChange}
                            className="form-control"
                            placeholder="Keyword"
                            autoFocus
                            name="keyword"/>
                        <input
                            type="number"
                            onChange={handleInputChange}
                            className="form-control"
                            placeholder="Scope"
                            autoFocus
                            name="scope"/>
                        <button className="btn btn-primary btn-appform">Search</button>
                    </div>
                </form>

            <div className="document-list">
                {inform? 
                /*<Documents title= {inform[0].title }/>: null /*OPERADOR TERNARIO (COMO UNA ESPECIE DE IF) */
                inform.map(item => {
                    return(item.content? <Documents title={item.title} content={item.content} author={item.author}/>: null)
                }): null
            } 
            </div>
        </div>
        

    );
};

export default Pdfsearch;