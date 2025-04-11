# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:28:41 2024

@author: The_Makoris
"""

##
# This program computes a triangle number using recursion.
#

def main():
    area = triangleArea(10)
    print("Area: %d " % area)
    print("Expected: 55")
    
##
# Computes the area of a triangle with a given side length
# @param sideLength the side of the triangle base
# @return the area
#

def triangleArea(sideLength):
    if sideLength <= 0:
        return(0)
    if sideLength == 1:
        return(1)
    
    smallerSideLength = sideLength - 1
    smallerArea = triangleArea(smallerSideLength)
    area = smallerArea + sideLength
    return(area)

# Start the program
main()