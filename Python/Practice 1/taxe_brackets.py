# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:02:19 2023

@author: Lenovo
"""

largest = int(input('Enter a value: '))
val = input('Enter another value: ')

while val != "":
    value = int(val)
    if value > largest:
        largest = value
    val = input("Enter another value: ")