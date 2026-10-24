#Check ticket price based on age
#Assumed prices: below 5 = free, 5–17 = ₹50, 18–59 = ₹100, 60 and above = ₹60.



age = int(input("Enter age: "))

if age < 5:
    print("Ticket price: Free")
elif age < 18:
    print("Ticket price: ₹50")
elif age < 60:
    print("Ticket price: ₹100")
else:
    print("Ticket price: ₹60")