#Check whether a number lies between 10 and 50
   #This program includes both 10 and 50.


num = int(input("Enter a number: "))

if num >= 10:
    if num <= 50:
        print("Number lies between 10 and 50")
    else:
        print("Number is greater than 50")
else:
    print("Number is less than 10")