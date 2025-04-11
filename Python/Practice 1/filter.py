# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 06:17:02 2023

@author: The_Makoris
"""

##
# This program reads data from a csv file that contains movie information,
# filters out unwanted data, and produces a new csv
#

from csv import reader, writer

# Open the two csv files
infile = open("movies.csv")
csvReader = reader(infile)

outfile = open("filtered.csv", "w")
csvWriter = writer(outfile)

# Add the list of column headers to the csv file
headers = ["Name", "Year", "Actors"]
csvWriter.writerow(headers)

# Skip the row of column header in the column header
next(csvReader)

# filter the rows of data
for row in csvReader:
    year = int(row[1])
    if year >= 1990 and year <= 1999:
        newRow = [row[0], row[1], row[2]]
        csvWriter.writerow(newRow)


infile.close()
outfile.close()