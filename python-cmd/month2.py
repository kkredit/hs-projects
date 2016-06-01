# month2.py
#  A program to print the month abbreviation, given its number.
# Kevin Kredit

def main():

    # months is a list used as a lookup.
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
              "Aug", "Sep", "Oct", "Nov", "Dec"]

    n = input("Enter the month nuber (1-12): ")

    print "The month abbreviation is", months[n-1] + "."

main()
