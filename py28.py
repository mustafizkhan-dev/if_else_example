#Calculate discount based on total shopping amount
    #Assumed discounts: ₹5,000 and above = 20%, ₹2,000–₹4,999 = 10%, below ₹2,000 = no discount.



amount = float(input("Enter shopping amount: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = amount * 0.20
    print("Discount: ₹", discount)
    print("Final amount: ₹", amount - discount)
elif amount >= 2000:
    discount = amount * 0.10
    print("Discount: ₹", discount)
    print("Final amount: ₹", amount - discount)
else:
    print("No discount")
    print("Final amount: ₹", amount)