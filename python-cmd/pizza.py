# pizza
#   This program calculates the price psi of pizza
# Kevin Kredit

def main():
    print "This program calcultes the price psi of pizza."
    diam = input("Input the diameter of the pizza: ")
    price = input("Input the price of the pizza: ")

    price_psi = (diam / 2.0)**2 * 3.14159 / price
    price_psi = price_psi / 100

    print "The price psi of the pizza is: $", price_psi, 

main()
    
