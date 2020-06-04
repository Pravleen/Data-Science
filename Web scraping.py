#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url="https://www.imdb.com/chart/boxoffice?ref_=nv_ch_cht_1"
html=requests.get(url)


# In[5]:


bsObj=BeautifulSoup(html.text,'lxml')


# In[8]:


bsObj.find('title').getText()


# In[18]:


h1list=bsObj.findAll('h1')


# In[15]:


for h1 in h1list:
    print(h1)


# In[16]:


h4list=bsObj.findAll('h4')


# In[17]:


for h4 in h4list:
    print(h4)


# In[20]:


titlelist=bsObj.findAll('td',{'class':'titleColumn'})


# In[23]:


for title in titlelist:
    print(title.getText())


# # ACTIVITY

# In[94]:


url1="https://www.reuters.com/companies/GOOG.O/people"
http1=requests.get(url1)


# In[95]:


http1


# In[96]:


bsObj1=BeautifulSoup(http1.text,'lxml')


# In[97]:


bsObj1


# In[100]:


import csv


# In[ ]:





# In[99]:


tables=bsObj1.find('table',{'class':'table-container MarketsTable-officers-1Yb5u'})
tables.text


# In[136]:


table1=[]
header=[]
for th in tables.findAll("th"):
        header.append(th.text.strip())
table1.append(header)
for table in tables.findAll('tr'):
    columns=table.findAll('td')
    table2=[]
    for column in columns:
        table2.append(column.text.strip())
    table1.append(table2)
with open('Output1.csv','w+') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(table1)


# In[ ]:





# In[62]:





# In[ ]:





# In[72]:





# In[73]:





# In[ ]:





# In[ ]:





# In[ ]:




