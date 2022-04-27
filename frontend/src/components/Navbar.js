import React from 'react';
import { Link } from 'react-router-dom'; // Se remplazan todas las etiquetas <a> por <Link> y los atribotos href= de estos por el atributo to=

// los estilos se aplican importandolos desde index.js

function Navbar() {
    return(
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">PDF Search</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon" />
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link" to="/about">About</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/upload">Upload files</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    );
};

// sacado de bootstrap y traducido con https://magic.reactjs.net/htmltojsx.htm

export default Navbar;