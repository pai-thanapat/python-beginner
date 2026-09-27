# 22. Shopping Cart

foods = []
prices = []
total = 0

while True:

    food = input("Enter a food to buy (q to quit): ")

    if food.lower() == "q":
        break

    price = float(input(f"Enter the price of {food}: "))

    foods.append(food)
    prices.append(price)

print("----- Shopping Cart -----")

for food in foods:
    index = foods.index(food)
    total += prices[index]

    print(f"{food:<10} {prices[index]:>6.2f}$")

print("--------------------------")
print(f"Total: {total:>10.2f}$")
