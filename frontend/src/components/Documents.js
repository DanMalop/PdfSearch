import React from 'react';
import '../styles/Documents.css'

function procesContent(content) {
    return {__html: content}
}

function Documents(props) {
    
    return (
        <div className='container-document'>
            <h3 className='title-document'>{props.title}</h3>
            <h5 className='author-document'>Author: {props.author}</h5>
            <p dangerouslySetInnerHTML={procesContent(props.content)}></p>
        </div>
    );
}

export default Documents;