# lightning.py
#   This program calculates the distance of a lightning strike
# Kevin Kredit

def main():
    print "This program calculates the distance of a lightning strike."
    print
    print "Input the amount of time between"
    time = input("the flash and the thunder(seconds): ")

    distance = (1100.0 * time) / 5280.0
    print "The distance away is", distance, "mile(s)."

main()
