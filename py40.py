#Check whether a password is valid using nested if
    #Assumption: The password must have at least 8 characters and contain the word @.



password = input("Enter password: ")

if len(password) >= 8:
    if "@" in password:
        print("Valid password")
    else:
        print("Password must contain @")
else:
    print("Password must have at least 8 characters")
#Programs using match case
#Note: match case is available in Python 3.10 and later.
