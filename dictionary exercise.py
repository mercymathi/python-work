#!/usr/bin/env python
# coding: utf-8

# In[7]:


#create a dictionary
dict={"name":"django",
     "time":"05:00 am",
     "place":"new york"}
print(dict)
print(dict["place"])


# In[8]:


#length of a dictionary
dict={"name":"django",
     "time":"05:00 am",
     "place":"new york"}
print(len(dict))


# In[25]:


#creating dictionary with different data types

dict={"name":"django",
     "time":5.00,
     "place":["new york"],
     "different_cities":("tokyo","london")
     }
print(type(dict["name"]))
print(type(dict["time"]))
print(type(dict["place"]))
print(type(dict["different_cities"]))


# In[30]:


#looping in dictionary
d={"name":"django",
     "time":"05:00 am",
     "place":"new york"}
for m in d.keys():
    print(m)


# In[31]:


dict={"name":"django",
     "time":"05:00 am",
     "place":"new york"}
for n in d.values():
    print(n)


# In[32]:


dict={"name":"django",
     "time":"05:00 am",
     "place":"new york"}
for p in d.items():
    print(p)


# In[ ]:




