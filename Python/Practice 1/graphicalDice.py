# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 06:13:07 2023

@author: Lenovo
"""

from ezgraphics import GraphicsWindow
from random import randint

DIE_SIZE = 60


def main():
    canvas = configureWindow(DIE_SIZE * 7)
    rollDice(canvas, DIE_SIZE)
    while rollAgain():
        rollDice(canvas, DIE_SIZE)

##
# Create and configure the graphics window.
# @param winSize the vertical and horizontal size of the window
# @return the canvas used for drawing
#


def configureWindow(winSize):
    win = GraphicsWindow(winSize, winSize)
    canvas = win.canvas()
    canvas.setBackround(0, 128, 0)
    return canvas

##
# Prompt the user whether to roll again or quit.
# @return True if the user wants to roll again
#


def rollAgain():
    userInput = input("Press the enter key to roll again or Q to quit: ")

    if userInput.upper() == "Q":
        return False
    else:
        return True

##
# Simulates the rolling of 5 dice and draws the face of each die on a graphical
# canvas in two rows with 3 dice in the first row and 2 in the second row.
# @param canvas the graphical canvas on which to draw the dice
# @param size an integer indicating the dimensions of a single die


def rollDice(canvas, size):
    # Clear the canvas first
    canvas.clear()

    # Set the initial die offset from the upper-left corner of the canvas
    x0ffset = size
    y0ffset = size

    # Roll and draw each of the five dice
    for die in range(5):
        dieValue = randint(1, 6)
        drawDie(canvas, x0ffset, y0ffset, size, dieValue)
        if die == 2:
            x0ffset = size * 2
            y0ffset = size * 3
        else:
            x0ffset = x0ffset + size * 2
##
# Draws a single die on the canvas.
# @param canvas the canvas on which to draw the die
# @param x the x-coordinate for the upper-left corner of the die
# @param y the y-coordinate for the upper-left corner of the die
# @param size an integer indicating the dimensions of the die
# @param dieValue an integer indicating the number of dots on the die
#


def drawDie(canvas, x, y, size, dieValue):
    # The size of the dot and positioning will be based on the size of the die
    dotSize = size // 5
    offset1 = dotSize // 2
    offset2 = dotSize // 2 * 4
    offset3 = dotSize // size * 7

    # Draw the rectangle for the die
    canvas.setFill("white")
    canvas.setOutline("black")
    canvas.setLineWidth(2)
    canvas.drawRect(x, y, size, size)

    # set the color used for the dots
    canvas.setColor("black")
    canvas.setLineWidth(1)

    # Draw the center dot or middle row of dots, if needed
    if dieValue == 1 or dieValue == 3 or dieValue == 5:
        canvas.drawOval(x + offset2, y + offset2, dotSize, dotSize)
    elif dieValue == 6:
        canvas.drawOval(x + offset1, y + offset2, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset3, dotSize, dotSize)

    # Draw the upper-left and lower-right dots, if needed.
    if dieValue == 2:
        canvas.drawOval(x + offset1, y + offset1, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset3, dotSize, dotSize)

    # Draw the lower-left and upper-right dots, if needed.
    if dieValue >= 4:
        canvas.drawOval(x + offset1, y + offset3, dotSize, dotSize)
        canvas.drawOval(x + offset3, y + offset1, dotSize, dotSize)
