# Mile-Kilometer
#   This program converts miles to kilometers
# Kevin Kredit
import string

def main():
    print "This program converts miles to kilometers or kilometers to miles."
    print
    which = raw_input("Which do you want to covert? (MtoK or KtoM):   ")
    print
    which = which.lower()
    if which == "mtok":
        mile = input("Input the distance in miles:   ")
        kilometer = mile * 1.609344
        print
        print "The distance in kilometers is:", kilometer, "kilometers."
    if which == "ktom":
        kilo = input("Input the distance in kilometers:   ")
        mile = kilo * 0.621371192
        print
        print "The distance in miles is:", mile, "miles."

main()
                 
