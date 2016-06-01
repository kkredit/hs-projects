# triangle2.py
# Kevin Kredit
import math
import graphics
from graphics import *

def square(x):
    return x * x

def dist(p1,p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on the three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    perim = dist(p1,p2) + dist(p2,p3) + dist(p3,p1)
    message.setText("The perimeter is: %0.2f" % perim)

    win.getMouse()
    win.close()

main()
