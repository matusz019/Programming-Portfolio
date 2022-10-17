def C_to_F(c):
    f = (c * (9 / 5) + 32)
    return f
def F_to_C(f):
    c = (f - 32) * (5/9)
    return c

option = int(input("""Choose and option
         1. Convert from Celsius to Fahrenheit
         2. Convert from Fahrenheit to Celsius
"""))
temp = float(input("Type in your temperature here: "))

if option == 1:
    print(C_to_F(temp))
elif option == 2:
    print(F_to_C(temp))
else:
    print("Error")