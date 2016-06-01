# futvalGraph2.py
#   A program to find the interest gained on an investment in ten years
#   with the information to be displayed on a graph
# Kevin Kredit
import graphics
from graphics import *

def drawBar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    print 'A program to find the interest gained on an investment in ten years'
    print 'with the information to be displayed on a graph.'
    print
    invest = input('What was the initial investment?    ')
    apr = input('What is the annual interest rate?  ')
    print
    
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75,-200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

    drawBar(win, 0, invest)
    for year in range (1, 11):
        invest = invest * (1+apr)
        drawBar(win, year, invest)
    win.getMouse()
    win.close()
main()
