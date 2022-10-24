import statistics

temps = []
rainfalls = []
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
max_month = ""
min_month = ""


def averages(arainfalls):
    maximum = max(arainfalls)
    minimum = min(arainfalls)
    mean_avg = statistics.mean(arainfalls)
    std_dev = statistics.pstdev(arainfalls)
    print(f"""
    The maximum rainfall is {maximum}mm in {max_month}
    the minimum rainfall is {minimum}mm in {min_month}
    
    Average: {mean_avg}mm
    Standard Deviation: {std_dev}mm""")


for month in months:
    rainfall = int(input(f"Enter rainfall for {month}: "))
    if rainfalls:
        if rainfall > rainfalls[-1]:
            max_month = month
        elif rainfall < rainfalls[-1]:
            min_month = month
    rainfalls.append(rainfall)

averages(rainfalls)

