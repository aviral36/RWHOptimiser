import React, { Component } from "react";

export default class GrievanceCard extends Component {
  render() {
    return (
      <div className="row justify-content-center mt5">
        <div className="col">
          <div class="card" style={{ width: "100rem" }}>
            <div class="card-body">
              <h4
                class="card-title pt3"
                style={{ fontFamily: "Montserrat', sans-serif " }}
              >
                Main Problem Heading
              </h4>
              <p class="card-text">Problem Description</p>
              <a href="#" class="card-link">
                View More
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
