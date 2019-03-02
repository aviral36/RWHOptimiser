#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import pandas as pd
import numpy as np
import seaborn as sns


# In[8]:


import json
from pprint import pprint

with open('delhi_highway.json') as f:
    data = json.load(f)

print(dir(data))


# In[12]:


data.keys()


# In[13]:


data['type']


# In[15]:


len(data['features'])


# In[22]:


data['features'][0]['geometry']['coordinates']


# In[27]:


import json
from pprint import pprint
import codecs

# with open('delhi_location.json',  encoding='utf-8') as f:
#     data = json.load(f)


data = json.load(codecs.open('delhi_location.json', 'r', 'utf-8-sig'))


# In[28]:


data

