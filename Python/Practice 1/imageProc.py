# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 04:30:27 2023

@author: The_Makoris

This program processes a digital image by creating a negative of a BMP image.
"""
from io import SEEK_CUR
from sys import exit

def main():
    filename = input("Please enter a  filename: ")
    
    # Open as a binary file for reading and writing
    imgFile = open(filename, "rb+")
    
    # Extract the image information
    fileSize = readInt(imgFile, 2)
    start = readInt(imgFile, 10)
    width = readInt(imgFile, 18)
    height = readInt(imgFile, 22)
    
    # Scan line must occupy multiples of 4 bytes
    scanlineSize = width * 3
    
    if scanlineSize % 4 == 0:
        padding = 0
    else:
        padding = 4 - scanlineSize % 4
        
    # Make sure this is a valid image
    if fileSize != (start + (scanlineSize + padding) * height):
        exit("Not a 24-bit true color image file.")
    
    # Move the first pixel in the image
    imgFile.seek(start)
    
    # Process the individual pixels
    for row in range(height):
        for col in range(width):
            processPixel(imgFile)
            
            # Skip the patdding at the end
            imgFile.seek(padding, SEEK_CUR)
    imgFile.close()

##
# Process an individual pixel
# @param imgFile the binary file conatining the BMP image
#

def processPixel(imgFile):
    # Read the pixel as an individual bytes
    theBytes = imgFile.read(3)
    blue = theBytes[0]
    green  = theBytes[1]
    red = theBytes[2]
    
    # Process the pixel
    newBlue = 255 - blue
    newGreen = 255 - green
    newRed = 255 - red
    
    # Write the pixel
    imgFile.seek(-3, SEEK_CUR) # Go back 3 bytes to the start of the pixel
    imgFile.write(bytes([newBlue, newGreen, newRed]))

##
# Get an integer from a binary file
# @param imgFile the file
# @param offset the offset at which to read the integer
# @return the integer starting at the given offset
#

def readInt(imgFile, offset):
    # Move the file pointer to a given byte within the file
    imgFile.seek(offset)
    
    # Read the 4 individual bytes and build an integer
    theBytes = imgFile.read(4)
    result = 0
    base = 1
    
    for i in range(4):
        result = result + theBytes[i] * base
        base = base * 256
        
    return(result)

# Start the program
main()

