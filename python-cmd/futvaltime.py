# futval.py
#   A program to compurte the future value of an investment
# Kevin Kredit

def main():
    print "This program calculates the future value"
    print "of an investment. "

    principal = input("Enter the initial principal: ")
    apr = input("Enter the annual interest rate: ")
    time = input("Enter the nuber of years that the investment will sit: ")

    for i in range(time):
        principal = principal * (1 + apr)

    print "The value in ",time ,"years is:", principal

main()
