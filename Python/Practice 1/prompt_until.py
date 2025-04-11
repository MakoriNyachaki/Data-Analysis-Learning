# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 05:22:30 2023

@author: Lenovo
"""

valid = False
while not valid :
    value = int(input("Please enter a positive value < 100: "))
    if value > 0 and value < 100 :
            valid = True
    else :
        print("Invalid input.")