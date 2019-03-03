#!/usr/bin/env python
# coding: utf-8

# ## Step 1: Fetch the real world data
# 
# - DATA FROM JSON TO CSV
# 

# In[20]:



import json
import requests
import codecs
import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
import random

from sklearn.datasets import make_blobs

# fetching data from file, parsing the json
data = None
file = '../data/location1.json'
with open(file, "r") as read_file:
    data = json.load(codecs.open(file, 'r', 'utf-8-sig'))

coord = []

# preprocessing the data
for line in data:
    coord.append(line['geometry']['coordinates']) 
    
new = []
for line in coord:
    for points in line:
        new.append(points)
        
# Isolating the dependencies
new_coord = np.unique(np.array(coord),axis=0)
new_coord.shape
dat = pd.DataFrame(new_coord, columns=['x','y'])
dat.to_csv("real_housing_data_x_y.csv")


# #### Defining our constants and variables

# In[21]:


# seed for consistent results
RANDOM_SEED = 32
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)
NUM_HOUSES = len(dat)

MEAN_DEMAND_WATER_PER_HOUSE = 100 # LITERS
VAR_DEMAND_WATER_PER_HOUSE = 50 # LITERS

# This can be evaluated using the vision api
MEAN_AREA_PER_HOUSE = 100 # METERS SQUARE
VAR_AREA_PER_HOUSE = 50 # METERS SQUARE PER HOUSE

RAINFALL_ESTIMATE = 100 # mm
FC_TANK_PLACEMENT = 10000 # Rs.
FIXED_COST_PIPE_PER_METER = 120 # Rs.
COST_PER_LITERS_TANK = 500 # Rs.


# ## Data to save and feed to algorithm

# In[22]:


house_data_x = dat['x'].values
house_data_y = dat['y'].values

# demand
demand_per_house = np.array([np.random.normal(loc = MEAN_DEMAND_WATER_PER_HOUSE, scale = VAR_DEMAND_WATER_PER_HOUSE) for i in range(NUM_HOUSES)])

#area
area_per_house = np.array([np.random.normal(loc = MEAN_AREA_PER_HOUSE, scale = VAR_AREA_PER_HOUSE) for i in range(NUM_HOUSES)])

# rainfall estimation
rainfall_estimate_for_city =  np.array([RAINFALL_ESTIMATE for i in range(NUM_HOUSES)]) # FLOAT

# capacity of the tanks per house (DERIVED)
capacity_for_tank_per_house = np.array([area_per_house[i]* RAINFALL_ESTIMATE/1000  for i in range(NUM_HOUSES)])

# average_length_of_pipe_per_house
average_length_of_pipe_per_house = np.random.normal(loc = 30, scale = 40, size = NUM_HOUSES)

# fixed_cost_of_tank_placement_per_house
fixed_cost_of_tank_placement_per_house = np.array([FC_TANK_PLACEMENT for i in range(NUM_HOUSES)])

# cost_per_liters_tank
cost_per_liters_tank_per_house = np.array([COST_PER_LITERS_TANK for i in range(NUM_HOUSES)])


# In[23]:


# print('House_data_x', (house_data_x.shape) )
# print('House_data_y', (house_data_y.shape))
# print('Demand_per_house', (demand_per_house.shape))
# print('Capacity_for_tank_per_house', (capacity_for_tank_per_house.shape))
# print('Rainfall_estimate_for_city', (rainfall_estimate_for_city.shape))
# print('Average_length_of_pipe_per_house', (average_length_of_pipe_per_house.shape))
# print('fixed_cost_of_tank_placement_per_house', (fixed_cost_of_tank_placement_per_house.shape))
# print('cost_per_liters_tank_per_house', (cost_per_liters_tank_per_house.shape))


# ## A visual representation of our data

# In[24]:


# sns.scatterplot(house_data_x, house_data_y, hue = house_data_labels)
# plt.figure(figsize = (12,12))
# plt.scatter(x= house_data_x, y= house_data_y )
# plt.xlabel("house x")
# plt.ylabel("house y")
# plt.show()


# In[25]:


df = pd.DataFrame(data = None, columns = None)
df['house_data_x'] = house_data_x
df['house_data_y'] = house_data_y
df['demand_per_house_liters'] = demand_per_house
df['area_per_house_metersq'] = area_per_house
df['capacity_for_tank_per_house_lt'] = capacity_for_tank_per_house
df['rainfall_estimate_for_city_mm'] = rainfall_estimate_for_city
df['average_length_of_pipe_per_house'] = average_length_of_pipe_per_house
df['fixed_cost_of_tank_placement_per_house'] = fixed_cost_of_tank_placement_per_house
df['cost_per_liters_tank_per_house'] = cost_per_liters_tank_per_house


df = df.round(3)
# df.head()


# In[26]:


df.to_csv("data.csv", index= False, header=True)


# Generating or getting the data for the tanks:
# 
# - Web App allows us to pip point the map and get the generated data in csv format

# ## Working with the tanks data
# - Real data
# - Taken directly from our web app
# 

# In[ ]:





# In[27]:


import csv

