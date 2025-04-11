# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:36:21 2023

@author: Lenovo
"""

scores = [20, 40, 60, 40, 40]

if scores != []:
    avg = sum(scores) / len(scores)
    print(f"The average of the {scores} list is {avg}")
else:
    print("An empty list!")

