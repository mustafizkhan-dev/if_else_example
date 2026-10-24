#Build a simple ATM menu using match case


balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print("Current balance: ₹", balance)

    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Deposited successfully")
            print("New balance: ₹", balance)
        else:
            print("Invalid amount")

    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance: ₹", balance)
        else:
            print("Insufficient balance")

    case 4:
        print("Thank you for using the ATM")

    case _:
        print("Invalid choice")


