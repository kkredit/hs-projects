# factorial.py
#   Program to compute the factorial of a number
#   Illustrates for loop with an accumulator
# Kevin Kredit

def main():
    n = input("Please enter a whole number: ")
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print "The factorial of", n, "is", fact

main()
