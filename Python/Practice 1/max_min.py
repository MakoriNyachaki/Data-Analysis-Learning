# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:27:02 2023

@author: The_Makoris
"""

from random import randint

num = 0
random_nums = []

for i in range(1, 101):
    while num < 20:
        i = randint(1, 100)
        random_nums.append(i)
        num += 1
        
maxi = max(random_nums)
mini = min(random_nums)

print(random_nums)
print(f'The maximum value is {maxi} and the minimum value is {mini}')