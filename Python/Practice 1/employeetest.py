# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 08:16:26 2023

@author: The_Makoris
"""
from employee import Employee
fname = str(input("First Name: "))
mname = str(input("Middle Name: "))
lname = str(input("Last Name: "))

pAddress = str(input("Postal Address: "))
pCode = str(input("Postal Code: "))
town = str(input("Town: "))
country = str(input("Country: "))



id_num = int(input("ID Number: "))
name = Employee.employeeName(1)
address = Employee.postalAddress(1)
phone = str(input("Phone Number: "))
email = Employee.createEmail(fname, lname)
dob = input("DOB: ")



emp = Employee(id_num, name, email, phone, address, country.upper(), dob)


print(f'\n\nID: {emp.idNum}\nName: {emp.name}\nEmail: {emp.email}\nPhone: {emp.phone}\nDOB: {emp.dob}\nAddress: {emp.address}\nCountry: {emp.country}')