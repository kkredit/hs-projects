# happy.py
#   A program to sing happy birthday
# Kevin Kredit

def happy():
    print "Happy bithday to you!"

def sing(person):
    happy()
    happy()
    print "Happy birthday, dear", person + "."
    happy()

def main():
    sing("Fred")
    print
    sing("Lucy")
    print
    sing("Elmer")

main()
    
