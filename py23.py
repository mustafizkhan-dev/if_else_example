#Calculate electricity bill based on units consumed
    #Assumed rates: first 100 units at ₹5/unit, next 100 at ₹7/unit, and units above 200 at ₹10/unit.



units = int(input("Enter units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill: ₹", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity bill: ₹", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity bill: ₹", bill)