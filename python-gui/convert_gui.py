# convert_gui.py
# Program to convert Celcius to Fahrenheit using a simple
#   graphical interface.
# Kevin Kredit
import graphics
from graphics import *

def main():
    win = GraphWin("Celcius Converter", 300, 200)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    Text(Point(1,3), "  Celcius Temperature:").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    input = Entry(Point(2,3), 5)
    input.setText("0.0")
    input.draw(win)
    output = Text(Point(2,1), "")
    output.draw(win)
    button = Text(Point(1.5,2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1.0,1.5), Point(2,2.5)).draw(win)

    win.getMouse()

    celcius = eval(input.getText())
    fahrenheit = 9.0/5.0 * celcius + 32

    output.setText("%0.1f " % fahrenheit)
    button.setText("Quit")

    win.getMouse()
    win.close()

main()
    
                  
