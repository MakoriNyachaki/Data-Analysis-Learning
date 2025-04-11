# -*- coding: utf-8 -*-
"""
Created on Mon May 20 09:37:01 2024

@author: The_Makoris
"""
from add import add, sumList, countList, countElements

def main():
    lst = [10, 20, 30, 40]
    print(f'The Expected sum is: {add(10, 20, 30, 40)}')
    print(f'The sum of the list is: {sumList(lst)}\n')
    
    elements = ['Diamond', 'Gold', 'Silver', 'Potassium', 'Sodium']
    print(f'The list has {countList(elements)} elements')
    
    dic = {
        1 : "Hello",
        2 : "How are you"
        }
    
main()
