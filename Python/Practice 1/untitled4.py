# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 04:24:29 2024

@author: The_Makoris
"""



def vectors_add(v, w):
    '''
    Converts lists into its corresponding vector compoent
    Adds corresponding elements in the two lists(vextors)
    '''
    return[v_i + w_i
           for v_i, w_i in zip(v, w)]


v = [1, 2, 3]
w = [3, 2, 1]
print(vectors_add(v, w))