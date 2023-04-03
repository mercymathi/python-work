#!/usr/bin/env python
# coding: utf-8

# In[14]:


##LIST EXERCISES

a=[22,"python",True]
for i in range(len(a)):
   print(a[i],type(a[i]))
   


# In[22]:


a=[23,4,67,22,45]
count=0
for i in range(len(a)):
    count+=1
    print(count)


# In[23]:


a=[23,4,67,22,45]
a.reverse()
print(a)


# In[46]:



a = [23, 4, 67, 22, 45]

for i in range (len(a)):
    b = a[i]*a[i]
    print(b,end=' ')


# In[57]:


a = [23, 4, 67, 22, 45]
sum = 0 
for i in a:
    sum +=i
print(sum)


# In[60]:


a = [23, 4, 67, 22, 45]
m = 1
for i in a:
    m*=i
print(m)


# In[ ]:




