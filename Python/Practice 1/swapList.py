# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 20:28:32 2023

@author: The_Makoris
"""

##
# This program implements an algorithm that swaps the first and second halves of a lis
#

def main():
    values = [9, 13, 21, 4, 11, 7, 1, 3, 4, 90]
    i = 0
    j = len(values) // 2
    while i < len(values) // 2:
        swap(values, i, j)
        i = i + 1
        j = j + 1
    print(values)

##
# Swaps the elemnts of a list at given positions
# @param a the list
# @param i the first position
# @param j the second position
#

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

# Start the program
main()