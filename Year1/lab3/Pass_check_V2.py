
password = input("Please input a password: ")
validation = input("Please input the password again: ")
if password == validation and 8 <= len(password) <= 12:
    print("Password set")
elif len(password) < 8:
    print("The password is too short")
elif len(password) > 12:
    print("The password is too long")
else:
    print("The 2 passwords were different")
