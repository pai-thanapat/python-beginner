# 28. Number Guessing Game

import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)

guess_count = 0
is_running = True

print("---------- NUMBER GUESSING GAME ----------")
print(f"Select a number between {lowest_number} and {highest_number}.")

while is_running:
    guess = input("Enter your guess: ")

    if not guess.isdigit():

        print("Invalid input. Please enter a number.")

        continue

    guess = int(guess)
    guess_count += 1

    if guess < lowest_number or guess > highest_number:
        print("Invalid input. Number out of range.")
        continue

    if guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(
            f"Congratulations! You've guessed the correct number {answer} in {guess_count} attempts."
        )

        is_running = False
