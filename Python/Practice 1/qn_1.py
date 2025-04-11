# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:38:16 2023

@author: The_Makoris
"""
FACTOR = 2


list_0 = []

for i in range(1, 11):
    list_0.append(i)
    
print(list_0)

list_1 = []

for j in range(0, 21):
    if j % 2 == 0:
        list_1.append(j)
        
print(list_1)

list_2 = []

for m in range(10):
    list_2.append(m * 0)
    
print(list_2)

list_3 = []

for n in range(10):
    if n % 2 == 0:
        list_3.append(0)
    elif n % 2 != 0:
        list_3.append(1)

print(list_3)

list_4 = []

for i in range(1, 5):
    list_4.append(i)
list_4 = list_4 * FACTOR

print(list_4)