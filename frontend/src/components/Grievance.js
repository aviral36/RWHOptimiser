import React, { Component } from "react";
import GrievanceCard from "./GrievanceCard";

export default class Grievance extends Component {
  render() {
    return (
      <div style={{ marginLeft: "250px", marginTop: "80px" }}>
        <h1
          style={{
            textDecoration: "underline",
            fontFamily: "monospace",
            fontWeight: "bold",
            fontSize: "300%",
            marginBottom: "70px",
            fontFamily: "Montserrat, sans-serif"
          }}
        >
          Grievances
        </h1>
        <GrievanceCard />
        <GrievanceCard />
      </div>
    );
  }
}
