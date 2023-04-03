#!/usr/bin/env python
# coding: utf-8

# In[9]:


#create a class
class mp:
    name='movie'
    age=25
    place='chennai'
print(mp.name)
print(mp.age)
print(mp.place)


# In[10]:


#with object creation
class mp:
    name='franklin'
    age=25
    place='france'
object=mp()
print(object.name)
print(object.age)
print(object.place)


# In[13]:


#creating class with state and variables
class Demo:
    a=90
    b=10
print(Demo.a)
print(Demo.b)
print(Demo)
obj=Demo()
print(obj.a)
print(obj.b)


# In[15]:


#modification of class
class Countries:
    c1="japan"
    c2="china"
    c3="india"
Countries.c1="USA"
print(Countries.c1)


# In[17]:


#modification of object
class Countries:
    c1="japan"
    c2="china"
    c3="india"
obj=Countries
obj.c1="canada"
print(obj.c1)


# In[30]:


#creating class and attribute instances
class Person:
    #instance attribute
    attribute = "human"
    #class attribute
    def __init__(self,name):
        self.name = name
tiffiny = Person("tiffiny")
print((tiffiny.__class__.attribute))
print((tiffiny.name))


# In[31]:


class Person:
    #instance attribute
    attribute = "human"
    #class attribute
    def __init__(self,name):
        self.name = name
tiffiny = Person("tiffiny")
print((tiffiny.__class__.attribute))
print((tiffiny.name))


# In[38]:


#inheritance parent and child class
class Person:
    def __init__(self,id_number,name,age):
        self.id_number = id_number
        self.name = name
        self.age = age
        
    def show(self):
        print((self.name))
        print((self.id_number))
        print((self.age))
        
class Employee(Person):
    def __init__(self,id_number,name,age,designation,place):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.designation = designation
        self.place = place
        
    def show(self):
        print(self.id_number)
        print(self.name)
        print(self.age)
        print(self.designation)
        print(self.place)
        
details = Employee("priya","idno00078","25","software engineer","bengaluru")
details.show()



# In[44]:


#polymorphism

class woman:
    
    def workculture(self):
        print("every women is working hard, but some of them don't")
    
class asian(woman):
    
    def workculture(self):
            print("the number of working women have increased since a decade in asian countries")
            
class european(woman):
    
    def workculture(self):
            print("But also the number working women gradually increases in the european countries")
            
#creating object
fact1 = woman()
fact2 = asian()
fact3 = european()

#object execution
fact1.workculture()
fact2.workculture()
fact3.workculture()

        
        


# In[56]:


#encapsulation

class audi:
    
    def __init__(self):
        self.highest_price = 9000000
    def selling_price(self):
        print(self.highest_price)
    def set_final_price(self,price):
        self.price = price
    
obj = audi()
obj.selling_price()
#setter function
obj.set_final_price = 10000000
obj.set_final_price


# In[ ]:




