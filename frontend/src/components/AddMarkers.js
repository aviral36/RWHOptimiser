import React from "react";
import { compose, withStateHandlers } from "recompose";
import {
  InfoWindow,
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Marker
} from "react-google-maps";

let locations = [];
locations.push({
  lat: 28.7041,
  lng: 77.1025
});

const Map = compose(
  withStateHandlers(
    () => ({
      isMarkerShown: false,
      markerPosition: null
    }),
    {
      onMapClick: ({ isMarkerShown }) => e => {
        let lat = e.latLng.lat();
        let lng = e.latLng.lng();

        console.log(lat, lng);

        locations.push({
          lat: lat,
          lng: lng
        });

        console.log(locations);

        return {
          markerPosition: e.latLng,
          isMarkerShown: true
        };
      }
    }
  ),
  withScriptjs,
  withGoogleMap
)(props => (
  <GoogleMap
    defaultZoom={8}
    defaultCenter={{ lat: 28.7041, lng: 77.1025 }}
    onClick={props.onMapClick}
  >
    {/* <Marker position={props.markerPosition} />
    <Marker position={{ lat: 28.7041, lng: 77.1025 }} /> */}
    {locations.map(latlng => {
      return <Marker position={{ lat: latlng.lat, lng: latlng.lng }} />;
    })}
  </GoogleMap>
));

export default class AddMarker extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div style={{ height: "100%" }}>
        <Map
          googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places"
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={
            <div style={{ height: `980px`, marginRight: "10px" }} />
          }
          mapElement={<div style={{ height: `100%` }} />}
        />
      </div>
    );
  }
}
