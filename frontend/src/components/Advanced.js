/*global google*/
import React, { Component } from "react";
import "./Advanced.css";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  DirectionsRenderer
} from "react-google-maps";
let waypoints;
export default class OptimalMap extends Component {
  state = {
    directions: null,
    startLat: 28.7041,
    startLng: 77.1025,
    endLat: 30.7333,
    endLng: 76.7794
  };
  updateMap = waypoints => {
    let latStart = Number(this.state.startLat);
    let lngStart = Number(this.state.startLng);

    let latEnd = Number(this.state.endLat);
    let lngEnd = Number(this.state.endLng);

    const directionsService = new google.maps.DirectionsService();

    const origin = { lat: latStart, lng: lngStart };
    const destination = { lat: latEnd, lng: lngEnd };
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

    const origin = { lat: this.state.startLat, lng: this.state.startLng };
    const destination = { lat: this.state.endLat, lng: this.state.endLng };
    waypoints = [
      // {
      //   location: new google.maps.LatLng(30.3782, 76.7767)
      // },
      // {
      //   location: new google.maps.LatLng(29.0588, 76.0856)
      // }
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

  handleStart = e => {
    let input = e.target.value;
    let geocoder;
    function initialize() {
      geocoder = new google.maps.Geocoder();
    }
    initialize();
    geocoder.geocode(
      {
        address: input
      },
      (results, status) => {
        let lat = results[0].geometry.location.lat();
        let lng = results[0].geometry.location.lng();
        this.setState({ startLat: lat });
        this.setState({ startLng: lng });
      }
    );
    // let res = input.split(" ");
    // if (res.length >= 2) {
    //   let lat = res[0];
    //   let lng = res[1];
    //   this.setState({ startLat: lat });
    //   this.setState({ startLng: lng });
    // }
    console.log(input);
  };

  handleEnd = e => {
    let input = e.target.value;
    let geocoder;
    function initialize() {
      geocoder = new google.maps.Geocoder();
    }
    initialize();
    geocoder.geocode(
      {
        address: input
      },
      (results, status) => {
        let lat = results[0].geometry.location.lat();
        let lng = results[0].geometry.location.lng();
        this.setState({ endLat: lat });
        this.setState({ endLng: lng });
      }
    );
    // let res = input.split(" ");
    // if (res.length >= 2) {
    //   let lat = res[0];
    //   let lng = res[1];
    //   this.setState({ endLat: lat });
    //   this.setState({ endLng: lng });
    // }
    console.log(input);
  };

  handleBtnClick = () => {
    console.log(this.state.startLat, this.state.startLng);
    console.log(this.state.endLat, this.state.endLng);
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
        <div
          className="row mt4 mb4"
          style={{ textAlign: "center", paddingLeft: "5%" }}
        >
          <div className="col-3 pl4 offset-2" style={{ textAlign: "center" }}>
            <h3 style={{ display: "inline-block", fontFamily: "monospace" }}>
              Start:
            </h3>
            <input type="text" onChange={this.handleStart} />
          </div>
          <div className="col-3" style={{ textAlign: "center" }}>
            <h3 style={{ display: "inline-block", fontFamily: "monospace" }}>
              End:
            </h3>
            <input type="text" onChange={this.handleEnd} />
          </div>
          <div className="col-3">
            <button
              type="button"
              class="btn btn-primary"
              onClick={this.handleBtnClick}
            >
              Submit
            </button>
          </div>
        </div>
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
