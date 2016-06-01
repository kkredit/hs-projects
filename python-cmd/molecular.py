# molecular weight
#   This program computes the molecular weight of a hydrocarbon
# Kevin Kredit

def main():
    print " This program computes the molecular weight of a hydrocarbon."

    oxy = input("Input the number of oxygen atoms: ")
    car = input("Input the number of carbon atoms: ")
    hyd = input("Input the number of hydrogen atoms: ")

    weight = (oxy * 15.9994) + (car * 12.011) + (hyd * 1.0079)

    print "The molecular weight of the hydrocarbon is:", weight , "grams."

main()
