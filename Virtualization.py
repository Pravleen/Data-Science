#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


# In[4]:


x=np.arange(1,20,1)
y=np.random.randint(1,20,20)


# In[6]:


data=[go.Scatter(x=x,y=y,mode="markers")]
pyo.plot(data,filename="scatter.html")


# In[7]:


x=np.arange(1,20,1)
y=np.random.randint(1,20,20)
z=np.random.randint(1,20,20)


# In[8]:


data=[go.Scatter(x=x,y=y,mode="markers",marker=dict(size=z))]
pyo.plot(data,filename="bubble.html")


# In[9]:


x=np.arange(1,20,1)
y=np.random.randint(1,20,20)
z=np.random.randint(1,100,20)


# In[10]:


data=[go.Scatter(x=x,y=y,mode="markers",marker=dict(size=z))]
pyo.plot(data,filename="bubble.html")


# In[11]:


x=np.random.randint(1,100,500)
data=[go.Histogram(
    x=x,
    xbins=dict(size=10)
      )]
pyo.plot(data,filename="Histogram.html")


# In[12]:


x=np.random.randint(1,100,500)
data=[go.Histogram(
    x=x,
    xbins=dict(start=1,end=100,size=10)
      )]
pyo.plot(data,filename="Histogram.html")


# In[14]:


import plotly.figure_factory as ff


# In[15]:


x=np.random.randn(1000)
data=[x]
labels=['Distribution plot']
fig=ff.create_distplot(data,labels)
pyo.plot(fig,filename="Ditribution.html")


# In[ ]:




