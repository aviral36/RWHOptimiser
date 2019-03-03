import React, { Component } from "react";
import { Link } from "react-router-dom";
export default class Navbar extends Component {
  render() {
    return (
      <div className="sidenav">
        <ul style={{ marginLeft: 0, paddingLeft: 0 }} className=" mt3">
          <li className="pt4">
            <Link to="/">Home</Link>
          </li>
          <li className="pt4">
            <Link to="/grievance">Grievance</Link>
          </li>
          <li className="pt4">
            <Link to="/optimalmap">Locations</Link>
          </li>
          <li className="pt4">
            <Link to="/playground">Playground</Link>
          </li>
          <li className="pt4">
            <Link to="/advanced">Advanced</Link>
          </li>
          <li className="pt4">
            <Link to="/network">Network</Link>
          </li>
          <li className="pt4">
            <Link to="/placetank">Place Tank</Link>
          </li>
        </ul>
      </div>
    );
  }
}
