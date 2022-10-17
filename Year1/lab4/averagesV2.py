from statistics import mean

temps = []


def averages(aTemps):
    maximum = max(aTemps)
    minimum = min(aTemps)
    mean_avg = mean(aTemps)
    print(f"""The maximum temps is {maximum}
    the minimum temp is {minimum}
    the mean of the temps is {mean_avg}""")


temp = input("Write your temp here: ")
while True:
    temp = input("Write your temp here: ")
    if temp == "":
        break
    else:
        temps.append(int(temp))
averages(temps)