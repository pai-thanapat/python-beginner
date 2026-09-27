# 4. Input

name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello, {name}!")
print(f"You are {age} years old.")


# Exercise 1

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width

print(f"The area of the rectangle is: {area}")


# Exercise 2

item = input("What item would you like to buy? ")
price = float(input(f"What is the price of {item}? "))
quantity = int(input(f"How many {item}(s) would you like to buy? "))

total_cost = price * quantity

print(f"The total cost of {quantity} {item}(s) is: ${total_cost:.2f}")
