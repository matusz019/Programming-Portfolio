from statistics import mean
temps = []
while len(temps) != 6:
    temps.append(int(input("Write the temperature: ")))

maximum = max(temps)
minimum = min(temps)
mean_avg = mean(temps)
print(f"""The maximum temps is {maximum}
the minimum temp is {minimum}
the mean of the temps is {mean_avg}""")
