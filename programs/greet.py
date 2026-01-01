import time

timestamp = time.strftime("%H:%M:%S")

print("Time: ", timestamp)

hour = int(time.strftime('%H'))

if (11 > hour >= 6):
    print("Good Morning".title())
elif (18 > hour >= 11):
    print("Good Afternoon".title())
else:
    print("Good Night".title())
