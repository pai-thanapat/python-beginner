# 7. IF Statement

# Exercise 1

age = int(input("Enter your age: "))

if age >= 100:
    print("You are a century-old person.")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not an adult.")


# Exercise 2

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Here is your food.")
elif response == "N":
    print("Okay, no food for you.")
else:
    print("Invalid input. Please enter Y or N.")


# Exercise 3

name = input("Enter your name: ")

if name == "":
    print("You didn't enter a name.")
else:
    print(f"Hello, {name}!")


# Exercise 4

is_for_sale = True

if is_for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")

is_online = False

if is_online:
    print("This item is available online.")
else:
    print("This item is not available online.")
