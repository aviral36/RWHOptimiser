/*global google*/
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
let tankId = 0;
// locations.push({
//   lat: 28.7041,
//   lng: 77.1025
// });

const Map = compose(
  withStateHandlers(
    () => ({
      markerPosition: null
    }),
    {
      onMapClick: ({ isMarkerShown }) => e => {
        let lat = e.latLng.lat();
        let lng = e.latLng.lng();

        let geocoder = new google.maps.Geocoder();

        let address;

        geocoder.geocode(
          {
            location: {
              lat: lat,
              lng: lng
            }
          },
          (results, status) => {
            tankId++;
            address = results[0].formatted_address;
            locations.push({
              lat: lat,
              lng: lng,
              tankId: tankId,
              address: address
            });

            console.log(locations);

            let data =
              "text/json;charset=utf-8," +
              encodeURIComponent(JSON.stringify(locations));

            return {
              markerPosition: e.latLng
            };
          }
        );
        return {
          markerPosition: e.latLng
        };
      }
    }
  ),
  withScriptjs,
  withGoogleMap
)(props => (
  <GoogleMap
    defaultZoom={15}
    defaultCenter={{ lat: 28.6315, lng: 77.2167 }}
    onClick={props.onMapClick}
  >
    {/* <Marker position={props.markerPosition} />
    <Marker position={{ lat: 28.7041, lng: 77.1025 }} /> */}
    {locations.map(latlng => {
      return <Marker position={{ lat: latlng.lat, lng: latlng.lng }} />;
    })}
  </GoogleMap>
));
export default class PlaceTank extends React.Component {
  handleClick = () => {
    let csv = "Lat,Lng,Id,Address\n";
    locations.forEach(row => {
      let address = row.address;
      address.split(",").join("");
      csv += row.lat + "," + row.lng + "," + row.tankId + "," + address + "\n";
    });
    console.log(csv);
    let hiddenElement = document.createElement("a");
    hiddenElement.href = "data:text/csv;charset=utf-8," + encodeURI(csv);
    hiddenElement.target = "_blank";
    hiddenElement.download = "tank.csv";
    hiddenElement.click();
  };
  render() {
    return (
      <div style={{ height: "100%" }}>
        <Map
          googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyDurZQBXjtSzKeieXwtFeGe-jhZu-HEGQU"
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={
            <div style={{ height: `890px`, marginRight: "10px" }} />
          }
          mapElement={<div style={{ height: `100%` }} />}
        />
        <button
          type="button"
          className="btn btn-primary mt4 ml6"
          onClick={this.handleClick}
        >
          Download
        </button>
      </div>
    );
  }
}
