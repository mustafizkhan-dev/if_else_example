#Check salary bonus based on years of service
#Assumed rule: 10 or more years = 10% bonus; otherwise, no bonus.



salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years >= 10:
    bonus = salary * 0.10
    print("Bonus:", bonus)
else:
    print("No bonus")