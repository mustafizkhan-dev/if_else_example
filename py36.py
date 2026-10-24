#Check whether a person is eligible for a driving license
    #Assumption: Minimum age is 18 years.



age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")