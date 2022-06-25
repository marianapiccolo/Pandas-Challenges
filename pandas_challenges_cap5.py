#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('marketing_campaign.csv', sep='\t')
df.head()


# In[3]:


df.info()


# ## Grouping and aggregation

# In[4]:


#list of interested columns
amount_bought = [
        'MntWines',
        'MntFruits',
        'MntMeatProducts',
        'MntFishProducts',
        'MntSweetProducts',
        'MntGoldProds'
    ]


# In[6]:


df.groupby(['Marital_Status']).mean()[amount_bought]


# ## Grouping by multiple columns

# In[8]:


df.groupby(['Education', 'Marital_Status'])['Income'].agg(['median','mean'])


# ## Applying a custom aggregate function

# In[9]:


df


# In[13]:


def top(df, n=5, column = 'NumWebPurchases'): #top 5 online purchase 
    return df.sort_values(by = column)[-n:]


# In[14]:


purchases = ['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
df.groupby(['Education']).apply(top)[purchases] #top 5 online purchase from each group based by their education level

