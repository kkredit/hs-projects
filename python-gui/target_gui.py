# exercise2.py
# A program to make an archery target
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin()

    white = Circle(Point(100,100), 100)
    white.setFill("white")
    white.draw(win)

    black = Circle(Point(100,100), 80)
    black.setFill("black")
    black.draw(win)

    blue = Circle(Point(100,100), 60)
    blue.setFill("blue")
    blue.draw(win)

    red = Circle(Point(100,100), 40)
    red.setFill("red")
    red.draw(win)

    yel = Circle(Point(100,100), 20)
    yel.setFill("yellow")
    yel.draw(win)

main()
