# dice.py
#   A program to draw dice
# Kevin Kredit

from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0.0,0.0, 11,11)

    die1 = Rectangle(Point(1,1), Point(2,2))
    die1.setOutline("black")
    die1.setFill("white")
    die1.draw(win)

    die2 = Rectangle(Point(3,1), Point(4,2))
    die2.setOutline("black")
    die2.setFill("white")
    die2.draw(win)

    die3 = Rectangle(Point(5,1), Point(6,2))
    die3.setOutline("black")
    die3.setFill("white")
    die3.draw(win)
    
    die4 = Rectangle(Point(7,1), Point(8,2))
    die4.setOutline("black")
    die4.setFill("white")
    die4.draw(win)

    die5 = Rectangle(Point(9,1), Point(10,2))
    die5.setOutline("black")
    die5.setFill("white")
    die5.draw(win)

    dot1 = Circle(Point(1.5,1.5), 0.15)
    dot1.setFill("black")
    dot1.draw(win)

    dot21 = Circle(Point(3.25,1.75), 0.15)
    dot21.setFill("black")
    dot21.draw(win)
    dot22 = Circle(Point(3.75,1.25), 0.15)
    dot22.setFill("black")
    dot22.draw(win)

    dot31 = Circle(Point(5.25,1.75), 0.15)
    dot31.setFill("black")
    dot31.draw(win)
    dot32 = Circle(Point(5.5,1.5), 0.15)
    dot32.setFill("black")
    dot32.draw(win)
    dot33 = Circle(Point(5.75,1.25), 0.15)
    dot33.setFill("black")
    dot33.draw(win)

    dot41 = Circle(Point(7.25,1.75), 0.15)
    dot41.setFill("black")
    dot41.draw(win)
    dot42 = Circle(Point(7.75,1.75), 0.15)
    dot42.setFill("black")
    dot42.draw(win)
    dot43 = Circle(Point(7.25,1.25), 0.15)
    dot43.setFill("black")
    dot43.draw(win)
    dot44 = Circle(Point(7.75,1.25), 0.15)
    dot44.setFill("black")
    dot44.draw(win)

    dot51 = Circle(Point(9.25,1.75), 0.15)
    dot51.setFill("black")
    dot51.draw(win)
    dot52 = Circle(Point(9.75,1.75), 0.15)
    dot52.setFill("black")
    dot52.draw(win)
    dot53 = Circle(Point(9.25,1.25), 0.15)
    dot53.setFill("black")
    dot53.draw(win)
    dot54 = Circle(Point(9.75,1.25), 0.15)
    dot54.setFill("black")
    dot54.draw(win)
    dot55 = Circle(Point(9.5,1.5), 0.15)
    dot55.setFill("black")
    dot55.draw(win)

main()


    
    








    
    
    
