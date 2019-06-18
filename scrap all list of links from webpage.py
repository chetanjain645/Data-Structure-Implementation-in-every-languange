#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


url = "https://www.statista.com/chartoftheday/"


# In[5]:


response = requests.get(url)
response


# In[7]:


data = response.text


# In[8]:


data


# In[9]:


soup = BeautifulSoup(data, 'html.parser')


# In[10]:


tags = soup.find_all('a')


# In[11]:


for tag in tags:
    print(tag.get('href'))


# In[ ]:





# In[ ]:




