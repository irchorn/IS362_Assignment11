#!/usr/bin/env python
# coding: utf-8

# # IS 362 Assignment 11

# <b>Use requests in Python to pull the json files</b>

# In[46]:


import json
import os
import requests
import time
import datetime

import pandas as pd


# In[47]:


end = datetime.date.today()
start = datetime.date(2021, 3, 26)
print('Start date ' + str(start))
print('End date ' + str(end))


# In[59]:


data_item = 
your_key = 'Q15AWEGLexxVtwiRoUDHilQtQcZ3GzOL'
url = 'https://api.nytimes.com/svc/topstories/v2/world.json?api-key='+your_key
r = requests.get(url)
json_data = r.json()
print(json_data)


# <b>Displaying data in a more readable way</b>

# In[61]:


str_data = json.dumps(json_data, indent=2)
print(str_data)


# In[87]:


world = json_data["section"] #I got stuck here becase I couldn't add ["subsection"] [title] [url]
print(world)


# In[54]:


import csv
file = 'world_news_today.csv'

with open(file, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)


# In[56]:


df = pd.read_csv( 'world_news_today.csv')
print(df.head())


# In[ ]:





# In[ ]:




