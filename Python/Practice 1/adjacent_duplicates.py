# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 05:45:00 2023

@author: Lenovo
"""

value = int(input("Enter a value: "))
val = input("Enter another value: ")

while val != "":
    prev = value
    value = int(val)
    if value == prev:
        print('Duplicate input.')
    val = input('Enter another value:')