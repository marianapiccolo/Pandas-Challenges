#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[11]:


stocks = pd.read_csv('stock_data.csv', index_col = 'Unnamed: 0', parse_dates = True)
stocks.head()


# In[12]:


stocks


# ## Calculate daily return

# In[14]:


rets = stocks.pct_change().dropna() #daily returns
rets


# In[15]:


get_year = lambda x : x.year
by_year_stocks = rets.groupby(get_year).sum() * 100
by_year_stocks # year return


# In[ ]:




