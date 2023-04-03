#!/usr/bin/env python
# coding: utf-8

# In[14]:


#open a file

file = open ('C:/file handling.txt','r')
print(file.read())
#or
f = open('C:/myfile.txt','r')
for each in f:
    print(each)


# In[15]:


#read lines
f = open('C:/myfile.txt','r')
print(f.read(5))


# In[25]:


#write in a file
fwrite = open('C:/file handling.txt','w')
fwrite.write("writing in file handling file")
fwrite.write("when you write in an existing file, the already written subjects will get deleted")
fwrite.close()


# In[26]:


#appending in a file
fwrite = open('C:/file handling.txt','a')
fwrite.write("this is the append method")
fwrite.close()


# In[27]:


#reading a file using with function
with open('C:/file handling.txt') as file1:
    a = file1.read()
    print(a)


# In[29]:


#split in file handling
with open('C:/file handling.txt') as file1:
    a = file1.readlines()
    for b in a:
        w = b.split()
        print(w)
 


# In[ ]:




