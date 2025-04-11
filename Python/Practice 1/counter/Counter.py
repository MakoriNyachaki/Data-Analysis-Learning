# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:08:07 2024

@author: The_Makoris
"""

##
# This module defines the counter class
#

# Models a tally counter whose value can be incremented, viewed or reset

class Counter:
    # Gets the current value of this counter
    # @return the current value
    def getValue(self):
        return(self._value)

    # Advances the value of this counter by 1
    def click(self):
        self._value = self._value + 1

    # Resetd the value of this counter to 0
    def reset(self):
        self._value = 0