#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


camp_df = pd.read_csv('marketing_campaign.csv', sep = '\t')
camp_df.head()


# In[4]:


camp_df.info()


# <h1>Selecting multiple columns</h1>

# In[5]:


#subset the original df to contain only columns pertaining to the amount of product purchased by customers
mnt_purchases = camp_df[
    [
        'ID',
        'MntWines',
        'MntFruits',
        'MntMeatProducts',
        'MntFishProducts',
        'MntSweetProducts',
        'MntGoldProds'
    ]
]


# In[6]:


mnt_purchases


# <h1>Subsetting rows from the dataframe using .loc[]</h1>

# In[7]:


camp_df.set_index('ID', inplace=True)
camp_df


# In[8]:


camp_df.loc[9405] #info about customer 9405


# In[9]:


camp_df.loc[7446:2114] #info from 7446 to 2114


# In[10]:


camp_df.loc[7446:2114, 'MntWines':'MntGoldProds'] # info from 7446 to 2114, from Column MntWines to MntGoldProds


# In[11]:


camp_df.reset_index(inplace=True)
camp_df


# In[16]:


camp_df.iloc[50:301:2,-9:] #rows from 50 to 300 and last 9 columns

