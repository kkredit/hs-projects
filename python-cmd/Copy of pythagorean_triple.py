# Pythagorean_Triple.py
#   A program to find pythagorean triples
# Kevin Kredit

import string
import math

def main():
    print "This program finds Pythagorean triples (a^2 + b^2 = c^2)."
    
    infoa = raw_input("\nDo you know side length (a)?(y/n)   ")
    if infoa == "y":
        a = input("What is the length of side (a)?     ")
        
    infob = raw_input("\nDo you know side length (b)?(y/n)   ")
    if infob == "y":
        b = input("What is the length of side (b)?     ")
        
    infoc = raw_input("\nDo you know side length (c)?(y/n)   ")
    if infoc == "y":
        c = input("What is the length of side (c)?     ")
        
    # yyy & #nnn
    if infoa == infob == infoc:
        print "\nDon't be and imbecile. That makes no sense."
          
    # yyn
    if infoa == "y" and infob == "y" and infoc == "n":
        c = math.sqrt((a**2 + b**2))
        if a <= b and b < c:
            print "\nYour triple is:", a,",",b,",",c
                        
    # yny
    if infoa == "y" and infob == "n" and infoc == "y":
        b = math.sqrt((c**2 - a**2))
        if a <= b and b < c:
            print "\nYour triple is:", a,",",b,",",c
                        
    # ynn
    if infoa == "y" and infob == "n" and infoc == "n":
        x = 1
        b = (((a**2.0)/x)/2)-((1.0/2.0)*x)
        c = (((a**2.0)/x)/2)+((1.0/2.0)*x)
        print "\nPossible solutions are:\n"
        for i in range(1000000):
            b = (((a**2.0)/x)/2)-((1.0/2.0)*x)
            c = (((a**2.0)/x)/2)+((1.0/2.0)*x)
            b1 = int(b)
            c1 = int(c)
            if b1 == b and c1 == c and a <= b1 and b1 < c1:
                print a,",",b1,",",c1
            x = x + 1
                    
    # nyy
    if infoa == "n" and infob == "y" and infoc == "y":
        a = math.sqrt((c**2 - b**2))
        if a < b and b < c:
            print "\nYour triple is:", a,",",b,",",c
                        
    # nyn
    if infoa == "n" and infob == "y" and infoc == "n":
        print "\nPossible solutions are:\n"
        x = 1
        x2 = x/2.0
        c = b+x2
        while c - b >= 1:
            x2 = x/2.0
            aa = ((2*b)+x2)*x2
            a = math.sqrt(aa)
            c = b+x2
            a1 = int(a)
            c1 = int(c)
            if a1 == a and c1 == c and a1 <= b and b < c1:
                print a1,",",b,",",c1
            x = x+1
                    
    # nny
    if infoa == "n" and infob == "n" and infoc == "y":
        n = 0
        x = c / math.sqrt(2)
        a = x
        b = x
        print "\nPossible solutions are:\n"
        a = a - n
        b = math.sqrt((c**2 - a**2))
        while c - b >= 1:
            a = a - n
            b = math.sqrt((c**2 - a**2))
            a1 = int(a)
            b1 = int(b)
            if a1 == a and b1 == b and a1 <= b1 and b1 < c:
                print a1,",",b1,",",c
            if n == 0:
                print x,",",x,",",c
            b = b + n
            a = math.sqrt((c**2 - b**2))
            a1 = int(a)
            b1 = int(b)
            if a1 == a and b1 == b and a1 <= b1 and b1 < c:
                print a1,",",b1,",",c
            n = n + 1

main()           
        
