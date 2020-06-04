#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd


# In[6]:


data=pd.read_csv('Data.csv')


# In[7]:


data
data=data.fillna(data.mean())
data


# In[8]:


X=data.iloc[:,0:5].values
X


# In[9]:


Y=data.iloc[:,5].values
Y


# # MISSING DATA

# In[10]:


from sklearn.impute import SimpleImputer


# In[11]:


get_ipython().run_line_magic('pinfo', 'SimpleImputer')


# In[12]:


imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
imputer


# In[13]:


x1=imputer.fit_transform(data)


# In[14]:


df=pd.DataFrame(x1)
df


# In[15]:


X


# In[16]:


from sklearn.preprocessing import LabelEncoder,OneHotEncoder


# In[17]:


le_x=LabelEncoder()
le_y=LabelEncoder()


# In[26]:


X[:,0]=le_x.fit_transform(X[:,0])
X[:,2]=le_x.fit_transform(X[:,2])
X[:,3]=le_x.fit_transform(X[:,3])
Y=le_y.fit_transform(Y)


# In[27]:


X


# In[20]:


Y


# In[28]:


ohe=OneHotEncoder(categorical_features=[0])
X=ohe.fit_transform(X).toarray()
X


# In[30]:


Y


# In[32]:


from sklearn.model_selection import train_test_split


# In[35]:


X_train,X_test,Y_train,Y_t=train_test_split(X,Y,test_size=0.4)


# In[36]:


X_train


# In[37]:


from sklearn.preprocessing import StandardScaler


# In[38]:


sc_x=StandardScaler()


# In[39]:


X_train=sc_x.fit_transform(X_train)
X_train=sc_x.fit_transform(X_test)


# In[40]:


X_train


# In[41]:


X_test


# In[ ]:




