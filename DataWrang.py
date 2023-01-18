# -*- coding: utf-8 -*-

""" The data file for this is WburgWeather.csv """

""" Write programming code to create the cleansed DataFrame here 
    using the variable name dfWeather for your DataFrame as directed 
    in the assignment.                                               """
#Using panda to wrangling data
import pandas as pd    

# read the data
dfWeather = pd.read_csv('WburgWeather.csv')
def f(x):
    if x[3]=='VRB':
        x[3]='Variable Direction'
    return x
dfWeather=dfWeather.apply(f,1)
dfWeather.tail(5)

#Saving the new data file
dfWeather.to_csv('newWeather.csv',index=False)

