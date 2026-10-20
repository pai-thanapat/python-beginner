# 62. Date and Time

import datetime

date = datetime.date(2026, 10, 19)
today = datetime.date.today()

time = datetime.time(14, 30, 45)
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S")

print("Date:", date)
print("Today:", today)

print("Time:", time)
print("Now:", now)

target_datetime = datetime.datetime(2027, 10, 19, 14, 30, 45)
current_datetime = datetime.datetime.now()


if target_datetime < current_datetime:
    print("The target date and time has already passed.")
else:
    print("The target date and time is in the future.")
