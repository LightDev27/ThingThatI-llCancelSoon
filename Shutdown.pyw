import time
import os
from datetime import datetime

dt = datetime.now()
day = dt.isoweekday()

day5h = "1311"
day6h = "1401"

def shutdown():
    if day == 1 or day == 4 or day == 5:
        if day5h == time.strftime("%H%M", time.localtime()):
            os.system("shutdown /s /t 0")
    elif day == 2 or day == 3:
        if day6h == ("%H%M", time.localtime()):
            os.system("shutdown /s /t 0")

while True:
    shutdown()
    time.sleep(10)
