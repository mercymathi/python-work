#!/usr/bin/env python
# coding: utf-8

# In[13]:


#add an item in tuple
a=("python","django","java")
b=list(a)
b.append("sql")
a=tuple(b)
print(a)


# In[21]:


#add an item in tuple without converting to list
a=("python","django","java")
b=("powerbi",)
a+= b
print(a)


# In[24]:


#iteration
a=("python","django","java")
for i in a:
    print(i)


# In[29]:


a=("python","django","java")
for i in range(len(a)):
    print(i)
    print(a[i])


# In[ ]:


a=("python","django","java")
i=0
while i<len(a):
    print(a[i])
    i=i+1
    


# In[2]:


a=("python")
print(type(a))


# In[ ]:




