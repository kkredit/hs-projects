# Koch Snowflake
#     A program to draw a Koch Snowflake starting with one face
# Kevin Kredit
# 6/29/10

from graphics import *

def main():
    lines = snowflake([Line(Point(0,0),Point(1,0))],1,
                      input('How many iterations? '))
    win = GraphWin('Koch Snowflake',800,800)
    win.setCoords(-.05,-.05,1.05,1.05)
    for line in lines:
        line.draw(win)

def snowflake(lines,down,togo):
    for line in lines:
        p1,p2 = line.getP1(),line.getP2()
        p1x,p1y,p2x,p2y = p1.getX(),p1.getY(),p2.getX(),p2.getY()
        newlines = [Line(p1,Point(p1x+(p2x-p1x)/3,p1y+(p2y-p1y)/3))]
        newlines.append(Line(Point(p1x+2*(p2x-p1x)/3,p1y+2*(p2y-p1y)/3),p2))
    if togo > down:
        return snowflake(newlines,down+1,togo)
    else:
        return newlines
        
main()
