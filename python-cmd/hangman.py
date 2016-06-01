# 6.00 Problem Set 3
# 
# Hangman
#

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
from random import randrange
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
def play_game():
    print '\nWelcome to the game Hangman!'
    while True:
        word,guesses,letters = initGame()
        while True:
            guesses,letters,won,lost = playerTurn(word,guesses,letters)
            if won or lost:break
        print won or lost
        if raw_input('\nPlay again? ')[0] != 'y':break

def initGame():
    word = wordlist[randrange(0,len(wordlist))]
    print '\nI am thinking of a word',len(word),'letters long.'
    return word,20-len(word),'abcdefghijklmnopqrstuvwxyz'

def playerTurn(word,guesses,letters):
    initTurn(guesses,letters)
    while True:
        guess = raw_input('Please guess an unchosen letter: ')
        if guess in letters:break
    gnum = letters.index(guess)
    letters = letters[0:gnum]+letters[gnum+1:len(letters)]
    won = '\nGood job! You won.'
    lost = ''
    if guess in word:print 'Good guess:',
    else:
        print 'Oops! that letter is not in my word:',
        guesses -= 1
        if guesses == 0:
            won = ''
            lost = '\nToo bad, you lost.\nThe correct word was '+word+'.'
    for letter in word:
        if not(letter in letters):print letter,
        else:
            print'_',
            won = ''
    return guesses,letters,won,lost

def initTurn(guesses,letters):
    print '\n-----------------------'
    print 'You have',guesses,'guesses left.'
    print 'Available letters: '+letters+'.\n'

if __name__=='__main__':play_game()




