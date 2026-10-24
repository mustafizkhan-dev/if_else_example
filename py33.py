#Check whether a person can apply for a loan
    #Assumption: Age must be at least 21 and monthly salary must be at least ₹25,000.



age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))

if age >= 21:
    if salary >= 25000:
        print("Eligible to apply for a loan")
    else:
        print("Salary is too low")
else:
    print("Age requirement not met")