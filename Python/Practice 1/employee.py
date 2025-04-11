# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:40:16 2023

@author: The_Makoris
"""
'''
The Employee class is used to declare the Employer and register an employee
in the a company
'''

class Employee:
    
    def __init__(self):
       
        self.idNum
        self.first_name
        self.middle_name
        self.last_name
        self.email
        self.name
        self.postal_address
        self.postal_code
        self.town
        self.country
        self.phone
        self.dob
        self.address
        self.country

    ##
    # employeeName takes in the first, second and last names of the employee
    # and concatenates them into one string
    # @param first_name first name
    # @param second_name other name
    # @param last_name surname
    # returns name
    #

    def employeeName(self):
        name = self.last_name + ', ' + self.first_name + ' ' + self.second_name
        return(name.upper())

    ##
    # employeeAddress takes in the contacts and the addresses of the employee
    # @param postal_address postal address of the employee
    # @param postal_code postal code
    # @param town postal town
    # @param country country of the postal code
    # returns the address of the employee
    #

    def postalAddress(self):
        address = self.postal_address + '-' + self.postal_code + ', ' + self.town + '.\n' + self.country
        return(address.upper())
    
    ##
    # createEmail takes in the first name and last name and creates an email
    # for the employee
    # @param first_name first name of the employee
    # @param last_name last name of the employee
    # return email
    #

    def createEmail(first_name, last_name):
        email = first_name + '.' + last_name + '@gmail.com'
        return(email)

    ##
    # registerEmployee registers the employee
    # returns successful on successful registration otherwise not registered
    
    def registerEmployee():
        pass
TAX = 30
NHIF = 2.75
HOUSING_LEVY = 1.5
NSSF = 1080
HOUSE_ALLOWANCE = 15
COMMUTER_ALLOWANCE = 10000
HARDSHIP_ALLOWANCE = 0

class Salary:   
  
    
    def __init__(self, idNum, salary):
        self.idNum = idNum
        self.salary = salary

    @staticmethod
    def totalDeductions():
         gross = Salary.grossSalary()
         deductions = (TAX * gross / 100) + NSSF + (NHIF * gross / 100) + (HOUSING_LEVY * gross / 100)
         return(deductions)

    @staticmethod    
    def grossSalary(self):
        gross_salry = self.salary + (HOUSE_ALLOWANCE * self.salary / 100) + COMMUTER_ALLOWANCE + HARDSHIP_ALLOWANCE 
        return(gross_salry)

   
    @staticmethod
    def netSalary():
        net_salary = Salary.grossSalary() - Salary.totalDeductions()
        return(net_salary)
    