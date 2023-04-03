#!/usr/bin/env python
# coding: utf-8

# In[1]:


#basics of python
#creating a variable
interger = 500
float = 500.00
string = "london"
print(interger)
print(float)
print(string)


# In[7]:


#create multiple variables with a single value simultaneoulsy

x=y=z=500
print(x)
print(y)
print(z)


# In[9]:


#multiple ojects to multiple variables
i,j,k = 500,500.00,"ice"
print(i,j,k)


# In[15]:


#python numeric datatype
d = 500
e = 500.00
f = 5j+7
print("data type of ", d ,"is" ,type(d))
print("data type of ", e ,"is" ,type(e))
print("data type of ", f ,"is" ,type(f))


# In[16]:


#python string datatype
string = 'london'
print(string)


# In[29]:


#sling a string 
print(string[2:5])
print(string[2:])
#multiply the string
print(string*2)
#concatenate
print(string+"","city")


# In[39]:


#arithmetic operators
y = 10
z = 90

print("addition:",y+z)
print("subtraction:",y-z)
print("multiplication:",y*z)
print("division:",y/z)
print("floor division:",y//z)
print("modulus:",y%z)
print("exponent:",y**z)


# In[41]:


#comparison operators

a = 30
b = 70

#equal
print(a==b)
#not equal
print(a!=b)
#less than
print(a<b)
#less than or equal to
print(a<=b)
#greater than
print(a>b)
#greater than or equal to
print(a>=b)


# In[47]:


#for loop with range and incrememt:
for i in range(0,10,2):
    print(i)
for i in range(1,11,2):
    print(i)


# In[ ]:


#for loops in list:

