import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

const App = (props) => (
  <div>
    <h1>Testing React Code: {props.name}</h1>
    <React.StrictMode>
      <HomePage />
    </React.StrictMode>
  </div>
);

const appDiv = document.getElementById("app");

render(<App name="Streak Junkie" />, appDiv);
