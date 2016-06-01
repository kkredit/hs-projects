# pound-kilo.py
#   This program converts pounds to kilos or kilos to pounds
# by: Kevin Kredit
import string

def main():
    print "This program converts American pounds into Metric kilos."
    print "It can also convert Metric kilos into American pounds."
    print
    print 'Which do you want to do? If you want to convert pounds to'
    print 'kilos, type: "kilo". If you want to convert kilos to pounds,'
    which = raw_input('type: "pound":   ')
    which = string.lower(which)
    print

    if which=='kilo':
        pound = input("Enter the weight in pounds: ")
        kilo = pound * 0.453592
        print
        print "The weight in kilos is:", kilo
        
    if which=='pound':
        kilo = input('Enter the weight in kilos: ')
        pound = kilo * 2.20462262
        print
        print 'The weight in pounds is:', pound
        
main()
