# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:00:08 2023

@author: The_Makoris
"""
from random import randint
random_numbers = []
num = 0

for i in range(1, 101): 
    while num < 10:
        i = randint(1, 100)
        num += 1
        random_numbers.append(i)

print(random_numbers)