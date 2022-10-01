Total = input("What is the total number of students in the class: ")
Group = int(Total) // 24
Remainder = int(Total) % 24
print ("The total amount of full groups is: " + str(Group))
print("The amount of students left over is: " + str(Remainder))
