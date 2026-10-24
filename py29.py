#Check blood donation eligibility based on age and weight
    #For this basic example, assume the person must be at least 18 years old and weigh at least 50 kg. Actual eligibility depends on local rules and medical screening.



age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))

if age >= 18 and weight >= 50:
    print("Eligible based on age and weight")
else:
    print("Not eligible based on age and weight")