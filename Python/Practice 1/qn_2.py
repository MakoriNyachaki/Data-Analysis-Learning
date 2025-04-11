# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:18:34 2023

@author: The_Makoris
"""

a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0]


total = 0
for i in range(10):
    total = total + a[i]
    
print(total)

# b
total = 0

for i in range(0, 10, 2):
    total = total + a[i]
    
print(total)

# c
total = 0

for i in range(1, 10, 2):
    total = total + a[i]
    
print(total)

# # d
# total = 0

# for i in range(2, 11):
#     total = total + a[i]
    
# print(total)

# e
total = 0
i = 1
while i < 10 :
    total = total + a[i]
    i = 2 * i
print(total)

# f
total = 0

for i in range(9, -1, -1):
    total = total + a[i]
    
print(total)

# g
total = 0

for i in range(9, -1, -2):
    total = total + a[i]
    
print(total)

# h
total = 0

for i in range(0, 10):
    total =  a[i] -total
    
print(total)