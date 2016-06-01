# username.py
#   Simple string processing program to generate usernames.
# Kevin Kredit

def main():
    print "This program is used to generate usernames."
    print

    # get user's first and last names
    first = raw_input("Please enter your first name (all lower case): ")
    last = raw_input("Please enter your last name (all lower case): ")

    # concentrate first initial with seven chars of last name.
    uname = first[0] + last[:7]

    # output the username
    print "Your username is:", uname

main()
