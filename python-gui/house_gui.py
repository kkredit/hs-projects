# house.py
#   A program to draw a house
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin("House", 350,350)
    win.setCoords(0.0,0.0, 75.0,75.0)
    overallt = Text(Point(35,70), "Draw a House").draw(win)
    
    mainm = win.getMouse()
    mainmx = mainm.getX()
    mainmy = mainm.getY()
    mainm2 = win.getMouse()
    mainm2x = mainm2.getX()
    mainm2y = mainm2.getY()
    main = Rectangle(Point(mainmx,mainmy), Point(mainm2x,mainm2y))
    main.setFill("brown")
    main.setOutline("black")
    main.draw(win)
    
    b = win.getMouse()
    b2 = b.getY()
    b3 = b.getX()
    v = mainm.getX()
    v2 = mainm2.getX()
    b4 = b3 - ((v2-v)/10)
    b5 = b3 + ((v2-v)/10)
    b6 = mainm.getY()
    door = Rectangle(Point(b4,b6), Point(b5,b2))
    door.setFill("white")
    door.setOutline("black")
    door.draw(win)
    
    r = (v2 - v)/10
    wind = Rectangle(Point(0.0,0.0), Point(r,r))
    p = win.getMouse()
    wind2 = wind.clone()
    c = wind.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    wind2.move(dx,dy)
    wind2.setFill("white")
    wind2.setOutline("black")
    wind2.draw(win)
    
    f = win.getMouse()
    fx = f.getX()
    fy = f.getY()
    roof = Polygon(Point(mainmx,mainm2y), Point(mainm2x,mainm2y), Point(fx,fy))
    roof.setFill("black")
    roof.setOutline("black")
    roof.draw(win)

    win.getMouse()
    win.close()

main()


    
    
            
