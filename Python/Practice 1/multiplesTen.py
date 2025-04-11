# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 18:52:08 2023

@author: Lenovo
"""

n = int(input("Enter the value of n: "))

count = 0

for i in range(0, n):
    if i % 10 == 0:
        print(n)
        count += 1
    n = n - 1


print(f' \nCount: {count}')
