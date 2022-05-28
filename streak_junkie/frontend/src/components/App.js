import React, { Component } from "react";
import { render } from "react-dom";

const App = (props) => <h1>Testing React Code: {props.name}</h1>;

const appDiv = document.getElementById("app");

render(<App name="Streak Junkie" />, appDiv);
