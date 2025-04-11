# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:30:03 2023

@author: Lenovo
"""

from ezgraphics import GraphicsWindow, GraphicsImage

# Define the gap and number of pictures

GAP = 10
NUM_PICTURES = 20
MAX_WIDTH = 720

pic = GraphicsImage("icon1.png")
win = GraphicsWindow(MAX_WIDTH, 700)
canvas = win.canvas()
canvas.drawImage(0, 0, pic)

x = 0
y = 0
max_Y = 0

for i in range(2, NUM_PICTURES + 1):
    max_Y = max(max_Y, pic.height())
    previous = pic
    filename = "icon%d.png" % i
    pic = GraphicsImage(filename)
    x = x + previous.width() + GAP

    if x + pic.width() < MAX_WIDTH:
        canvas.drawImage(x, y, pic)
    else:
        x = 0
        y = y + max_Y + GAP
        canvas.drawImage(x, y, pic)
win.wait()
