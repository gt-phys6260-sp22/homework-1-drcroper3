#!/usr/bin/env python
# coding: utf-8

# ##### PHYS 6260: Homework 1, Christopher Roper

# ## Problem 2
# 
# The goal of HW1 is to modify the Jupyter notebook by answering questions 2a) through 2d). The assumptions are also listed within the following quesitons to perform: 
# 
# a) Create a 100 x 3 array with random numbers. The 100 position vectors is assumed to initially be in Cartesian Coordinates.
# 
# b) Create scatter plot of x vs z in Cartesian Coordinates
# 
# c) Generate a function that converts Cartesian to Cylinderical Coordinates
# 
# d) Use numpy toolbox and compute radial coordinate values for:
# 
# * Mean
# * Minimum 
# * Maximum

# ### Part (a)

# In[1]:


import numpy as np

#randomize array of numbers in position Vectors
positionVectors=np.random.random((100,3))
#reshape position vector to 100,3
positionVectors=positionVectors.reshape(100,3)


# ### Part (b)

# In[2]:


import matplotlib.pyplot as plt
#scatter position vectors points
plt.scatter(positionVectors[:,0],positionVectors[:,1])
plt.xlabel('X-axis')
plt.ylabel('Z-axis')
plt.title('X vs. Z')
plt.show()


# ### Part (c)

# In[4]:


#position Vector Value
z=positionVectors
x=positionVectors[:,0]
y=positionVectors[:,1]


#function to convert cartesian to cylindrical, return r,z
def cartesianToCylindrical(x,y,z):
    z=z
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y,x)
    return(r,theta,z)

#print cylinricl coordinates    
print(cartesianToCylindrical(x,y,z))


# ### Part (d)

# In[5]:


#calculate radial coordinate formula
r = np.sqrt(x**2 + y**2)


#calling function to receive radial coordinate
#cartesianToCylindrical(x,y,z)

#find the mean, min, max of radial coordinate
print("mean:",np.mean(r))
print("min:",np.min(r))
print("max:",np.max(r))




# In[ ]:





# In[ ]:




