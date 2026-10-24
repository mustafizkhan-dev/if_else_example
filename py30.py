#Check the type of number (single, double, or three digit)
    #This program classifies positive integers by digit count.



num = int(input("Enter a number: "))
num = abs(num)

if num <= 9:
    print("Single-digit number")
elif num <= 99:
    print("Double-digit number")
elif num <= 999:
    print("Three-digit number")
else:
    print("More than three digits")

