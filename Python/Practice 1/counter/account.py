# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:32:22 2024

@author: The_Makoris
"""

##
# This module defines the cash register
# A simulated cash register that tracks the item count the total amount
#

class CashRegister:
    # Constructs a cash register with cleared item count and total
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0
    # Adds an item to this cash register
    # @param price the price of this item
    def addItems(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price
        
    # Gets the price of all items in the current sale
    # @return the total price
    def getTotal(self):
        return(self._totalPrice)
    
    # Gets the number of items in the current sale
    # @return the item count
    def getCount(self):
        return(self._itemCount)
    
    # Clears the item count and the total
    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0