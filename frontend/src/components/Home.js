import React, { Component } from "react";

export default class Home extends Component {
  componentDidMount() {
    window.executeHome();
  }
  render() {
    return (
      <div
        style={{ marginLeft: "220px", marginTop: "60px", overflowX: "hidden" }}
      >
        <canvas id="myChart" width="400" height="200" />
        <div className="row">
          <div className="col">
            <h1>Total Tanks:10</h1>
          </div>
        </div>
      </div>
    );
  }
}
