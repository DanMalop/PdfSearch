import React from "react";

//subir archivos

function UploadFiles() {

    const handleFileSubmit = async (event) => {
        event.preventDefault();
        console.log(event);
        const formData = new FormData(event.currentTarget);
        //let document = formData.get("file")
        await fetch('http://localhost:5000/upload', {
            mode: "no-cors",
            method: 'POST',
            body: formData,
            headers: {"Content-Type": "text"}
        }).then(response => console.log(response))
    }

    return (
        <form method="post" onSubmit={handleFileSubmit} className="pdfapp-form card card-body" encType = "multipart/form-data">
            <input
                type="file"
                className="form-control"
                placeholder="Submit-files"
                accept=".pdf"
                autoFocus
                name="file"/>
            <button type="submit" className="btn btn-primary btn-appform">Upload</button>
        </form>
    )
}

export default UploadFiles;