/*global google*/
import React, { Component } from "react";
import {
  withScriptjs,
  withGoogleMap,
  GoogleMap,
  Marker,
  InfoWindow
} from "react-google-maps";

let locations = [];


const MyMapComponent = withScriptjs(
  withGoogleMap(props => (
    <GoogleMap defaultZoom={8} defaultCenter={{ lat: 28.7041, lng: 77.1025 }}>
      {locations.map(latlng => {
        return (
          <Marker position={{ lat: latlng.latitude, lng: latlng.longitude }} />
        );
      })}
    </GoogleMap>
  ))
);

export default class OptimalMap extends Component {
  constructor(){
    super();
    this.state = {
        locations: []
    }
  }
  componentDidMount(){
    fetch("https://rwholt-api.herokuapp.com/possible-locations")
    .then(res => res.json())
    .then(data => {
      locations = data;
      this.setState({
        locations: locations
      });
      //console.log(locations);
      //data_recieved = true;
    });
  }
  render() {
    if(!this.state.locations)
            return null;
    let locations = this.state.locations;
    return (
      <MyMapComponent
        isMarkerShown
        googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places"
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={
          <div
            style={{
              height: "980px",
              marginLeft: 0,
              paddingLeft: 0,
              marginRight: "10px"
            }}
          />
        }
        mapElement={<div style={{ height: `100%` }} />}
      />
    );
  }
}
