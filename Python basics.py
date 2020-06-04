#!/usr/bin/env python
# coding: utf-8

# # PYTHON

# In[1]:


x="Hello World"


# In[2]:


x.capitalize()


# In[3]:


p= lambda a: a+5


# In[4]:


p(10)


# In[5]:


def addFive(a):
    return(a+5)


# In[6]:


lst=[2,4,6,2,3,4,5]


# In[7]:


list(map(addFive,lst))


# In[8]:


list(filter(lambda a: a%2==0,lst))


# # What is 3.3 to the power of 5

# In[9]:


3.3**5


# # Create one dummy 10 character string and reverse it.

# In[10]:


s="PravleenKB"
print(s[::-1])


# # define one function which accept string in form of num1+or-num2
# 
# # Like :    2+3,  5-6, 10+12, 10-2, 234-45

# In[11]:


def cal(num1,num2):
    return int(num1)+int(num2)
cal("10","-2")


# # Create List and add 1 thousand different random string in it, each string must be of 2 character only.

# In[12]:


l=["aa","bb"]


# # NUMPY
# 

# In[13]:


import numpy as np


# In[14]:


vec=[1,2,3]


# In[15]:


np_vec=np.array(vec)
print(np_vec)


# In[16]:


mat=[[2,3,4],[3,4,5]]
np_mat=(np.array(mat))
print(np_mat)


# In[17]:


np.zeros((3,4))


# In[18]:


np.ones((2,3))


# In[19]:


np.eye(4)


# In[20]:


np.random.randn(3,5)


# In[21]:


np.random.randint(5,15,6)


# In[22]:


np.arange(4,9,3)


# In[23]:


np.linspace(2,13,5)


# In[24]:


np_mat.shape


# In[25]:


np_mat.min()


# In[26]:


np_mat.reshape(3,2)


# # Create numpy array which has all number divisible by 3 between 10 and 100.

# In[27]:


arr1=np.arange(10,100)
ans=(arr1[(arr1%3==0)])
print(ans)
print(type(ans))


# # Find Second largest value in above array.

# In[28]:


ans.sort()
print(ans[-2])


# In[29]:


n=np.random.randint(10,100,60)
print(n)
n.sort()
print(n)
print(n[-3])


# # PANDAS

# In[30]:


import pandas as pd


# In[31]:


s1=pd.Series([2,3,4],index=['a','b','c'])
s1


# In[32]:


s1['a']


# # DATAFRAMES

# In[33]:


df=pd.DataFrame(data=[[1,2,3],[3,4,5],[6,7,8]],columns=['C1','C2','C3'],index=['R1','R2','R3'])
df


# In[34]:


df['newC']=df['C1']+5
df


# In[35]:


df.drop('R3' ,axis=0)


# In[36]:


df.set_index('C3',inplace=True)


# In[37]:


df


# In[38]:


df.loc[3,:]


# In[39]:


df1=pd.DataFrame(data=np.array([['Science','A','S1',98.2],['Maths','A','S2',78],['English','A','S4',88],['Science','B','S4',91],['Maths','B','S5',80.9],['English','B','S6',88.9]]),columns=['SUBJECT','SECTION','NAME','Marks'])
print(df1)                             


# In[40]:


df1=df1.set_index(['SECTION','SUBJECT'])
df1


# In[41]:


df1.loc['A'].loc['Maths']


# In[42]:


df2=pd.DataFrame([[np.nan,2,3,np.nan],[3,np.nan,0,np.nan],[2,np.nan,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan]],columns=list('PRAV'),index=list('ABCD'))
df2


# In[43]:


df2.dropna(axis=1,how='all')


# In[44]:


df2.dropna(axis=0,how='all')


# In[45]:


df2['R'].fillna(df2['R'].mean())


# In[46]:


df2['R'].mean()


# In[47]:


df2.replace(3.0,"There was 3 here")


# In[48]:


df3=pd.DataFrame([['MI','FEMALE','P1',32,45],['RCB','MALE','P2',22,67],['RR','MALE','P3',23,55],['RCB','MALE','P4',44,8],['MI','FEMALE'
                                                                                                                  ,'P5',32,100],['RR','MALE','P6',33,45]],columns=['TEAM','SEX','NAME','AGE','SCORE'])
df3


# In[49]:


