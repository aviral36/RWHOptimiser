/*global google*/
import React, { Component } from "react";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  DirectionsRenderer
} from "react-google-maps";
let waypoints;
export default class OptimalMap extends Component {
  state = {
    directions: null
  };
  updateMap = waypoints => {
    const directionsService = new google.maps.DirectionsService();
    const origin = { lat: 28.7041, lng: 77.1025 };
    const destination = { lat: 30.7333, lng: 76.7794 };
    directionsService.route(
      {
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.WALKING,
        waypoints: waypoints
      },
      (result, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
          this.setState({
            directions: result
          });
        } else {
          console.error(`error fetching directions ${result}`);
        }
      }
    );
  };
  componentDidMount() {
    const directionsService = new google.maps.DirectionsService();

    const origin = { lat: 28.7041, lng: 77.1025 };
    const destination = { lat: 30.7333, lng: 76.7794 };
    waypoints = [
      {
        location: new google.maps.LatLng(30.3782, 76.7767)
      },
      {
        location: new google.maps.LatLng(29.0588, 76.0856)
      }
    ];
    directionsService.route(
      {
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.WALKING,
        waypoints: waypoints
      },
      (result, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
          this.setState({
            directions: result
          });
        } else {
          console.error(`error fetching directions ${result}`);
        }
      }
    );
  }

  handleClick = e => {
    let lat = e.latLng.lat();
    let lng = e.latLng.lng();
    waypoints.push({
      location: new google.maps.LatLng(lat, lng)
    });
    this.updateMap(waypoints);
  };

  render() {
    const GoogleMapExample = withGoogleMap(props => (
      <GoogleMap
        defaultCenter={{ lat: 28.7041, lng: 77.1025 }}
        defaultZoom={8}
        onClick={this.handleClick}
      >
        <DirectionsRenderer directions={this.state.directions} />
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
