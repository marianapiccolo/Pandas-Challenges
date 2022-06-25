#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# <h1>Reading data from CSV and Excel files</hi>

# In[4]:


# Read file and add column name
df = pd.read_csv("auto_mpg.csv", header = 0,
                 names = ['MPG','Cylinders','Displacement',\
                          'Horsepower','Weight',
                 'Acceleration', 'Model Year', 'Origin'])

df.head()


# <h1>Checking dataframe information and attributes</h1>

# In[5]:


df.shape #show the shape of dataframe


# In[6]:


df.columns #show the name of the columns
list(df.columns) #create a list


# In[7]:


df.info() #all information about the data


# In[8]:


df.index


# In[9]:


df.dtypes


# <h1>Study the summary statistics of numerical and catergorical columns</h1>

# In[10]:


df.describe()


# In[11]:


df.describe(include = 'object') # an object 


# In[12]:


df.value_counts(['Origin']) #frequence


# In[13]:


df.value_counts(['Origin']).plot(kind = 'bar') #graph


# <h1>Selecting columns and creating columns</h1>

# In[16]:


# 3 new columns 
df['displacement_on_power'] = df['Displacement']/df['Horsepower']
df['weight_per_cylinder'] = df['Weight']/df['Cylinders']
df['acc_per_cyl'] = df['Acceleration']/df['Cylinders']
df.head()

