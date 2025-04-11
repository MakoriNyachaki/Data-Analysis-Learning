# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 05:12:39 2023

@author: The_Makoris
"""

##
# This program processes a file containing a count followed by data values
# If the file doesn't exist or the format is incorrect, you can specify another file.
#

def main():
    done = False
    while not done:
        try:
            filename = input("Please enter a filename: ")
            data = readFile(filename)
            
            # As an example for processing data, we compute the sum
            total = 0
            for value in data:
                total += value
            print(f'The sum is: {total}')
            done = True
        except IOError:
            print("Error: File not found.")
        except ValueError:
            print("Error: File contents invalid.")
        except RuntimeError as error:
            print("Error: ", str(error))

##
# Opens a file and reads a dataset
# @param filename the name of the file holding the data
# @param return a list containing the data in the file
#

def readFile(filename):
    inFile = open(filename, 'r')
    try:
        return(readData(inFile))
    finally:
        inFile.close()
        

##
# Reads a dataset
# @param inFile the input file conatining the data
# @return the data set in a list
#


def readData(inFile):
    line = inFile.readline()
    numberOfValues = int(line)  # May raise a ValueError exception
    data = []
    
    for i in range(numberOfValues):
        line = inFile.readline()
        value = int(line)   # May raise a ValueError exception
        data.append(value)
        
    # Make sure there are  no more values in the file
    line = inFile.readline()
    if line != "":
        raise RuntimeError("End of file expected.")
    
    return(data)

# Start the program
main()