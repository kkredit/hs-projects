# printfile.py
#   Prints a file to the screen
# Kevin Kredit

def main():
    fname = raw_input('Enter file name: ')
    infile = open(fname, 'r')
    data = infile.read()
    print data

main()
    
