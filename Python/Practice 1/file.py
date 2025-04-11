# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 15:55:30 2023

@author: The_Makoris
"""

##
# This program reads a file containing numbers and writes the number to
# another file, lined up in a column and followed by their and average
#

# Prompt the user for the name of the input and output files.

inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")

# Open the input and output files
infile = open(inputFileName, "r")
outfile = open(outputFileName, "w")

# Read the input and write the output
total = 0.0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write("%15.2f\n" % value)
    total = total + value
    count = count + 1
    line = infile.readline()
    
# Output the total and average

outfile.write("15s\n" % "------------")
outfile.write("Total: %8.2f\n" % total)

avg = total / count
outfile.write("Average: %6.2f\n" % avg)

# Close the files
infile.close()
outfile.close()