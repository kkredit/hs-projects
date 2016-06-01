# jumble.py
#   A program to solve jumble puzzles

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    from string import split
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

dictionary = load_words()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def anagram(word):
    if word == '':
        return ['']
    else:
        ans = []
        for w in anagram(word[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+word[0]+w[pos:])
        return ans

def isWord(word,low,high,index):
    mid = (low+high)/2
    if word == dictionary[mid]:
        return mid
    elif low > high:
        return ''
    elif len(dictionary[mid]) > index:
        if word[:index] == dictionary[mid][:index]:
            return isWord(word,low,high,index+1)
        elif alphabet.index(word[index]) < alphabet.index(dictionary[mid][index]):
            return isWord(word,low,mid-1,index)
        elif alphabet.index(word[index]) > alphabet.index(dictionary[mid][index]):
            return isWord(word,mid+1,high,index)
    else:
        return isWord(word,low,high+2,index)

def main():
    from string import lower,split
    word = lower(raw_input('\nWhat are the scrambled letters: '))
    found,printed = 0,[]
    for w in anagram(word):
        #real = isWord(w,0,len(dictionary)-1,1)
        #if type(real)==int:
        #    print '\nThe unscrambled word is',dictionary[real]
        #    found = True
        #    break
        parts = 0
        for part in split(w):
            if part in dictionary:
                parts += 1
        if parts == len(split(w)):
            if not found:
                print '\nThe letters unscrambled:\n'
            if w not in printed:
                print w
                printed.append(w)
            found += 1
            #if parts == 1:break########
    if not found:
        print '\nThose letters do not form any words.'
    if lower(raw_input('\nAgain? ')[0]) == 'y':main()

if __name__=='__main__':main()
