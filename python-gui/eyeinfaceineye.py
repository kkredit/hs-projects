# smileyFace.py
#   A program to draw smiley faces.
# Kevin Kredit
from graphics import *
import random
from random import randrange

def main():
    win = GraphWin("Smiley Face", 500, 500)
    win.setCoords(0,0, 500,500)
    x = randrange(200,300)
    y = randrange(200,300)
    center = Point(x,y)
    size = randrange(100,200)
    circle, lefteye, righteye, mouth, oldeye, oldeye2, s4 = drawFace(center, size, win)
    circle.draw(win)
    lefteye.draw(win)
    righteye.draw(win)
    mouth.draw(win)
    for i in range(5):
        newcircle, newlefteye, newrighteye, newmouth, oldeye, oldeye2, s4 = drawFace(oldeye, s4, win)
        newcircle2, newlefteye2, newrighteye2, newmouth2, oldeye, oldeye2, s4 = drawFace(oldeye2, s4, win)
        newcircle.draw(win)
        newlefteye.draw(win)
        newrighteye.draw(win)
        newmouth.draw(win)
        newcircle2.draw(win)
        newlefteye2.draw(win)
        newrighteye2.draw(win)
        newmouth2.draw(win)
        
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
    oldeye = Point(rightcenterx, rightcentery)
    oldeye2 = Point(leftcenterx,leftcentery)
    return circle, lefteye, righteye, mouth, oldeye, oldeye2, s4

main()
