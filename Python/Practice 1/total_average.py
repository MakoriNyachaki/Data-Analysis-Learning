# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 05:00:05 2023

@author: Lenovo
"""

total = 0
count = 0

val = input("Enter a value: ")

while val != "":
    value = float(val)
    count += 1
    total += value
    val = input("Enter a value: ")
    
print(f'The total is {total}, the count is {count} ' +
      f'and the average is {total / count if count >  0 else 0.0}')
print(count)