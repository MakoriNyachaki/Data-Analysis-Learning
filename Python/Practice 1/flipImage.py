# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:19:40 2023

@author: Lenovo
"""


from ezgraphics import GraphicsImage

filename = input("Enter the name of the image file: ")

# Load the image from the file

origImage = GraphicsImage(filename)

# Create an empty image that will contain the new flipped image

width = origImage.width()
height = origImage.height()
newImage = GraphicsImage(width, height)

# Iterate over the image and copy the pixels to the new image to
# produce the flipped image.

newRow = height - 1
for row in range(height):
    for col in range(width):
        newCol = col
        pixel = origImage.getPixel(row, col)
        newImage.setPixel(newRow, newCol, pixel)
    newRow = newRow - 1

# Save the new image with a new name
newImage.save("flipped-" + filename)
