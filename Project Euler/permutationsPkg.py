#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ncr(n,r):    
    prod=1
    if(n<r):
        return 0
    if(n==0):
        return 0
    while(r>=1):
        prod*=n/r        
        n-=1
        r-=1    
    return int(prod)        


# In[2]:


res=ncr(11,6)
print(res)


# In[3]:


import math


# In[4]:


def npr(n,r):
    return ncr(n,r)*math.factorial(r)


# In[5]:


res=npr(11,6)
print(res)

