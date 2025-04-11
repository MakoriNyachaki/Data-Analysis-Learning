# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:31:06 2023

@author: Lenovo

How do you simulate a coin toss with the random method?
"""

from random import randint

for i in range(2):
    # 0 for tail and 1 for head
    
    toss = randint(0, 1)
    
    if toss == 0:
        print("Tail")
    elif toss == 1:
        print("Head")
    else:
        print("Invalid toss!")

