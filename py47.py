#Check user role using match case


role = input("Enter user role: ").lower()

match role:
    case "admin":
        print("Full access")
    case "user":
        print("Normal access")
    case "guest":
        print("Limited access")
    case _:
        print("Unknown role")