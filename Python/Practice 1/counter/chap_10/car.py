# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 05:17:43 2024

@author: The_Makoris
"""

##
# This module defines classes that model the Vehicle class
#

# A generic vehicle superclass
class Vehicle:
    # Constructs a vehicle object with a given number of tires
    # @param numberOfTires the number of tires of the vehicle
    def __init__(self, numberOfTires):
        self._numberOfTires = numberOfTires
        
    # Gets the nummber of tires on the vehicle
    # @return the number of tires
    def getNumberOfTires(self):
        return(self._numberOfTires)
    
    # Changes the number of tires on the vehicle
    # @param newValue the number of tires
    def setNumberOfTires(self, newValue):
        self._numberOfTires = newValue
    
    # Gets the description of the vehicle
    # @return a string containing the description of the vehicle
    def getDescription(self):
        return("A vehicle with " + str(self._numberOfTires) + "tires.")
    
##
# A specific type of vehicle
#

class Car(Vehicle):
    # Constructs a car object
    def __init__(self):
        # Call the superclass constructor to define its instance variable
        super().__init__(4)
        
        # This instance variable is added to the subclass
        self._plateNumber = "??????"
        
        # Sets the licence plate number of the car
        # @param newValue a string containing the number
        
        def setLicenseNumber(self, newValue):
            self._plateNumber = newValue
        
        def setLicensePlateNumber(self, newValue):
            self._plateNumber = newValue
        
        # Gets a description of the car
        # @return a string containing the description
        def getDescription(self):
            return("A car with license plate" + self._plateNumber)