#!/usr/bin/env python
# coding: utf-8

# In[1]:
import json

def keys():
    with open('twitter_credentials.json') as data_file:
        data = json.load(data_file)
    consumer_key =  data['consumer_key']
    consumer_secret=  data['consumer_secret']
    access_key = data['access_key']
    access_secret = data['access_secret']
    return consumer_key,consumer_secret,access_key,access_secret


# In[8]:





# In[9]:





# In[ ]:




