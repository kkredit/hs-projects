# Pythagorean Triple2.py
#   A program to find Pythagorean triples
# Kevin Kredit

import string
import math


def main():
    # user input
    print "\nThis program finds Pythagorean triples (a^2 + b^2 = c^2)."
    #print "   If you know two sides, simply input the lengths. If you know"
    #print "   only one side, input the length and press Enter twice."
    
    side1 = input("\nWhat is the length of the first side?     ")    
    side2 = raw_input("What is the length of the second side?    ")

    # determine 1 side or 2 sides
    if side2 == "":
        sides = 1

    else:
        side2, sides = float(side2), 2
        
    # 1 side
    if sides == 1:
        printed, x = 0, 1
        
        # side A
        #print "Possible solutions assuming the input side was side (A) are:\n"
        print "\n(A)\n"
        for i in range(9999):
            b = (((side1**2.0) / x) / 2) - ((1.0 / 2.0) * x)
            c = (((side1**2.0) / x) / 2) + ((1.0 / 2.0) * x)
            b1, c1 = int(b), int(c)
            if b1 == b and c1 == c and side1 <= b1 and b1 < c1:
                print side1,",",b1,",",c1
                printed = printed + 1
            x = x + 1
        if printed == 0:
            #print "\nThere are no solutions for side (A)."
            print "\nNo solutions: (A)."
            
        # side B
        printed, c = 0, side1 + (x / 2.0)
        #print "\nPossible solutions assuming the input side was side (B) are:\n"
        print "\n(B)\n"
        for i in range(9999):
            aa = ((2 * side1) + (x / 2.0))*(x / 2.0)
            a, c = math.sqrt(aa), side1 + (x / 2.0)
            a1, c1 = int(a), int(c)
            if a1 == a and c1 == c and a1 <= side1 and side1 < c1:
                print a1,",",side1,",",c1
                printed = printed + 1
            x = x + 1
        if printed == 0:
            #print "There are no solutions for side (B)."
            print "No solutions: (B)."

        # side C
        printed, iso, iso2 = 0, side1 / math.sqrt(2), side1 * math.sqrt(2)
        a = int(iso)
        #print "\nPossible solutions assuming the input side was side (C) are:\n"
        print "\nIsosceles triangle:\n"        
        print iso,",", iso,",",side1,"\n  -or-\n",side1,",",side1,",",iso2
        print "\n(C)\n"
        for i in range(9999):
            b = math.sqrt(side1**2 - a**2)
            b1 = int(b)
            if b1 == b and a1 <= b1 and b1 < side:
                print a1,",",b1,",",side1
                printed = printed + 1
            a = a - 1
        if printed == 0:
            #print "There are no solutions for side (C)."
            print "No solutions: (C)."

    # 2 sides    
    elif sides == 2:

        if side1 >= side2:
            z, side1 = side1, side2
            side2 = z

        # sides AB
        c, printed = math.sqrt(side1**2 + side2**2), 0
        if side1 <= side2 and side2 < c:
            #print "\nAssuming the input sides were side (A)&(B), your solution is:"
            print "\n(A)&(B):"
            print "     ",side1,",",side2,",",c
            printed = printed + 1
        if printed == 0:
            #print "\nThere are no solutions for sides (A)&(B)."
            print "\nNo solutions: (A)&(B)."

        # sides AC
        b, printed = math.sqrt(side2**2 - side1**2), 0
        if side1 <= b and b < side2:
            #print "\nAssuming the input sides were side (A)&(C), your solution is:"
            print "\n(A)&(C):"
            print "     ",side1,",",b,",",side2
            printed = printed + 1
        if printed == 0:
            #print "\nThere are no solutions for sides (A)&(C)."
            print "\nNo solutions: (A)&(C)."

        # sides BC
        a, printed = math.sqrt(side2**2 - side1**2), 0
        if a < side1 and side1 < side2:
            #print "\nAssuming the input sides were side (B)&(C), your solution is:"
            print "\n(B)&(C):"
            print "     ",a,",",side1,",",side2
            printed = printed + 1
        if printed == 0:
            #print "\nThere are no solutions for sides (B)&(C)."
            print "\nNo solutions: (B)&(C)."
        
    else:
        print "\nYou are an imbecile.  What you said makes no sense."
        
main()


