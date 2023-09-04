# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
# l = ["Rahul"]
# Your program should pronouce:
# Shoutout to Rahul
# Note: If you are not using windows, try to figure out how to do the same thing using some other package

import pyttsx3

inputs=input("enter names (separated by \",\") :")
names=inputs.split(",")

for name in names:
    speaker=pyttsx3.init()
    speaker.say(f"Shoutout to {name} ")
    speaker.runAndWait()
