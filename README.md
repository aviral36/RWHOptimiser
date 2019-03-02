# RWHOptimiser


[![Hit-Counter](http://hits.dwyl.io/aviral36/RWHOptimiser.svg)](http://hits.dwyl.io/aviral36/RWHOptimiser) 
![made-with-python](https://img.shields.io/badge/Contributors-6-blue.svg)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



RWHOpt is a underground water tank location optimizer that finds the optimal location(s) and capacity of water tank(s) to be placed in the city, provided housing data, catchments, stability and (x,y) coordinates of houses. See more about input "HERE".

RWHOpt implements a transshipment model to produce optimal number and location of tanks. This data is fed into the web application which displays a map of shared tanks and a cost analysis graph. See more about output "HERE".

## Data Collection and Preprocessing

The transshipment model takes in numeric data as input. The input data can either be fetched from a database retrieved from the city municipal corporation data. In case such data is not available, we use Vision API by Google to map catchment area on different coordinates of the city. 
The software is flexible and can take in data in different forms. Both our methods have been discussed below.

### Fetching Data from Municipal Corporation Data

A city municipal corporation has an accurate and comprehensive data of all land use in that city. The data includes important parameters like rooftop_area, coordinates_of_building, type_of_development (industrial/residential, etc.) amongst others. Land_use data is important as it helps differentiate industrial rooftops from residential rooftops.

### Mapping Data using Vision API

The below image shows how a society in Dwarka, New Delhi is being analysed to estimate the catchment area on/near the buildings.

![Rooftop mapping using Vision API](https://github.com/aviral36/RWHOptimiser/blob/master/metadata/Webp.net-gifmaker.gif)



