count = 0
times_table = int(input("Which time table do you require? "))
while count < 13:
    multiplication = times_table * count
    print(str(times_table) + " x " + str(count) + " = " + str(multiplication))
    count += 1
