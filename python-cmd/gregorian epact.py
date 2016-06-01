# Gregorian Epact
#   This program finds the Gregorian Epact after you input the date.
# Kevin Kredit
import math

def main():
    print "This program finds the Gregorian Epact after you input the date."
    year = input("Input the date of the year (ex: 2005): ")
    c = year / 100

    epact = (8 + (c / 4) - c + ((8 * c + 13) / 25) + 11 * (year % 19)) % 30
    print "The Gregorian Epact is ", epact, "."

main()
