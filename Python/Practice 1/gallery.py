# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:46:47 2023

@author: Lenovo
"""

from ezgraphics import GraphicsWindow, GraphicsImage

GAP = 10

pic = GraphicsImage("icon95.png")

win = GraphicsWindow(800, 600)
canvas = win.canvas()
canvas.drawImage(0, 0, pic)
pic2 = GraphicsImage("icon98.png")
x = pic.width() + GAP
canvas.drawImage(x, 0, pic2)
x = x + pic2.width() + GAP
pic3 = GraphicsImage("icon97.gif")
canvas.drawImage(x, 0, pic3)
win.wait()
