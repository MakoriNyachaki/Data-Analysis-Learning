# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 04:39:19 2023

@author: Lenovo
"""
NMAX = 5
XMAX = 10

##
# printing the table header
#

for n in range(0, NMAX + 1) :
    print("%10d" % n, end="")
    
print()
for n in range(0, NMAX + 1) :
    print("%10s" % "x ", end="")

print("\n", " ", "-" * 60)

##
# print table body
#

for x in range(0, XMAX + 1):
    # Print x row in the table
    for n in range(0,NMAX + 1):
        print("%10.0f" % x ** n, end="")
        
    print()
    