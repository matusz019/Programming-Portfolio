bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password = input("Please input a password: ")
    validation = input("Please input the password again: ")
    if password == validation and 8 <= len(password) <= 12 and password not in bad_passwords:
        print("Password set")
        break
    elif len(password) < 8:
        print("The password is too short")
    elif len(password) > 12:
        print("The password is too long")
    elif password in bad_passwords:
        print("That is a bad password")
    else:
        print("The 2 passwords were different")