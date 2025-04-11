# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 05:16:10 2023

@author: The_Makoris
"""

ROWS = 8
COLUMNS = 8

table = []

    
for rows in range(ROWS):
    if rows % 2 == 0:
        table.append(0)
    elif rows % 2 != 0:
        table.append(1)

list_0 = [table] * COLUMNS
print(list_0)