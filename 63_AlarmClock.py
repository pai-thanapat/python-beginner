# 63. Alarm Clock

import time
import datetime
import pygame


def set_alarm(alarm_time):
    print("Alarm set for:", alarm_time)

    sound_file = "sound/Hallowed Ground - David Simon-Baker, Robert Powell.mp3"

    is_runniung = True

    while is_runniung:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print("Current time:", current_time)

        if current_time == alarm_time:

            print("Wake up! It's time!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_runniung = False

        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")

    set_alarm(alarm_time)
