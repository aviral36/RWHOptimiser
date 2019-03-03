import React, { Component } from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import Grievance from "./components/Grievance";
import OptimalMap from "./components/OptimalMap";
import "./App.css";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Playground from "./components/Playground";
import { withScriptjs } from "react-google-maps";
import Advanced from "./components/Advanced";
import Network from "./components/Network";
import PlaceTank from "./components/PlaceTank";
class App extends Component {
  render() {
    const MapLoader = withScriptjs(Playground);
    const MapLoader2 = withScriptjs(Advanced);
    const MapLoader3 = withScriptjs(Network);
    return (
      <BrowserRouter>
        <div className="App">
          <Navbar />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/grievance" component={Grievance} />
            <Route exact path="/optimalmap" component={OptimalMap} />
            <Route
              exact
              path="/playground"
              component={() => (
                <MapLoader
                  googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyDurZQBXjtSzKeieXwtFeGe-jhZu-HEGQU"
                  loadingElement={<div style={{ height: `100%` }} />}
                />
              )}
            />
            <Route
              exact
              path="/advanced"
              component={() => (
                <MapLoader2
                  googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyDurZQBXjtSzKeieXwtFeGe-jhZu-HEGQU"
                  loadingElement={<div style={{ height: `100%` }} />}
                />
              )}
            />
            <Route
              exact
              path="/network"
              component={() => (
                <MapLoader3
                  googleMapURL="https://maps.googleapis.com/maps/api/js?key=AIzaSyDurZQBXjtSzKeieXwtFeGe-jhZu-HEGQU"
                  loadingElement={<div style={{ height: `100%` }} />}
                />
              )}
            />
            <Route exact path="/placetank" component={PlaceTank} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
