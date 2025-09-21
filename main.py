username = "admin"
password_length = 12 

username = input("Enter username: ")
password = input("Enter password: ")


password_length = len(password)


if username == "admin":
    
    if password_length >= 10:
        print("Login successful.")
    else:
        print("Admin password incorrect.")
else:
    
    if password_length >= 6:
        print("Login successful.")
    else:
        print("User password must be 6+ characters.")
