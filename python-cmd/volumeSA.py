# volume
#   A program to calculate the Volume and SA of a sphere
# Kevin Kredit

def main():
    print "This program calculates the volume and SA of a sphere."
    radius = input("Input the radius of the given circle: ")
    vol = 4.0 / 3.0 * 3.14159 * radius**3
    area = 4.0 * 3.14159 * radius**2
    print "The volume is:", vol, "; the SA is:", area

main()
    
                   
