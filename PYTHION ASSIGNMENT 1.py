#!/usr/bin/env python
# coding: utf-8

# # PYTHON ASSIGMENT 1

# QUESTION NO:3

# In[ ]:


pi=3.1415926535
diameter=12.0
radius=diameter/2
Volume=(4/3)*pi*radius**3
print("Volume of the sphere with diameter 12cm is",Volume)


# QUESION NO:1

# In[49]:


print('Number visible by 7 and not a multilpe of 5 between 2000 and 3000 are:\n')
## 2000 and 3000 are included
for x in range (2000,3001):  
    if(x%7==0 and x%5!=0):
        print(x,end=',')


# QUESTION NO:2

# In[8]:


firstname=input("Please enter first name :")
print(f'First name is {firstname}')
lastname=input("Please enter last name :")
print(f'First name is {lastname}')
f=firstname[::-1]
l=lastname[::-1]
print("Names in reversed order is",f,l)

