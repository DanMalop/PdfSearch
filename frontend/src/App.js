//import logo from './logo.svg';
import './App.css';
import Pdfsearch from './components/Pdfsearch';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Enrutador (navegación)

import About from './components/About';
import Navbar from './components/Navbar'
import UploadFiles from './components/UploadFiles'

// npm i react-router-dom

function App() {  

  return(
    <Router>
      <Navbar/>
      <div className="container p-4">
        <Routes>
          <Route path="/about" element={<About/>}/>
          <Route path="/upload" element={<UploadFiles/>}/>
          <Route path="/" element={<Pdfsearch/>}/>
        </Routes>
      </div>
    </Router>
  );
}

// En versiones anteriores se usaba Switch, ahora se usa Routes -> https://reactrouter.com/docs/en/v6/upgrading/v5#upgrade-all-switch-elements-to-routes

export default App;
