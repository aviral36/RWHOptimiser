# RWHOptimiser


[![Hit-Counter](http://hits.dwyl.io/aviral36/RWHOptimiser.svg)](http://hits.dwyl.io/aviral36/RWHOptimiser) 
![made-with-python](https://img.shields.io/badge/Contributors-6-blue.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


[View Presentation](https://docs.google.com/presentation/d/1ab0oc-WsSwmTbChWk_8pl0WLWHiz80Aj56PJ07-EgZM/edit?usp=sharing)

RWHOpt is a underground water tank location optimizer that finds the optimal location(s) and capacity of water tank(s) to be placed in the city, provided housing data, catchments, stability and (x,y) coordinates of houses. [See more about input](#inputs-structure-of-data).

RWHOpt implements a transshipment model to produce optimal number and location of tanks. This data is fed into the web application which displays a map of shared tanks and a cost analysis graph. [See more about output](#output-of-the-model).

## Data Collection and Preprocessing

The transshipment model takes in numeric data as input. The input data can either be fetched from a database retrieved from the city municipal corporation data. In case such data is not available, we use Vision API by Google to map catchment area on different coordinates of the city. 
The software is flexible and can take in data in different forms. Both our methods have been discussed below.

### Fetching Data from Municipal Corporation Data

A city municipal corporation has an accurate and comprehensive data of all land use in that city. The data includes important parameters like rooftop_area, coordinates_of_building, type_of_development (industrial/residential, etc.) amongst others. Land_use data is important as it helps differentiate industrial rooftops from residential rooftops.

### Mapping Data using Vision API

The below image shows how a society in Dwarka, New Delhi is being analysed to estimate the catchment area on/near the buildings.

![Rooftop mapping using Vision API](https://github.com/aviral36/RWHOptimiser/blob/master/metadata/Webp.net-gifmaker.gif)

The green cover in above image shows the catchment area as figured out by Vision. This has been made by implementing the watershed problem, which contains a segmentation code which segments a map, built entirely from scratch. 

## Inputs: Structure of Data

<strong>Coordinates (x,y): </strong>represent the geographical location of the centre of the catchment area, which may be a house, an apartment complex, an official building, a factory, etc, hereafter referred to as a node.

<strong> Demand (volumetric): </strong> This parameter denotes the demand of a catchment area arising from a particular node. The unit for measurement is cubic metre per month.

<strong> Stability (decimal): </strong> This measure gives the relative stability of a place (x,y) with a decimal numeral ranging from -1 to 10. Instability arises due to various factors like groundwater level, loose ground, existing pipelines, etc. Further, if a tank is impossible to be placed in a certain location, the value is set to -1. 

<strong> Cost of implementation: </strong> The overall cost of the system is actually a combination of two costs: fixed costs and variable costs. Fixed costs include one-time construction and installation costs. This includes all types of costs incurred during the set-up, like excavation, cost of concrete (per cubic meter) and others. 

## Output of the Model 

###### NOTE: This section deals with the output of our optimization model. This output is fed into a script which displays this information in a more appealing manner, along with various other functionalities. To see the visual output, [click here](#software-output-web-based-application).

<strong> Cost difference/benefit calculator</strong> calculates the difference between operational costs of implementing primitive approach and the new found distribution's approach. This cost difference (in currency) is fed into a script which displays this information in a more apealing manner. Cost calculations have been done using the assumptions:
Total cost is a combination of two costs, 
total cost = fixed costs + recurring costs
fixed(one time) costs include  
                               -tank construction cost        constant k (per cubic metre)
                                                              k * (volume of tank) gives construction cost
                               -pipeline construction cost    constant v (per metre)
                                                              v * (length of pipe) from node to tank
                               -installation cost             labor cost, permit cost, etc.
                                                              fixed value c
                                                              
                      total fixed cost = tank_construction_cost + pipeline_construction_cost + installation_cost
                      
Recurring costs include         -maintainance cost            monthly costs of tank, q per cubic meter
                                                              q * (volume of tank)
                                                              monthly costs of pipeline maintainace, w per meter
                                                              w * (length of pipeline)
                                         
                              total recurring cost = maintainance_cost (tanks + pipes)


## Files Description

In the absence of required data, we sought to generate our own data to test out our proposed algorithms. The files in the repository serve the following purposes:

[ENTIRE_CODE_PIPELINE.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/pipeline/ENTIRE_CODE_PIPELINE.ipynb) contains the entire pipeline of RWHOpt software. Different modules have been merged together in a single file. Returns the JSON file which is feeded into the webApp database for graphical plotting. JSON export consists of (x,y) coordinates, cost of making tanks, capacity of tanks and pipe framework connecting from a node(house) to a tank.

[RANDOM_DATA_GENERATOR.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/RANDOM_DATA_GENERATOR.ipynb): This file generates completely random data. All the variables including the coordinates, the demands of households, the catchement areas and the rainfall in the city are random numbers without any assumptions. To generate the positions of tanks, the houses are clustered together and the centroid of each cluster is taken as a probable spot for keeping a tank.

Next, we took the jury's suggestions in mind and generated pseudo-random data. We assumed that all the pipelining(sewerage, gas, etc) is done along side roads. This is because it is easier to access these pipes if they need to be maintained or replaced. Also, we assumed that houses are built along sides roads and hence we used the coordinates from the road map as coordinates of houses to obtain about 30000 points. We further used a subset of this data of about 1100 points to test our algorithm.

[json_parser.py](https://github.com/aviral36/RWHOptimiser/blob/master/json_parser.py) Extracts coordinates from a GeoJSON mapfile and pushes them into a numpy array. 
[JSON Location_Reader.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/JSON_Location_Reader.ipynb): Built upon json_parser code to extract location data of catchments from a GeoJSON file. Used python codec to help decode non-UTF8 JSON encoding. 

[PRIMITIVE.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/PRIMITIVE.ipynb): Implements native rainwater harvesting system, which is completely unshared, and each tank lies under a house. Takes (x,y) as input, returns average cost of installation per house and total cost of implementation on entire city.


# Software Output: Web Based Application

The front end of our software is a web-based application which takes in data from our backend feeders (like primitive, which outputs (x,y) tuples, demand, cost) and display them in a visually appealing manner. The webApp contains a home page and a grievance tab.
The Home page takes in city data and returns optimal value of number of tanks to be placed. Further, it shows a brief summary of cost benefits obtained by implementing the shared harvesting model. Further, the administrator has an option of vary the number of tanks according to his/her will, even though the cost might not be the lowest. 
This tab also contains a button which open the city map with locations of tanks and their capacities. 

The grievance tab displays all the recorded issues of citizens along with location and type of issue. This tab fetches data from a grievance app which the citizens use to address their system related problem.

## Grievance App

The grievance app is a mobile application which can be used by citizens to address their problems regarding the water harvesting system. For instance, a pipe leakage can be registered on this app along with location. The Water Department official will get to know about this problem through his portal.
      
![Grievance App](https://github.com/aviral36/RWHOptimiser/blob/master/metadata/GrievanceApp.PNG)

Since we plan to expand this app throughout a city, it will contain many perons who do not know the complexities of an app. So, we have tried to keep the interface as minimal as possible. Furthermore, the app will be developed so as to work in a offline mode - taking care of the fact that lot of people do not have access to the internet. In this method, the grievance will be sent via an SMS, which will be read accordingly by the Admin portal.

<hr>

## Data Used in this Repository

Since data is not available from municipal corporation data, we map our data according to the city roadmap structure. 
We were able to extract roadmap from StreetMaps data of Delhi, INDIA. These roads are plotted using (x,y) coordinates connecting every 450m. It can be safely assumed that every catchment area will lie alongside a road. Hence, these coordinates act as our nodes or centers of catchment area. The below image shows the highway map of Delhi. 
![Highway_Map](https://github.com/aviral36/RWHOptimiser/blob/master/metadata/highway_map.png)

The JSON file of above map containing the coordinates can be found in data folder of this repository. This data is being used by our functions to optimise location of tanks.

<hr>

### Contributors

[Ashish Gupta](https://github.com/ashishgupta1350)<br>
[Aviral Sharma](https://github.com/aviral36)<br>
[Khyati Mahendru](https://github.com/KhyatiMahendru)<br>
[Mihir Ahlawat](https://github.com/mihirahlawat)<br>
[Vikram Singh](https://github.com/SinghVikram97)<br>
[Shubham Tyagi](https://github.com/shubhamtyagihkt)<br>

<p align='center'>
©Six Nearest Neighbors,<br>
Delhi Technological University<br>
For Goldman Sachs
</p>
