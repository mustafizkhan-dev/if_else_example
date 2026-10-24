#Check whether a year is a leap year and century year


year = int(input("Enter year: "))

if year % 100 == 0:
    print("Century year")
    if year % 400 == 0:
        print("Leap year")
    else:
        print("Not a leap year")
else:
    if year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")