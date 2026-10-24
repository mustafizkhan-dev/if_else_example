#Check whether a character is uppercase or lowercase


ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Neither uppercase nor lowercase")