#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
import numpy as np
import urllib


# In[64]:


tanks = pd.read_csv("tanks_loc.csv")
houses = pd.read_csv("data.csv")


# In[65]:


houses.head(3) # TODO


# In[66]:


tanks.head(3) # TODO


# In[67]:


NUM_TANKS = len(tanks)
NUM_HOUSES = len(houses)


# In[68]:


NUM_TANKS, NUM_HOUSES # TODO


# In[69]:


# FOR EVERY HOUSE AND TANK, ASSIGN EVERY HOUSE A NEAREST TANK BASED ON THE CLUSTER

# CREATING 2D ARRAY OF TANKS
tanks_houses = [[] for j in range(NUM_TANKS)]

for i in range(len(houses)):
    # LOC OF HOUSE
    hx, hy = houses.house_data_x.iloc[i],houses.house_data_y.iloc[i]
    min_dist_from_house_to_tank = np.inf
    min_dist_tank = None
    
    for j in range(len(tanks)):
        # LOC OF TANKS
        tx, ty = tanks.tanks_x.iloc[j], tanks.tanks_y.iloc[j]
        
        # DIST ~ APPROX
        dist = np.sqrt( (ty- hy)**2 + (tx- hx)**2)
        
        if dist<min_dist_from_house_to_tank:
            min_dist_from_house_to_tank = dist
            min_dist_tank = j
            
    tanks_houses[min_dist_tank].append(i) # appending the house
    
tanks_houses[:10] # TODO


# In[70]:


len(tanks_houses) # TODO 
# COMMENT OUT THIS LINE


# In[71]:


# ASSUMING THE DATA FOR CIJ
def calculate_capacity_of_tanks(tanks_houses):
    capacity_of_jth_tank = []
    for j in range(len(tanks_houses)):
        houses_tank = tanks_houses[j]
        capacity = np.sum(houses_tank)
        capacity_of_jth_tank.append(capacity)
    return capacity_of_jth_tank
capacity_of_jth_tank= calculate_capacity_of_tanks(tanks_houses)
'capacity of jth tank',capacity_of_jth_tank[:10] # TODO


# In[72]:


print('tanks with no capacity(no houses connected) are:', [tank for tank in range(len(capacity_of_jth_tank)) if capacity_of_jth_tank[tank]==0])
# TODO


# In[82]:


FIXED_COST_OF_PIPES_PER_METER = 100
CIJ = [[0 for i in range(NUM_TANKS)] for j in range(NUM_HOUSES)]
print(np.array(CIJ).shape) # TODO
for i in range(NUM_HOUSES):
    hx, hy = houses.house_data_x.iloc[i],houses.house_data_y.iloc[i]
    for j in range(NUM_TANKS):
        tx, ty = tanks.tanks_x.iloc[j], tanks.tanks_y.iloc[j]
        dist = np.sqrt( (ty- hy)**2 + (tx- hx)**2)
        
        CIJ[i][j]= dist*FIXED_COST_OF_PIPES_PER_METER

CIJ = np.array(CIJ)


# In[86]:


cost_of_setting_jth_tank = []
for j in range(len(tanks_houses)):
    houses_linked_to_tank = tanks_houses[j]
    cost = 0
    if capacity_of_jth_tank[j] >=0: 
        cost = houses.cost_per_liters_tank_per_house[j]
    for house_index in (houses_linked_to_tank):
        cost += CIJ[house_index][j]
        
    cost_of_setting_jth_tank.append(cost)
        
cost_of_setting_jth_tank # TODO


# In[99]:


houses.head() # TODO


# In[87]:


# import sys

# sys.argv[1]
# sys.argv[2]  


# In[ ]:


import numpy as np
import codecs, json 

List = [{} for j in range(NUM_TANKS)]

for j in range(NUM_TANKS):
    List[j]['x'] = tanks['tanks_x'].iloc[j].astype('float32')
    List[j]['y'] = tanks['tanks_y'].iloc[j].astype('float32')
    List[j]['stability'] = 1.00
    List[j]['capacity'] = capacity_of_jth_tank[j].astype('float32')
    List[j]['cost_of_making'] = cost_of_setting_jth_tank[j].astype('float32')
    
temp = pd.DataFrame(List)
temp.head()


# In[116]:


temp.head()


# In[114]:


values = temp.values
print(json.dumps(values.tolist())) # TODO 
# FINAL

