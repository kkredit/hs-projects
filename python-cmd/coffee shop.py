# Coffee Shop
#   This program computes the cost of shipping coffee from Konditorei Coffee
# Kevin Kredit

def main():
    print "This program computes the cost of"
    print "shipping coffee from Konditorei Coffee."
    print
    pounds = input("Please enter the number of pounds of your shipment: ")

    price = (pounds * 11.36) + 1.5

    print "The total price will be: $", price, "."

main()
                   
