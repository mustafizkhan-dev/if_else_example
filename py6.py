#Compare two numbers and print the greater one
#Program:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greater number is:", a)
elif b > a:
    print("Greater number is:", b)
else:
    print("Both numbers are equal")