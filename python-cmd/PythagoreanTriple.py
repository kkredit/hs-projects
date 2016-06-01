# Pythagorean Triple.py
#   A program to find Pythagorean triples
# Kevin Kredit

import string
import math
from math import *


def main():
    # user input
    print "\nThis program finds Pythagorean triples (a^2 + b^2 = c^2)."
    
    sides = input("\nHow many sides do you know? (1 or 2)    ")

    # 1 side
    if sides == 1:
        side1, x = input("\nWhat is the length of the side?         "), 1
        
        # side A
        printed = 0
        print "\nPossible solutions assuming the input side was side (A) are:\n"
        for i in range(9999):
            b = (((side1**2.0) / x) / 2) - ((1.0 / 2.0) * x)
            c = (((side1**2.0) / x) / 2) + ((1.0 / 2.0) * x)
            b1, c1 = int(b), int(c)
            if b1 == b and c1 == c and side1 <= b1 and b1 < c1:
                print "     ",side1,",",b1,",",c1
                printed = printed + 1
            x = x + 1
        if printed == 0:
            print "There are no solutions for side (A)."

        # side B
        printed, c = 0, side1 + (x / 2.0)
        print "\nPossible solutions assuming the input side was side (B) are:\n"
        for i in range(9999):
            aa = ((2 * side1) + (x / 2.0))*(x / 2.0)
            a, c = math.sqrt(aa), side1 + (x / 2.0)
            a1, c1 = int(a), int(c)
            if a1 == a and c1 == c and a1 <= side1 and side1 < c1:
                print "     ",a1,",",side1,",",c1
                printed = printed + 1
            x = x + 1
        if printed == 0:
            print "There are no solutions for side (B)."

        # side C
        printed, iso, iso2 = 0, side1 / math.sqrt(2), side1 * math.sqrt(2)
        a = int(iso)
        print "\nPossible solutions assuming the input side was side (C) are:\n"
        print "For an Isosceles triangle, the solution is:"
        print iso,",",iso,",",side1
        print side1,",",side1,",",iso2,"\n"
        for i in range(9999):
            b = math.sqrt(side1**2 - a**2)
            b1 = int(b)
            if b1 == b and a1 <= b1 and b1 < side1:
                print "     ",a1,",",b1,",",side1
                printed = printed + 1
            a = a - 1
        if printed == 0:
            print "There are no solutions for side (C)."

    # 2 sides    
    elif sides == 2:
        side1 = input("\nWhat is the length of the first side?   ")
        side2 = input("What is the length of the second side?  ")

        if side1 >= side2:
            z, side1 = side1, side2
            side2 = z

        # sides AB
        c, printed = math.sqrt(side1**2 + side2**2), 0
        if side1 <= side2 and side2 < c:
            print "\nAssuming the input sides were side (A)&(B), your solution is:"
            print "     ",side1,",",side2,",",c
            printed = printed + 1
        if printed == 0:
            print "\nThere are no solutions for sides (A)&(B)."

        # sides AC
        b, printed = math.sqrt(side2**2 - side1**2), 0
        if side1 <= b and b < side2:
            print "\nAssuming the input sides were side (A)&(C), your solution is:"
            print "     ",side1,",",b,",",side2
            printed = printed + 1
        if printed == 0:
            print "\nThere are no solutions for sides (A)&(C)."

        # sides BC
        a, printed = math.sqrt(side2**2 - side1**2), 0
        if a < side1 and side1 < side2:
            print "\nAssuming the input sides were side (B)&(C), your solution is:"
            print "     ",a,",",side1,",",side2
            printed = printed + 1
        if printed == 0:
            print "\nThere are no solutions for sides (B)&(C)."
        
    else:
        print "\nYou are an imbecile.  What you said makes no sense."
        
main()


