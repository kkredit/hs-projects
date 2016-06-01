# exercise1.py
# A program to make shapes
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(25,25), Point(75,75))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range (10):
        x = shape.clone()
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        x.move(dx,dy)
        x.draw(win)
    thing = Text(Point(100,50), "Click again to Quit")
    thing.draw(win)
    win.getMouse()
    win.close

main()
