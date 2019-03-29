import React, { Component } from "react";

export default class Home extends Component {
  componentDidMount() {
    window.executeHome();
  }
  render() {
    return (
      <div
        style={{ marginLeft: "250px", marginTop: "60px", overflowX: "hidden" }}
      >
        <canvas id="myChart" width="400" height="200" />
      </div>
    );
  }
}
