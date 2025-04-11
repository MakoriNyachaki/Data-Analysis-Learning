# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 05:36:13 2024

@author: The_Makoris
"""

##
# This program provides a simple test of the car class
#
from car import Car

def main():
    aPlainCar = Car()
    printInfo(aPlainCar)
    
    aLimo = Car()
    aLimo.setLicenseNumber("WHOHOO")
    aLimo.setNumberOfTires(8)
    printInfo(aLimo)
    
def printInfo(car):
    print(car.getDescription())
    print("Tires", + car.getNumberOfTires())
    
# Start the program
main()