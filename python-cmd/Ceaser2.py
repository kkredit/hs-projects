# CeaserCipher2.py
#   A program to encode a string of plain text with a Ceaser cipher code.
# Kevin Kredit

def main():
    print 'This is a program to encode a string of'
    print 'plaintext with Ceaser cipher code.'
    string = raw_input('What string do you want coverted? ')
    print
    key = input('What key value do you want to use? ')
    print
    for ch in string:
        if (ord(ch)+key) > 122:
            print chr(ord(ch)+ key-26),
        if (ord(ch)+key) < 122:
            print chr(ord(ch)+ key),
        if (ord(ch)+key) == 122:
            print chr(ord(ch)+ key),       
    print
        
main()
