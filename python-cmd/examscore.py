# examscore.py
#       This program computes the letter grade for a 100 point exam
# Kevin Kredit

def main():
    print "This program computes the letter grade for a 100 point exam."
    
    number = input("Enter the score out of 100 that you got: ")
    
    letter = 60*'F'+ 10*'D'+ 10*'C'+ 10*'B'+ 11*'A'

    score = letter[number]

    print "The letter grade you received is:", score

main()
