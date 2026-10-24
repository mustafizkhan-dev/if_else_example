#Check login status based on username and password


username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
#Note: This is a simple practice example, not a secure login system.