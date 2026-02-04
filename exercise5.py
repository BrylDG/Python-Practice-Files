user_name = "admin"
password = "admin"

enteredUserName = input("Enter username: ")
enteredPassword = input("Enter password: ")

if user_name == enteredUserName and password == enteredPassword:
    print("Correct Credentials")
else:
    print("Invalid Credentials")