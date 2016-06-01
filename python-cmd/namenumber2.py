# namenumber2.py
#   A program to calculate the number value of your name.
# Kevin Kredit
import string

def main():
    print 'A program to calculate the number value of your name.'
    print
    name = raw_input('Input your name: ')

    name = name.lower()

    num = 0

    for ch in name:
        if (ord(name[0]))== 32:
            num = num + 64
        num = num + (ord(name[0])-96)

        name = name[1:]
    
    print 'The numeric value of your name is:', num

main()
