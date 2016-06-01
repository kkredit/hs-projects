# c-curve.py
# a program to draw c-curves without using (a+bi)^c
# Kevin Kredit
# 8/14/2012

from graphics import *
from math import *

def main():
    win = GraphWin('C-curve',600,600)
    win.setBackground('black')
    win.setCoords(-300,-300,300,300)

    xpos,ypos = 0,0
    xpos,ypos = drawline(xpos,ypos,0,win) #init first line

    direction = 0
    degree = 0
    turns = [3]
    
    while True:

        for turn in turns:

            direction += turn
            print turn,
            xpos,ypos = drawline(xpos,ypos,direction,win)

        turns *= 2
        turns[0] = degree%4
        degree += 1

        #if degree == 10: break #manually determine the degree
            


def drawline(xpos,ypos,direction,win):
    
    startpoint = Point(xpos,ypos)

    #xpos += [0,1,0,-.99][direction%4]*5 #last multiplyer defines scale
    #ypos += [1,0,-.99,0][direction%4]*5

    xpos += sin(direction*.5*pi)*5 #last multiplyer defines scale
    ypos += cos(direction*.5*pi)*5

    line = Line(startpoint,Point(xpos,ypos))
    line.setFill('green')
    line.draw(win)

    return xpos,ypos


main()




