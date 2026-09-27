# 19. Countdown Timer

import time

time_left = int(input("Enter the countdown time in seconds: "))

for x in range(time_left, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("Time's up!")
