# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 04:59:22 2024

@author: The_Makoris
"""

from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

#Create line chart years on x-axis, gdp on y-axis

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

#Add  title
plt.title("Nominal GDP")

#Add label to the y-axis
plt.ylabel("Billions of $")
plt.show()
