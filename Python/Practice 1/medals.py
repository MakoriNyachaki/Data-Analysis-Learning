# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 04:58:09 2023

@author: The_Makoris
"""

##
# This program prints a table of medal winner counts with row totals
#

MEDALS = 3
COUNTRIES = 8

# Create a list of countries

countries = ["Canada",
             "Italy",
             "Germany",
             "Japan",
             "Kazakhtan",
             "Russia",
             "South Korea",
             "United States"]

# Create a table of medal counts

counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
    ]

# Print the table header
print("       Country     Gold    Silver  Bronze  Total")

# Print countries, counts and row totals

for i in range(COUNTRIES):
    print("%15s" % countries[i], end="")
    
    # Print each row element and update the row total
    total = 0
    for j in range(MEDALS):
        print("%8d" % counts[i][j], end="")
        total = total + counts[i][j]
        
    # Display the row total and print a new line
    print("%8d" % total)