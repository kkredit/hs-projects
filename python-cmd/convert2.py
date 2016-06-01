# convert2.py
#	A program to convert Celcius temperatures to Fahrenheit.
# Kevin Kredit
import string

def main():
    print "This program converts Celcius temperatures to Fahrenheit,"
    print
    celsius = input("What is the Celsius temperature:   ")
    print
    fahrenhiet = (celsius * 1.8) + 32
    print "The temperature is", fahrenhiet, "degrees Fahrenheit."
    if fahrenhiet < 32:
        print "Bundle up! It's cold out there!"
    if fahrenhiet > 90:
        print "Don't forget the sun-tan lotion! It's hot!"

main()
    
