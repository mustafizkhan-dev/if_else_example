#Check whether a number is divisible by both 3 and 7


num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")