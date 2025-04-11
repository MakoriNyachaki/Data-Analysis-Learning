# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 06:39:15 2023

@author: Lenovo
"""

def main():
    print(countZeros())


# Create a list of values
def createList():
    zeros = []
    
    print("Enter values, or Q to quit:")
    userInput = input()
    
    while userInput.upper() != "Q":
        zeros.append(float(userInput))
        userInput = input()
    return(zeros)
    
# count the number of zeros in a list
def countZeros():
    count = 0
    zeros = createList()
    for i in zeros:
        if i == 0:
            count += 1
    return(f'The number of zeros in {zeros} is {count}')


main()