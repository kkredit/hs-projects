# wordcount.py
#   A program to count the words in a sentence.
# Kevin Kredit
import string

def main():
    sent = raw_input('Input a sentence for the words to be counted in: ')
    print
    x = 0
    n = string.split(sent)
    for ch in n:
        x = x + 1

    print 'The number of words in the sentence is:', x

main()
