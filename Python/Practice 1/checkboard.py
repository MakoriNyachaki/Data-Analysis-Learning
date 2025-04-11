# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 05:25:02 2023

@author: Lenovo
"""

for i in range(12) :
    for j in range(12) :
        if i % 2 == j % 2 :
            print(" ** ", end="")
        else :
            print(" ", end="")
    print()