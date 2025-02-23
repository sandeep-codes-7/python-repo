//import ListGroup from "./components/ListGroup";
import Login from "./components/login.tsx";
//import React from "react";
import { BrowserRouter as Router,Route,Routes } from "react-router-dom";

function App(){
    return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
      </Routes>
    </Router>);

}

export default App;