# File: chaos2.py
# A simple program illistrating chaotic behavior.
# Kevin Kredit

def main():
    print "This program illustrates a chaotic function"
    x = input("Enter a number between 0 and 1: ")
    y = input("Enter another number: ")
    n = input("How many numbers should I print? ")
    j = 1
    print
    print "Index   ",x,"     ",y
    print '-----------------------------------'
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print ' ',j,'   %0.6f' % (x),' %0.6f' % (y)
        j = j + 1
main() 
       


            
