import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Activities from "./Activities";

const HomePage = () => (
  <Router>
    <Routes>
      <Route exact path="/" element={<p>This is the home page</p>} />
      <Route path="/activities" element={<Activities />} />
    </Routes>
  </Router>
);

export default HomePage;
