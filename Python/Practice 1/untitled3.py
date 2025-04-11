# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:43:13 2024

@author: The_Makoris
"""

grades = [54.0, 63.0, 66.0, 23.0, 13.0]

newGrade = []

for score in grades:
    if score > 83 and score <= 100:
        print("A")
    elif score <= 83 and score > 74:
        print("A-")
    elif score <= 74 and score > 66:
        print("B+")
    elif score <= 66 and score > 58:
        print("B")
    elif score <= 58 and score > 51:
        print("B-")
    elif score <= 51 and score > 44:
        print("C+")
    elif score <= 44 and score > 37:
        print("C")
    elif score <= 37 and score > 30:
        print("C-")
    elif score <= 30 and score > 24:
        print("D+")
    elif score <= 24 and score > 19:
        print("D")
    elif score <= 19 and score > 15:
        print("D-")
    elif score <= 15 and score >= 0:
        print("E")
    else:
        print("F")
    newGrade.append(score)
    
print(newGrade)