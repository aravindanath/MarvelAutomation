import calendar

from datetime import datetime
from datetime import date

mm = 3
yy = 2020

print(calendar.month(yy,mm))

print("is this year a leap year?",calendar.isleap(2020))

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

today = date.today()
print("Today's date:", today)

