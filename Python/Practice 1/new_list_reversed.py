# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:37:05 2023

@author: The_Makoris
"""
list_0 = []
list_1 = []

for i in range(10):
    num = int(input("Enter a number: "))
    list_0.append(num)

print(list_0)

##
# Reverse the list created(list_0)
# First find the lenght of the list 0 which will also be the length of the
# reversed list
#
list_len = len(list_0)

# Negative index indicating the last index in the previous list
# The value in the index is the first element in the reversed list

index = -1

while index >= -list_len:
    # get the value at the index position
    value = list_0[index]
    # append value to list_1
    list_1.append(value)
    # Decrement index to move to the next index position and terminate the loop
    index -= 1

if len(list_0) == len(list_1):
    print(list_1)
else:
    print("The length of the reversed list is not equal to the length of the original list.")