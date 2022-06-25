#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# <h1>Checking and handling missing values in the data</h1>

# In[2]:


df = pd.read_csv('landslides.csv')
df.head()


# In[3]:


df.info()


# In[4]:


df.isna().sum() #numbers of missing values


# In[6]:


df_null = df[df['date'].isnull()] # all nan dates
df_null


# In[7]:


df = df[-df['date'].isnull()] #date without nulls
df


# In[8]:


df['time'].value_counts()


# In[9]:


df['time'].isnull().sum()


# In[11]:


df['time'] = df['time'].fillna('Not Known') #fill na with Not Known
df


# In[12]:


df['time'].isnull().sum()


# In[13]:


mean_fatalities = df['fatalities'].mean()
mean_fatalities


# In[14]:


df['fatalities'] = df['fatalities'].fillna(mean_fatalities) # fill fatalities with the mean
df


# In[15]:


df['fatalities'].isnull().sum()


# <h1>Date time parsing using .to_datetime()</h1>

# In[16]:


df.info()


# In[17]:


df['date']


# In[20]:


df['parsed_date'] = pd.to_datetime(df['date'],format = '%m/%d/%y') # create a new column datetime
df['parsed_date']


# In[21]:


month_of_landslides = df['parsed_date'].dt.month #extract month from parsed date
month_of_landslides


# In[22]:


import seaborn as sns


# In[26]:


month_of_landslides = month_of_landslides.dropna() #drop na
sns.histplot(month_of_landslides, kde = False, bins = 12) #parsed_date = months
# it shows the distribuition of numbers of landslides across months of year


# <h1>Correcting the data format</h1>

# In[27]:


df['time'].value_counts()


# In[43]:


def format_time(x): # function to format hours with ':'
    if ':' in x.lower(): # if there is ':'
            if int(x.split(':')[0]) >= 12 and int(x.split(':')[0]) < 18: #split by ':' and get the first element to get the hour
                x = 'Afternoon'
            elif int(x.split(':')[0]) < 12:
                x = 'Morning'
            elif int(x.split(':')[0]) >= 18:
                x = 'Night'
    elif 'evening' in x.lower(): #other cases
        x = "Evening"
    elif 'morning' in x.lower() or 'dawn' in x.lower():
        x = "Morning"
    elif 'afternoon' in x.lower():
        x = "Afternoon"
    elif 'night' in x.lower():
        x = "Night"
    else:
        x = "Not Known!"
        
    return x


# In[44]:


df['time'] = df['time'].apply(format_time)


# In[45]:


df['time'].value_counts()

