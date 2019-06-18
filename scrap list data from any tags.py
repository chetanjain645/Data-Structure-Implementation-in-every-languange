#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://boston.craigslist.org/search/sof"


# In[4]:


response = requests.get(url)
response
data = response.text
soup = BeautifulSoup(data, 'html.parser')
titles = soup.find_all('a', {"class" : "result-title" })


# In[5]:


for title in titles:
    print(title.text)


# In[ ]:




