# convert_gui.py
# Program to convert Celcius to Fahrenheit using a simple
#   graphical interface.
# Kevin Kredit
from graphics import *
import string

def main():
    win = GraphWin("Temperature Converter", 400,300)
    win.setCoords(0.0,0.0, 3.0,4.0)

    intro = Text(Point(1,3), "This Program gives lets you choose whether to").draw(win)
    intro2 = Text(Point(1,2), "convert F to C or C to F.").draw(win)
    win.getMouse()
    intro.undraw()
    intro2.undraw()
    optfc = Text(Point(0.25,1.5), "Fahrenheit to Celcius")
    orpcf = Text(Point(1.75,1.5), "Celcius to Fahrenheit")
    opt = win.getMouse()
    x = opt.getX()

       
    if x < 1.5:
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

        output.setText("%0.1f" % fahrenheit)
        button.setText("Quit")

        win.getMouse()
        win.close()

    if x > 1.5:
        Text(Point(1,3), "  Fahrenheit Temperature:").draw(win)
        Text(Point(1,1), "Celcius Temperature:").draw(win)
        input = Entry(Point(2,3), 5)
        input.setText("0.0")
        input.draw(win)
        output = Text(Point(2,1), "")
        output.draw(win)
        button = Text(Point(1.5,2.0), "Convert It")
        button.draw(win)
        Rectangle(Point(1.0,1.5), Point(2,2.5)).draw(win)

        win.getMouse()

        fahrenheit = eval(input.getText())
        celcius = 5.0/9.0 * (fahrenheit - 32)

        output.setText("%0.1f" % celcius)
        button.setText("Quit")

        win.getMouse()
        win.close()

main()
    
                  
