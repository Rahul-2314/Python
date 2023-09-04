import time
timestamp = time.strftime("%H:%M:%S")
print("Time: ", timestamp)
hour = int(time.strftime('%H'))
if (11 > hour >= 6):
    print("good morning".title())
elif (18 > hour >= 11):
    print("good afternoon".title())
else:
    print("good night".title())
