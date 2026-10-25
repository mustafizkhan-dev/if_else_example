#Check whether a character is a vowel or consonant
#Program:


ch = input("Enter a character: ").lower()

if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Please enter a single alphabet")