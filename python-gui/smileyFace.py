# smileyFace.py
#   A program to draw smiley faces.
# Kevin Kredit
from graphics import *
import random
from random import randrange

def main():
    win = GraphWin("Smiley Face", 500, 500)
    win.setCoords(0,0, 500,500)
    for i in range(1000):
        x = randrange(15,485)
        y = randrange(15,485)
        center = Point(x,y)
        size = randrange(5,25)
        circle, lefteye, righteye, mouth = drawFace(center, size, win)
        circle.draw(win)
        lefteye.draw(win)
        righteye.draw(win)
        mouth.draw(win)
    win.getMouse()
    win.close()

def drawFace(center, size, win):
    cy = center.getY()
    cx = center.getX()
    circle = Circle(Point(cx,cy), size)
    circle.setFill("yellow")
    circle.setOutline("black")
    leftcentery = cy + (size/2)
    leftcenterx = cx - (size/2)
    rightcenterx = cx + (size/2)
    rightcentery = cy + (size/2)
    s4 = size / 4
    bottompointx = cx - (size/2)
    bottompointy = cy - (size/2)
    upperpx = cx + (size/2)
    upperpy = cy - (size/4)
    lefteye = Circle(Point(leftcenterx,leftcentery), s4)
    righteye = Circle(Point(rightcenterx, rightcentery), s4)
    mouth = Rectangle(Point(bottompointx,bottompointy), Point(upperpx,upperpy))
    lefteye.setFill("black")
    righteye.setFill("black")
    mouth.setFill("black")
    return circle, lefteye, righteye, mouth

for i in range(50):
    main()
