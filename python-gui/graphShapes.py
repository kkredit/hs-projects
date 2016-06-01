# Kevin Kredit
# A program to draw cool shapes on a graph. Inspired by Kelson Weaver
# graphShapes.py

from graphics import *

def main():
    numSquares = 50
    win = GraphWin('Graph Pad',600,600)
    win.setCoords(-1,-1,numSquares+1,numSquares+1)
    win.setBackground('White')

    if 0:#grid edges
        for n in range(numSquares+1):
            Point(0,n).draw(win)
        for n in range(numSquares+1):
            Point(numSquares,n).draw(win)
        for n in range(numSquares):
            Point(n+1,0).draw(win)
        for n in range(numSquares):
            Point(n+1,numSquares).draw(win)

    LB = Point(0,0)
    LM = Point(0,numSquares/2.0)
    LT = Point(0,numSquares)
    MB = Point(numSquares/2.0,0)
    MM = Point(numSquares/2.0,numSquares/2.0)
    MT = Point(numSquares/2.0,numSquares)
    RB = Point(numSquares,0)
    RM = Point(numSquares,numSquares/2.0)
    RT = Point(numSquares,numSquares)

    for line in quarterCircleBL(0,0,25,25):
        line.draw(win)
    for line in quarterCircleTL(0,25,25,50):
        line.draw(win)
    for line in quarterCircleTR(25,25,50,50):
        line.draw(win)
    for line in quarterCircleBR(25,0,50,25):
        line.draw(win)
    for line in quarterCircleBL(25,25,50,50):
        line.draw(win)
    for line in quarterCircleTL(25,0,50,25):
        line.draw(win)
    for line in quarterCircleTR(0,0,25,25):
        line.draw(win)
    for line in quarterCircleBR(0,25,25,50):
        line.draw(win)

    for line in quarterCircleBL(0,0,50,50):
        line.draw(win)
    for line in quarterCircleTL(0,0,50,50):
        line.draw(win)
    for line in quarterCircleTR(0,0,50,50):
        line.draw(win)
    for line in quarterCircleBR(0,0,50,50):
        line.draw(win)


def quarterCircleBL(startX,startY,endX,endY):#assumes square in shape
    numSquares = endX - startX
    lines = []
    for n in range(numSquares+1):
        p1 = Point(0+startX,n+startY)
        p2 = Point(numSquares-n+startX,0+startY)
        lines.append(Line(p1,p2))
    return lines

def quarterCircleBR(startX,startY,endX,endY):#assumes square in shape
    numSquares = endX - startX
    lines = []
    for n in range(numSquares+1):
        p1 = Point(numSquares+startX,n+startY)
        p2 = Point(n+startX,0+startY)
        lines.append(Line(p1,p2))
    return lines

def quarterCircleTL(startX,startY,endX,endY):#assumes square in shape
    numSquares = endX - startX
    lines = []
    for n in range(numSquares+1):
        p1 = Point(n+startX,numSquares+startY)
        p2 = Point(0+startX,n+startY)
        lines.append(Line(p1,p2))
    return lines

def quarterCircleTR(startX,startY,endX,endY):#assumes square in shape
    numSquares = endX - startX
    lines = []
    for n in range(numSquares+1):
        p1 = Point(numSquares+startX,n+startY)
        p2 = Point(numSquares-n+startX,numSquares+startY)
        lines.append(Line(p1,p2))
    return lines

main()
input()
















            
