# acronyms.py
#       This program makes acronyms out of phrases determined by the user.
# Kevin Kredit

import string

def main():
    print "This program makes acronyms out of phrases determined by the user."
    
    phrase = raw_input("Input the phrase that you want to become an acronym: ")

    acr = ""

    for word in string.split(phrase):
        acr = acr + word[0]

    x = string.upper(acr)

    print x       

main()
    
    
                
