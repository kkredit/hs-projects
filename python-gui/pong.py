# pong.py
#   A program to make a "pong" game
# Kevin Kredit
from graphics import *

def left(shape,window):
    shape.erase(window)
    center = shape.getCenter()
    px = center.getX()
    py = center.getY()
    newx = px - 7
    newx2 = px + 3
    shape = Rectangle(Point(newx,py), Point(newx2,py))
    return shape
    left()

def right(shape,window):
    shape.erase(window)
    center = shape.getCenter()
    px = center.getX()
    py = center.getY()
    newx = px - 3
    newx2 = px + 7
    paddle = shape(Point(newx,py), Point(newx2,py))
    return shape
    right()

def move(shape,window,enter):
    if enter == "d":
        right(shape,window)
        shape.draw(window)
    if enter == "a":
        left(shape,window)
        shape.draw(window)
    move()

def main():
    win = GraphWin((500,500), "Pong")
    win.setCoords(0,0, 500,500)
    ente = Entry((250,-15), 1)
    paddle = Rectangle(Point(245,15), Point(255,18))
    paddle.setFill("green")
    paddle.setOutline("black")
    paddle.draw(win)
    scorep1 = 0
    scorep2 = 0
    textscorep1 = Text((250,10), scorep1)
    textscorep2 = Text((250,490), scorep2)
    if scorep1 == 5:
        win.getMouse()
        win.close()
    if scorep2 == 5:
        win.getMouse()
        win.close()
    else:
        move(paddle,win,enter)

main()
    
    















           

                    
    
    
