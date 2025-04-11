# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:49:07 2023

@author: Lenovo
"""
from math import floor

def main():
    print(middle("middlerh"))
    
def digiSum(n):
    if n == 0:
        return(0)
    return(digiSum(n // 10) + n % 10)

def smallest(x, y, z):
    return(min(x, y, z))

def average(x, y, z):
    return(round(((x + y  + z) / 3), 2))

def allTheSame(x, y, z):
    return(True if x == y and y == z else False)

def allDifferent(x, y, z):
    return(True if x != y and y != z else False)

def sorted(x, y, z):
    return(True if (x <= y and y <= z) or (x >= y and y >= z) else False)

def firstDigit(n):
    for i in n:
        if i.isdigit():
            return(i)
        
def digits(x):
    count = 0
    for i in x:
        if i.isdigit():
            count += 1
    return(count)

def middle(n):
    lenx = len(n)
    mid = lenx // 2
    if lenx % 2 == 0:
        return(n[mid - 1] + n[mid])
    elif lenx % 2 == 1:
        return(n[mid])
    
main()