df3['TEAM'].value_counts()


# In[50]:


byteam= df3.groupby('TEAM')


# In[51]:


byteam.sum()


# In[52]:


byteam.mean()


# In[53]:


def congrats(x):
    if x >50:
        return "Congratulations"
    else:
        return ""


# In[54]:


df3['NAME']=df3['SCORE'].apply(congrats)+df3['NAME']


# In[55]:


df3


# In[56]:


bill=pd.read_html('https://en.wikipedia.org/wiki/The_World%27s_Billionaires')


# In[57]:


type(bill)


# In[58]:


bill[3]


# In[60]:


bill


# In[61]:


df5=pd.DataFrame(data=np.random.randint(1,100,(100,3)),columns=['C1','C2','C3'])


# In[62]:


df5


# In[63]:


df5.head()


# In[64]:


df5['C1'].plot.area()


# In[65]:


df5['C2'].plot.bar()


# In[66]:


df5['C2'].plot.barh()


# In[67]:


df.plot.bar()


# In[68]:


df5.plot.area()


# In[69]:


df5.plot.bar()


# In[70]:


df5['C2'].plot.line()


# In[71]:


df5['C2'].plot.box()


# In[72]:


df5.plot.box()


# In[73]:


df5.plot.scatter(x='C1',y='C2')


# In[74]:


df5.plot.hist()


# # MATPLOTLIB

# In[76]:


import matplotlib.pyplot as plt


# In[75]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[77]:


m=np.linspace(1,10,100)
y=np.sin(m)
z=np.cos(m)


# In[78]:


z


# In[96]:


fig=plt.figure()
ax=fig.add_axes([0.1,0.1,1,1])
ax.plot(m,y,c='red',alpha=0.6,marker='^',lw=3,label='sine')
ax.plot(m,z,c='green',alpha=0.7,marker='*',label='cosine')
ax.set_xlim(0,10)
ax.set_ylim(-1,1)
ax.legend()
ax.set_xlabel("Time")
ax.set_ylabel("AMP")
ax.set_title("GRAPH")


# # SUBPLOTS

# In[109]:


fig1,ax1=plt.subplots(nrows=1,ncols=2,figsize=(20,5))
ax1[0].plot(m,y,c='pink')
ax1[1].plot(m,z,c='grey')


# In[122]:


i=[1,2,3,4,5,6,7,8,9]
j=[7,6,5,4,3,3,4,5,6]


# In[123]:


plt.bar(i,j)


# In[113]:


plt.scatter(i,j)


# In[119]:


plt.hist(j)


# In[124]:


plt.box(i)


# In[126]:


pip install plotly


# In[1]:


import plotly.offline as plo


# In[2]:


pip install plotly==4.7.1


# In[4]:


import plotly.offline as pyo


# In[5]:


import numpy as np


# In[6]:


import pandas as pd


# In[7]:


import matplotlib.pyplot as plt


# In[97]:


d1f=pd.DataFrame(np.random.randn(10,1),columns=['C1'])
d1f


# In[98]:


d1f.plot()


# In[99]:


data=[{
    'x' :d1f.index,
    'y' :d1f['C1']
}]


# In[100]:


pyo.plot(data,filename='basic_plot.html')


# In[101]:


d2f=pd.DataFrame(data=np.random.randn(10,3),columns=['C1','C2','C3'])
d2f


# In[102]:


d2f.plot()


# In[117]:


data1=[{
    'x' :d2f.index,
    'y' :d2f['C1','C2','C3'],
    type:'line'
}]


# In[109]:


pyo.plot(data1,filename='py.html')


# In[18]:


import plotly.graph_objs as go


# In[59]:


a=np.arange(0,20,2)
b=np.random.randint(1,20,20)

  


# In[90]:


t1=go.Scatter(x=a,y=b,mode='lines +markers',name='SOMETHING')
t2=go.Scatter(x=a,y=b+6,mode='lines ',name='VNFJNV',)
data1=[t1,t2]


# In[91]:


pyo.plot(data1,filename='Scatter_plot.html')


# # BARCHART

# In[63]:


d=[go.Bar(
    x=['Grade-1','Grade-2','Grade-3'],
    y=[89,88,66]
)]


# In[64]:


pyo.plot(d,filename='Bar.html')


# In[ ]:




