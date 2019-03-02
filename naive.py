###
This program calculates the Naive cost of installing rainwater harvesting tanks in a city.

Data collected: 
rainfall data (CSV)
housing data (CSV)

return value:
overall cost of project in the city. (currency)
###

#==========================================

import numpy as np                       #for array manipulations and pandas support
import pandas as pd                      #for interacting with dataframe 
import math                              #mathematical functionality

rain = pd.read_csv(file_name)
catchment_csv = pd.read_csv(file_name)

#==========================================

#different costs of construction

#One time Costs
#construction cost of underground tank 
tank_c = 1000       #per m3
pipe_c = 50         #per m

#fixed cost of constuction of tank
fixed_cost = 30     #per m3


#Annual Costs
#maintainance_cost
tank_m = 10         #per m3
pipe_m = 10         #per m

#===========================================

def naive_calculator(df_rain, df_catchment):
    
    
    #one time costs
    ot_cost
    
    #annual costs
    ann_cost
    
    
    return ot_cost, ann_cost
