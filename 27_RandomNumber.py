# 27. Random Number

import random

low = 1
high = 100

random_number = random.randint(low, high)
print(f"Random number between {low} and {high}: {random_number}")

random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")

options = ("rock", "paper", "scissors")
option = random.choice(options)

print(f"Random choice from {options}: {option}")

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
random.shuffle(cards)

print(f"Shuffled cards: {cards}")
