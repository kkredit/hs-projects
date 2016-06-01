# quadratic3.py
# Kevin Kredit
import math  # Makes math library available.

def main():
    print "This program finds the real solutions to a quadratic"
    print

    a, b, c = input("Please enter the coefficients (a, b, c): ")

    discrim = b * b - 4 * a * c
    if discrim >= 0:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)

        print "\nThe solutions are:", root1, root2
    else:
        print "\nThe equation has no real roots!"

main()
