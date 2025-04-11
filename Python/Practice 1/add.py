# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:15:17 2024

@author: The_Makoris
"""
TOT = 0
COUNT = 0

def add(*args):
    tot = TOT
    for i in args:
        tot += i
    
    return(tot)

def sumList(lst):
    tot = TOT
    for num in lst:
        tot += num
    
    return(tot)

def countElements(**kwargs):
    count = COUNT
    for kwarg in kwargs:
        count += 1

    return(kwargs)

def countList(lst):
    count = COUNT
    for element in lst:
        count += 1
        
    return(count)
