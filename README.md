# RWHOptimiser


[![Hit-Counter](http://hits.dwyl.io/aviral36/RWHOptimiser.svg)](http://hits.dwyl.io/aviral36/RWHOptimiser) 
![made-with-python](https://img.shields.io/badge/Contributors-6-blue.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



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

###### NOTE: This section deals with the output of our optimization model. This output is fed into a script which displays this information in a more appealing manner, along with various other functionalities. To see the visual output, click here.

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


## Model
In the absence of required data, we sought to generate our own data to test out our proposed algorithms. The files in the repository serve the following purposes:

[RANDOM_DATA_GENERATOR.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/RANDOM_DATA_GENERATOR.ipynb): This file generates completely random data. All the variables including the coordinates, the demands of households, the catchement areas and the rainfall in the city are random numbers without any assumptions. To generate the positions of tanks, the houses are clustered together and the centroid of each cluster is taken as a probable spot for keeping a tank.

Next, we took the jury's suggestions in mind and generated pseudo-random data. We assumed that all the pipelining(sewerage, gas, etc) is done along side roads. This is because it is easier to access these pipes if they need to be maintained or replaced. Also, we assumed that houses are built along sides roads and hence we used the coordinates from the road map as coordinates of houses to obtain about 30000 points. We further used a subset of this data of about 1100 points to test our algorithm.

[JSON HIGHWAY READER.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/JSON_HIGHWAY_READER.ipynb): Extracts coordinates from a GeoJSON mapfile and pushes them into a numpy array. Used python codec to help decode non-UTF8 JSON encoding. 

[PRIMITIVE.ipynb](https://github.com/aviral36/RWHOptimiser/blob/master/PRIMITIVE.ipynb): Implements native rainwater harvesting system, which is completely unshared, and each tank lies under a house. Takes (x,y) as input, returns average cost of installation per house and total cost of implementation on entire city.
