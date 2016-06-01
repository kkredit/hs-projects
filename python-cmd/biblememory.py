# Kevin Kredit
# biblememory.py
# A program to aid in the studying for Bible memory verses
# 2/27/2010
from string import split,lower
from random import random

def main():
    verse = "My lovely pretend practice verse is so cool! I hope this program "\
            "works, if it didn't I'd be sad; very much so."
    vlist = verse.split()
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM-'qwertyuiopasdfghjklzxcvbnm"
    print '\n\n'
    for word in vlist:
        punc = ''
        if word[len(word)-1] not in alphabet: punc = word[len(word)-1]
        if random() > 0.6: print '_____'+punc,
        else: print word,
    if (raw_input('\n\nAgain? '))[0].lower() == 'y': main()

main()
