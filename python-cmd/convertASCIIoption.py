# optionASCII.py
#       A program to convert a sequence of ASCII numbers into a sring of text
#       Or the other way around.
# Kevin Kredit

import string 

def main():
    print "This program converts a sequence of ASCII numbers into"
    print "the sring of text that it represents.It can also change"
    print "text into ASCII numbers."
    print

    print 'Which do you want ot do? If you want to convert'
    print 'text to ASCII, type: "ASCII", if you want ot convert'
    which = raw_input('ASCII to text, type: "text":   ')
    which = string.lower(which)
    print
# ASCII to Text
    if which=='text':
        inSting = raw_input("PLease enter the ASCII-encoded message: ")

        message = ""
        for numStr in string.split(inSting):
            asciiNum = eval(numStr)
            message = message + chr(asciiNum)

        print "The encoded message is:", message
        print
# Text ot ASCII
    if which=='ascii':
        message = raw_input("Please enter the message to encode: ")

        print
        print "Here are the ASCII codes:"

        for ch in message:
            print ord(ch),
        print
# Rude Computer
    if not which=='text' or 'ascii':
        print 'Are you some kind of idiot? Type what I told you!'
        
main()
