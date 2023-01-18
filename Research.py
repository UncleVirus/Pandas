# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

""" Complete your solution to the first research task here,
which involves the data file named temperatures.csv and using the 
variable names as directed in the assignment."""

data = pd.read_csv('temperatures.csv' , encoding = 'Latin1')
print('Shape: ',data.shape)
data.head()

#create a variable called myTemps and assign it to the list of floating point values

myTemps = [float(temp[:-3]) for temp in data] # Assign you solution to this variable
myTemps[:5]
""" Complete your soution to the second research task here, which 
    involves combining numpy arrays """


x = np.array([0,1,2,3])
y = np.array([4,5,6,7])
z = [[x[loop1],y[loop1]] for loop1 in range(len(x))]
z