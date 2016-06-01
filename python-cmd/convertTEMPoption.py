# convert_C-F.py
#	A program to convert farenheit to celcius or other way around.
# Kevin Kredit
import string
 
def main():
    print "This program converts Celcius temperatures to Fahrenheit,"
    print "or Fahrenheit to Celcius."
    print

    print "If you want to convert C to F, print 'CtoF',"
    which = raw_input("if you want to convert F to C, print 'FtoC': ")
    print

    string.lower(which)

    if which=="ctof":
        c = input("What is the Celcius temperature? ")
        f = (c * 1.8) + 32
        print "The temperature is", f, "degrees Fahrenheit."

    if which=="ftoc":
        f = input("What is the Fahrenheit temperature? ")
        c = (f - 32) / 1.8
        print "The temperature is", c, "degrees Celcius."

main()
