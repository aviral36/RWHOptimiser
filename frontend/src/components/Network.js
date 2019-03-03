/*global google*/
import React, { Component } from "react";
import { withGoogleMap, GoogleMap, Polyline } from "react-google-maps";

export default class OptimalMap extends Component {
  state = {
    directions: null
  };

  render() {
    const networks = [
      [{ lat: 28.7208, lng: 77.1072 }, { lat: 28.5677, lng: 77.2433 }],
      [
        {
          lat: 28.4595,
          lng: 77.0266
        },
        {
          lat: 28.5355,
          lng: 77.391
        }
      ],
      [
        {
          lat: 28.6692,
          lng: 77.4538
        },
        {
          lat: 28.8955,
          lng: 76.6066
        }
      ]
    ];

    // const pathCoordinates1 = [
    //   { lat: 28.7208, lng: 77.1072 },
    //   { lat: 28.5677, lng: 77.2433 }
    // ];

    // const pathCoordinates2 = [
    //   {
    //     lat: 28.4595,
    //     lng: 77.0266
    //   },
    //   {
    //     lat: 28.5355,
    //     lng: 77.391
    //   }
    // ];
    const GoogleMapExample = withGoogleMap(props => (
      <GoogleMap
        defaultCenter={{ lat: 28.7041, lng: 77.1025 }}
        defaultZoom={8}
        onClick={this.handleClick}
      >
        {networks.map(pathCoordinate => {
          return (
            <Polyline
              path={pathCoordinate}
              geodesic={true}
              options={{
                strokeColor: "#e21309",
                strokeOpacity: 0.75,
                strokeWeight: 5
              }}
            />
          );
        })}
        {/* <Polyline
          path={pathCoordinates1}
          geodesic={true}
          options={{
            strokeColor: "#e21309",
            strokeOpacity: 0.75,
            strokeWeight: 5
          }}
        />
        <Polyline
          path={pathCoordinates2}
          geodesic={true}
          options={{
            strokeColor: "#e21309",
            strokeOpacity: 0.75,
            strokeWeight: 5
          }}
        /> */}
      </GoogleMap>
    ));

    return (
      <div>
        <GoogleMapExample
          containerElement={
            <div
              style={{ height: `980px`, width: "100%", marginRight: "10px" }}
            />
          }
          mapElement={<div style={{ height: `100%` }} />}
        />
      </div>
    );
  }
}
