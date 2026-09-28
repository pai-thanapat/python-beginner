# 35. Iterable

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end="-")

print()

for number in reversed(numbers):
    print(number, end=" ")

numbers_tuple = (10, 20, 30, 40, 50)

for number in numbers_tuple:
    print(number, end=" ")

print()

fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit, end=" ")

print()

name = "Bro Code"

for character in name:
    print(character, end=" ")

print()

my_dict = {"A": 1, "B": 2, "C": 3}

for key in my_dict:
    print(key, end=" ")

print()

for value in my_dict.values():
    print(value, end=" ")

print()

for key, value in my_dict.items():
    print(f"{key}: {value}")
