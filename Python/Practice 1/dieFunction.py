# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 05:56:03 2023

@author: Lenovo
"""
from random import randint

## Computes the value of a toss of a single die
# @param x the first value in range
# @param y last value in range
# @ return toss value of the toss
#

def die(x:int, y:int) -> int:
    toss = randint(x, y)
    return(toss)



for i in range(10):
    first_die = die(1, 6)
    second_die = die(1, 6)
    print(f'({first_die}, {second_die})')