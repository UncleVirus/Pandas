# -*- coding: utf-8 -*-
""" The data file for this is ozone.csv """

""" Write programming code using the variable names as directed 
    in the assignment.                                          """

import pandas as pd
# Read csv from ozone.csv
df_oz = pd.read_csv("ozone.csv")
print(df_oz)


# Get the correlation matrix
dfCorr = df_oz.corr()
print(dfCorr)
""" From the matix we can clearly see that temperature and ozone
 has the greatest magnitude of correlation with correlation value = 0.432301 
and we can see that wind and ozone has the least magnitude 
of correlation with correlation value = -0.03
"""
# Plot the graphs with appropriate captions and titles
import matplotlib.pyplot as plt
# set font size in plot
plt.rcParams["font.size"] =9
# set figure size
plt.figure(figsize=(10,10))
# Plot the scatter plot between ozone and temperature
plt.scatter(df_oz["ozone"],df_oz["temperature"])
# Add appropriate axes labels and titles
plt.xlabel("ozone")
plt.ylabel("temperature")
plt.title("Scatter plot between Ozone and Temperature(Highly Correlated)")
# save as ozHi.jpg
plt.savefig("ozHi.jpg")
plt.show()
#%%
# Repeat the above same procedure,instead plot scatter plot for ozone and wind
plt.figure(figsize=(10,10))
plt.scatter(df_oz["ozone"],df_oz["wind"])
plt.xlabel("ozone")
plt.ylabel("wind")
plt.title("Scatter plot between Ozone and Wind(Least correlated)")
plt.savefig("ozLo.jpg")
plt.show()