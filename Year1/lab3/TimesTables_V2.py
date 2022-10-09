count = 0
times_table = int(input("Which time table do you require? "))
if times_table >= 0:
    while count < 13:
        multiplication = times_table * count
        print(str(times_table) + " x " + str(count) + " = " + str(multiplication))
        count += 1
else:
    count = 12
    while count >= 0:
        multiplication = times_table * count
        print(str(times_table) + " x " + str(count) + " = " + str(multiplication))
        count -= 1
