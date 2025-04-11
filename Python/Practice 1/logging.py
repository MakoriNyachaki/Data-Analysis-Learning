# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 06:43:50 2025

@author: The_Makoris
"""

import dis
def sumx(x, y):
    return(x+y)

print("The sum is %d"%sumx(10, 20))
print(sumx.__code__.co_argcount)
print(sumx.__code__.co_varnames)

#print(sumx(10, 30))

dis.show_code(sumx)