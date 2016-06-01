# futvalGraph.py
#   A program to find the interest gained on an investment in ten years
#   with the information to be displayed on a graph
# Kevin Kredit
import graphics
from graphics import *

def main():
    print 'A program to find the interest gained on an investment in ten years'
    print 'with the information to be displayed on a graph.'
    print
    invest = input('What was the initial investment?    ')
    apr = input('What is the annual interest rate?  ')
    print
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    height = invest * 0.2
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    for year in range(1,11):
        invest = invest * (1 + apr)
        xll = year * 25 + 40
        height = invest * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll+25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    raw_input("Press <Enter> to quit")

    win.close()

main()
