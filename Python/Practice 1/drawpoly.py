# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 09:26:51 2023

@author: The_Makoris
"""

from ezgraphics import GraphicsWindow
from math import radians, cos, sin

WIN_SIZE = 400
POLY_RADIUS = 150
POLY_OFFSET = WIN_SIZE // 2 - POLY_RADIUS

def main():
    win = GraphicsWindow(WIN_SIZE, WIN_SIZE)
    canvas = win.canvas()
    canvas.setOutline("blue")
    numSides = getNumberSides()
    while numSides != 0:
        canvas.clear()
        polygon = buildRegularPolygon(POLY_OFFSET, POLY_OFFSET, numSides, POLY_RADIUS)
        drawPolygon(polygon, canvas)
        numSides = getNumberSides()


##
# Obtain from the user the number of sides for the polygon
# @return the number of sides >= 3 or 0 if the user wishes to quit
#

def getNumberSides():
    numSides = int(input("Enter number of sides must be 3 or greater: "))
    while numSides < 3 and numSides != 0:
        print("Error! The number of sides must be (>= 3) or greater")
        numSides = int(input("Enter number of sides must be 3 or greater: "))

    return(numSides)

##
#

def drawPolygon(vertexList, canvas):
    last = len(vertexList) - 1
    for i in range(last):
        start = vertexList[i]
        end = vertexList[i + 1]
        canvas.drawLine(start[0], start[1], end[0], end[1])
    start = vertexList[last]
    end = vertexList[0]
    canvas.drawLine(start[0], start[1], end[0], end[1])

##
# Computes and builds a list of vertices for aregular polygon.
# defined within a bounding square.
# @param x the x-coordinate of the upper-left corner of the bounding square
# @param y the y-coordinate of the upper-left corner of the bounding square
# @param sides the number of sides for the polygon
# @param radius the radius of regular polygon
# @return the list of vertices stored in the format [[x1, y1], ... [xn, yn]]
#

def buildRegularPolygon(x, y, sides, radius):
    xOffset = x + radius
    yOffset = y + radius

    angle = 0.0
    angleInc = radians(360 / sides)
    vertexList = []
    for i in range(sides):
        xVertex = xOffset + radius * cos(angle)
        yVertex = yOffset + radius * sin(angle)
        vertexList.append([round(xVertex), round([yVertex])])
        angle = angle + angleInc

    return(vertexList)



