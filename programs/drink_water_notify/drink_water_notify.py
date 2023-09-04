from plyer import notification
import time

title="Drink Water"
message="Time to drink water"
app_icon="C:/Users/chowd/Desktop/Python/programs/drink_water_notify/water-bottle.ico"

# help(notification.notify)

while True:
    time.sleep(100)
    notification.notify(title= title ,message=message , app_icon=app_icon ,timeout=20)
