#!/usr/bin/env python
# coding: utf-8

# In[14]:


#zero divisible error
def ze(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("number is not divisible by 0")
    
print(ze(90,0))


# In[21]:


#with finally keyword

try:
    z = 5//0
    print(z)
    
except ZeroDivisionError:
    print("cannot be divisible by 0")
    
finally:
    print("the task is completed")


# In[ ]:




