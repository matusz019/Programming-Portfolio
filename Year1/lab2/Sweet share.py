Students = int(input("What is the total number of students in the class: "))
Sweets = int(input("How many sweets have you got "))
Group = Sweets // Students
Remainder = Sweets % Students
print("You should give " + str(Group) + " sweets to each student")
print("The amount of sweets left over is: " + str(Remainder))