# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:34:08 2023

@author: The_Makoris
"""

from random import randint

num = 0
random_nums = []
prod = 1
negative = 0

for i in range(1, 101):
    while num < 15:
        # Generating 15 random numbers between -100 and 100
        i = randint(-100, 100)
        # Appending the generated random number into the list
        random_nums.append(i)
        # Terminator of the while loop
        num += 1

# Printing all numbers in the list on the same line separated by a space
for i in random_nums:
    print(i, end = " " )

# Print a new line
print()

# Finding the product of all numbers in the list
for i in random_nums:
    prod *= i

# Finding how many numbers are negative integers in the list
for i in random_nums:
    if i < 0:
        negative += 1

# Print all the results

if negative > 0:
    print(f'Negatives in the list are {negative}')
else:
    print("All numbers in the list are positive integers.")

print(f'The product is :{prod}')