tank_data_from_website = []
with open('tank_loc_website.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            x = row[0]
            y = row[1]
            tank_data_from_website.append([x,y])
            line_count += 1
#     print(f'Processed {line_count} lines.')

tank_data_from_website = np.array(tank_data_from_website)
# print(tank_data_from_website.shape)
                  
NUM_TANKS = len(tank_data_from_website)

tanksdf = pd.DataFrame(data = None, columns = None)
tanksdf['tanks_x'] = tank_data_from_website[:,1]
tanksdf['tanks_y'] = tank_data_from_website[:,0]
tanksdf = tanksdf.round(3)
tanksdf.to_csv("tanks_loc.csv", index = False, header = True)


                  
                  


# # Solution 1: Clustering

# In[29]:


tanks = pd.read_csv("tanks_loc.csv")
houses = pd.read_csv("data.csv")

# print(houses.head(3))
# print()
# print(tanks.head(3))


# In[30]:


# defining the variables
NUM_TANKS = len(tanks)
NUM_HOUSES = len(houses)
# print('Number of tanks and houses are: ',NUM_TANKS, NUM_HOUSES )

# FOR EVERY HOUSE AND TANK, ASSIGN EVERY HOUSE A NEAREST TANK BASED ON THE CLUSTER

# CREATING 2D ARRAY OF TANKS
tanks_houses = [[] for j in range(NUM_TANKS)]

for i in range(len(houses)):
    # LOC OF HOUSE
    hx, hy = houses.house_data_x.iloc[i],houses.house_data_y.iloc[i]
    min_dist_from_house_to_tank = np.inf
    min_dist_tank = None
    hx*=1000
    hy*=1000
    
    for j in range(len(tanks)):
        # LOC OF TANKS
        tx, ty = tanks.tanks_x.iloc[j], tanks.tanks_y.iloc[j]
        
        # converting lat long to the actual distance based coordinates
        # can be optimised
        
        tx*=1000
        ty*=1000
        
#         print(tx,ty, hx, hy)
        # DIST ~ APPROX ~ EUCLIDIAN DISTANCE
        dist = np.sqrt( (ty- hy)**2 + (tx- hx)**2)
        
        if dist<min_dist_from_house_to_tank:
            min_dist_from_house_to_tank = dist
            min_dist_tank = j
            
    tanks_houses[min_dist_tank].append(i) # appending the house
    
# print('houses clustered to tanks')
# tank_index = 0
# for x in tanks_houses[:]:
#     print('Tank index = {0}'.format(tank_index),'\nhouses:',x)
#     print()
#     tank_index+=1


# ## Calculating the capacity and where not to place tanks

# In[34]:


# ASSUMING THE DATA FOR CIJ
def calculate_capacity_of_tanks(tanks_houses):
    capacity_of_jth_tank = []
    for j in range(len(tanks_houses)):
        houses_tank = tanks_houses[j]
        capacity = np.sum(houses_tank)
        capacity_of_jth_tank.append(capacity)
    return capacity_of_jth_tank
capacity_of_jth_tank= calculate_capacity_of_tanks(tanks_houses)
# print('capacity of jth tank(10 tanks here)',capacity_of_jth_tank[:10]) 
# print()
# print()
# print('tanks with no capacity(no houses connected) are:', [tank for tank in range(len(capacity_of_jth_tank)) if capacity_of_jth_tank[tank]<=0])


# Main step is to calculate the CIJ,tie the cost of pipe from i'th house to j'th tank
# 
# - can be optimised
# - moving forward with the assumptions

# In[35]:


# CIJ CALCULATION
FIXED_COST_OF_PIPES_PER_METER = 120
CIJ = [[0 for i in range(NUM_TANKS)] for j in range(NUM_HOUSES)]
# print(np.array(CIJ).shape) # TODO

for i in range(NUM_HOUSES):
    hx, hy = houses.house_data_x.iloc[i],houses.house_data_y.iloc[i]
    hx*=1000
    hy*=1000
    for j in range(NUM_TANKS):
        tx, ty = tanks.tanks_x.iloc[j], tanks.tanks_y.iloc[j]
        
        tx*=1000
        ty*=1000
        dist = np.sqrt( (ty- hy)**2 + (tx- hx)**2)
        
        CIJ[i][j]= dist*FIXED_COST_OF_PIPES_PER_METER

CIJ = np.array(CIJ)


# In[36]:


cost_of_setting_jth_tank = []
for j in range(len(tanks_houses)):
    houses_linked_to_tank = tanks_houses[j]
    cost = 0
    if capacity_of_jth_tank[j] >0: 
        cost = houses.cost_per_liters_tank_per_house[j]
    else :
        cost = 0
        
    for house_index in (houses_linked_to_tank):
        cost += CIJ[house_index][j]
    
    cost_of_setting_jth_tank.append(cost)
        
# zip(cost_of_setting_jth_tank) # TODO


# In[41]:


# giving the data to the backend of our web application
import numpy as np
import codecs, json 

List = [{} for j in range(NUM_TANKS)]

for j in range(NUM_TANKS):
    List[j]['x'] = tanks['tanks_x'].iloc[j].astype('float32')
    List[j]['y'] = tanks['tanks_y'].iloc[j].astype('float32')
    List[j]['stability'] = 1.00
    List[j]['capacity'] = capacity_of_jth_tank[j].astype('float32')
    List[j]['cost_of_making'] = cost_of_setting_jth_tank[j]
    
temp = pd.DataFrame(List)
# temp.head()


# ### Tanks that should not be constructed

# In[39]:


# print('tanks with no capacity(no houses connected) are:', [tank for tank in range(len(capacity_of_jth_tank)) if capacity_of_jth_tank[tank]==0])


# ## JSON passed to backend of the website

# In[40]:


values = temp.values
print(json.dumps(values.tolist())) # TODO 
# FINAL


# In[ ]:





# In[ ]:




