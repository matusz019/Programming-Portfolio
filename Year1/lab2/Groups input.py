Total = input("What is the total number of students in the class: ")
Group_size = int(input("What is the required group size: "))
Group = int(Total) // Group_size
Remainder = int(Total) % Group_size
if Group > 1:
    print("The total amount of full groups is: " + str(Group))
elif Group == 1:
    print("There is only 1 group")
else:
    print("There are no full groups")
    print(f"There are {Total} students left")
if Remainder == 1:
    print("There is only 1 student left over")
elif Remainder > 1:
    print("The amount of students left over is: " + str(Remainder))
else:
    print("There are no students left over")
