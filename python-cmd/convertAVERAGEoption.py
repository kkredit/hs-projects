# avg2.py
#   A simple program to average two exam scores
#   Illustrates use of multiple input
# by: Kevin Kredit

def main():
    print "This program computes the average of exam scores."
    print
    n = input("How many numbers do you need averaged together?   ")
    print
    total = 0

    for i in range(n):
        b = input("What is the number?   ")
        total = total + b
        average = total / n

    print
    print "The average of the exam scores is:", average

main()
