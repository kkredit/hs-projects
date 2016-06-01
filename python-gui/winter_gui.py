# winter.py
#   A program to make a winter scene
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0.0,0.0, 100.0, 100.0)

    ground = Rectangle(Point(0.0,0.0), Point(100.0,50.0))
    ground.setFill("grey")
    ground.draw(win)

    sky = Rectangle(Point(0.0,100.0), Point(100.0, 100.0))
    sky.setFill("blue")
    sky.draw(win)

    b1 = Circle(Point(25,25), 20)
    b1.setFill("white")
    b1.setOutline("black")
    b1.draw(win)

    b2 = Circle(Point(25,45), 18)
    b2.setFill("white")
    b2.setOutline("black")
    b2.draw(win)

    b3 = Circle(Point(25,65), 16)
    b3.setFill("white")
    b3.setOutline("black")
    b3.draw(win)

    trunk = Rectangle(Point(70,25), Point(80,35))
    trunk.setFill("brown")
    trunk.draw(win)

    t1 = Polygon(Point(50,35), Point(100,35), Point(75,55))
    t1.setFill("green")
    t1.setOutline("black")
    t1.draw(win)

    t2 = Polygon(Point(55,45), Point(95,45), Point(75,65))
    t2.setFill("green")
    t2.setOutline("black")
    t2.draw(win)

    t3 = Polygon(Point(60,55), Point(90,55), Point(75,75))
    t3.setFill("green")
    t3.setOutline("black")
    t3.draw(win)

    t4 = Polygon(Point(65,65), Point(85,65), Point(75,85))
    t4.setFill("green")
    t4.setOutline("black")
    t4.draw(win)

    t5 = Polygon(Point(70,75), Point(80,75), Point(75,95))
    t5.setFill("green")
    t5.setOutline("black")
    t5.draw(win)

main()
    
    
                       
