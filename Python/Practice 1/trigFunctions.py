# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:16:46 2023

@author: Lenovo
"""

##
# This program creates a line graph containing the curves for the sine and
# cosine trigonometric functions for x-values between –180 and 180 degrees.
#

from matplotlib import pyplot
from math import pi, cos, sin

# Create empty lists to store y-values for sine and cosine curves
cosY = []
sinY = []


##
# Create an empty list to store the x values for cosine and sine curves
# x-values ill be the same for both
#

trigX = []

# Compute the y-values for both the sine and cosine curves

angle = -180

while angle <= 180:
    x = pi / 180 * angle
    trigX.append(x)
    
    y = sin(x)
    sinY.append(y)
    
    y = cos(x)
    cosY.append(x)
    
    angle = angle + 1


# Plot two curves

pyplot.plot(trigX, cosY)
pyplot.plot(trigX, sinY)


# Add descriptive information
pyplot.title("Trigonometric Functions")

# Improve the appearance of the graph
pyplot.legend("cos(x)", "sin(x")
pyplot.grid("on")
pyplot.axis("equal")
pyplot.axhline(color="k")
pyplot.axvline(color="k")


pyplot.show()
