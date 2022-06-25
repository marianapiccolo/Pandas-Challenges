#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('marketing_campaign.csv', sep = '\t')
df.head()


# In[3]:


df.info()


# <h1>Conditional filtering</h1>

# In[4]:


df['Marital_Status'] == 'Married' #married in each row


# In[5]:


df[df['Marital_Status'] == 'Married'] #dataframe with married


# In[6]:


df.loc[df['Marital_Status'] == 'Married'] # the same result


# ## Chained conditional

# In[7]:


df['Marital_Status'].value_counts()


# In[8]:


df.loc[-df['Marital_Status'].isin(['Married', 'Together']) & (df['Year_Birth'] > 1990)] #customers without a partner who are born after 1990


# ## Use multiple conditionals to create new features

# In[15]:


df.loc[(df['NumWebPurchases'] > 5) | (df['NumDealsPurchases'] > 5), 'ActiveOnlineBuyers'] = 'Active' #customers who buy online more than 5 web or deals purchases = 'Active' in the new column 'ActiveOnlineBuyers'
df.loc[(df['NumWebPurchases'] < 5) & (df['NumDealsPurchases'] < 5), 'ActiveOnlineBuyers'] = 'Not Active' ##customers who did not buy online more than 5 web and did not buy deals purchases = 'Not Active' in the new column 'ActiveOnlineBuyers'
df.head()


# ## Campaign for targeting highly educated folks above a certain income with no(zero) or one kid

# In[16]:


df['Education'].value_counts()


# In[19]:


ed_class = ['Graduation', 'PhD', 'Master'] #list with degrees aceptable
criteria_ed = df['Education'].isin(ed_class) #education criteria
criteria_sal = df['Income'] > 65000 #salary criteria
criteria_kids = df['Kidhome'] < 1 # kids criteria - no kids at home
criteria_final = (criteria_ed & criteria_sal & criteria_kids)


# In[20]:


df.loc[criteria_final] #customers with advanced degrees, income more than 65000 and no children living at home

