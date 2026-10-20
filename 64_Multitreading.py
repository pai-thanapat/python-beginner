# 64. Multithreading

import threading
import time


def walk_dog(name, last_name):

    time.sleep(8)

    print(f"You finished walking with {name} {last_name}.")


def take_out_trash():

    time.sleep(2)

    print("You finished taking out the trash.")


def get_mail():

    time.sleep(4)

    print("You get the mail.")


chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are completed")
