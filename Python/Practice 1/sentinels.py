# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:29:14 2023

@author: Lenovo
"""

count = 0
total = 0.0

salary = 0.0

while salary >= 0.0:
    salary = float(input('Enter a salary or -1 to finish: '))
    if salary >= 0.0:
        total += salary
        count += 1
    
print(f'The average is {total/count if count > 0 else "No data entered"}')