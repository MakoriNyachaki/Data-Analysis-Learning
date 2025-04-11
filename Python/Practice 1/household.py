# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 08:15:29 2023

@author: Lenovo
"""
##
# Define constant amounts
#

MORE_THAN_THREE = 1000
MORE_THAN_TWO = 1500
REST = 2000


##
# main function to test the function
#


def main():
    print(f"Greater 30000: {householdIncome(35000, 4)}")
    print(f"Greater 20000: {householdIncome(22000, 1)}")
    print(f"Less than 20000: {householdIncome(5000, 4)}")
    print(f"Less than 20000: {householdIncome(3000, 1)}")


##
# A function used to determine the annual household income
# @param income annual income for the household
# @param children number of children in the household
#


def householdIncome(income, children):
    amount = 0
    if (income >= 30000 and income <= 40000) and children >= 3:
        amount = MORE_THAN_THREE * children
    elif (income >= 20000 and income < 30000) and children >= 2:
        amount = MORE_THAN_TWO * children
    elif income < 20000:
        amount = REST * children
    return(amount)

main()