# userfile.py
#   Program to create a file of usernames in batch mode
# Kevin Kredit

def main():
    print 'This program creates a file of usernames from a'
    print 'file of names.'

    infileName = raw_input('What file are the names in? ')
    outfileName = raw_input('What file should the usernames go in? ')

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    for line in infile:
        first, last = string.split(line)
        uname = string.lower(first[0]+last[:7])
        outfile.write(uname+'\n')

    infile.close()
    outfile.close()

    print 'Usernames have been written to', outfileName

main()
                        
                        
