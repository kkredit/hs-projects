# fibograph.py
#   A program to graph the numbers of Fibonacci
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin("Fibonacci Graph", 390,390)
    win.setCoords(0,0, 385,385)
    # Text
    bottom = Text(Point(150,5), "Term in Fibonacci Sequence")
    bottom.setSize(10)
    bottom.draw(win)
    side = Text(Point(30,200), "Number")
    side.setSize(10)
    side.draw(win)
    bottom1 = Text(Point(47,12), "1")
    bottom1.setSize(5)
    bottom1.draw(win)
    bottom2 = Text(Point(65,12), "2")
    bottom2.setSize(5)
    bottom2.draw(win)
    bottom3 = Text(Point(83,12), "3")
    bottom3.setSize(5)
    bottom3.draw(win)
    bottom4 = Text(Point(101,12), "4")
    bottom4.setSize(5)
    bottom4.draw(win)
    bottom5 = Text(Point(119,12), "5")
    bottom5.setSize(5)
    bottom5.draw(win)
    bottom6 = Text(Point(137,12), "6")
    bottom6.setSize(5)
    bottom6.draw(win)
    bottom7 = Text(Point(155,12), "7")
    bottom7.setSize(5)
    bottom7.draw(win)
    bottom8 = Text(Point(173,12), "8")
    bottom8.setSize(5)
    bottom8.draw(win)
    bottom9 = Text(Point(191,12), "9")
    bottom9.setSize(5)
    bottom9.draw(win)
    bottom10 = Text(Point(209,12), "10")
    bottom10.setSize(5)
    bottom10.draw(win)
    bottom11 = Text(Point(227,12), "11")
    bottom11.setSize(5)
    bottom11.draw(win)
    bottom12 = Text(Point(245,12), "12")
    bottom12.setSize(5)
    bottom12.draw(win)
    bottom13 = Text(Point(263,12), "13")
    bottom13.setSize(5)
    bottom13.draw(win)
    bottom14 = Text(Point(281,12), "14")
    bottom14.setSize(5)
    bottom14.draw(win)  
    # Calculations
    x = 1
    n = 0
    m = 1
    for i in range (14):
        a = n + x
        x = n
        n = a
        bx = (m * 18) + 20
        by = a + 17
        bf = bx + 18
        bar = Rectangle(Point(bx,17), Point(bf,by)).draw(win)
        m = m + 1

    win.getMouse()
    win.close

main()
         
       
