# overtime.py
#   A program to calculate how much overtime money you earn
# exercise 1
# Kevin Kredit

def main():
    print "A program to calculate how much overtime money you earn"
    print "assuming you get 150% pay for overtime over 40 hours."
    print
    time = input("How many hours did you work this week:    ")
    wages = input("How much do you earn per hour:            ")
    print
    if time < 40:
        money = time * wages
    if time >= 40:
        overtime = time - 40
        money = (40 * wages) + (overtime * (1.5 * wages)) 
    print "You earned $",money,"."

main()
