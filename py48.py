#Print language choice using match case


print("1. English")
print("2. Hindi")
print("3. Marathi")
print("4. French")

choice = int(input("Choose a language (1-4): "))

match choice:
    case 1:
        print("You selected English")
    case 2:
        print("You selected Hindi")
    case 3:
        print("You selected Marathi")
    case 4:
        print("You selected French")
    case _:
        print("Invalid language choice")