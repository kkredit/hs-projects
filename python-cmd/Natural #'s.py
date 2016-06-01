# Natural #'s
#   This program dislays a specific number of consecutive natural numbers.
# Kevin Kredit

def main():
    print "This program dislays a specific number of consecutive natural numbers."
    n = input ("Input the number of consecutive natural numbers you want to print: ")

    for i in range (n):
        n = n - 1
        print n

main()
