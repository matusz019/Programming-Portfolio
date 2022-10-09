password = input("Please input a password: ")
validation = input("Please input the password again: ")
if password == validation:
    print("Password set")
else:
    print("The 2 passwords were different")