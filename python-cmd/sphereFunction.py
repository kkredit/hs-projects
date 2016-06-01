# geometryFunctions.py
#   A program to run geometry functions
# kevin kredit
import math
import string

def main():
    print "Would you like to find the SA or V of a sphere?"
    print
    which = raw_input("If SA, type 'SA', if V, type 'V'.    ")
    which = string.lower(which)
    print

    if which == "sa":
        r = input("What is the radius?  ")
        m = sa(r)
        print "The SA of your sphere is approxamatly:", m, "units squred."
        

    if which == "v":
        r = input("What is the radius?  ")
        n = v(r)
        print "The V of your sphere is approxamatly:", n, "units squared."

def sa(r):
    sa = 4 * r**2 * 3.14159
    return sa

def v(r):
    v = (4/3) * 3.14159 * r**3
    return v

main()

        
