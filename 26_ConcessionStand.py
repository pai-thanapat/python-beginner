# 26. Concession Stand

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzels": 3.50,
    "soda": 1.50,
    "lemonade": 4.25,
}

cart = []
total = 0

print("------------- Menu -------------")

for key, value in menu.items():
    print(f"{key:<10} ${value:>5.2f}")

print("--------------------------------")

while True:
    item = input("Enter a food to buy (q to quit): ")

    if item.lower() == "q":
        break

    name = item.lower()

    if menu.get(item.lower()):
        cart.append(name)

print("----------- YOUR ORDER ---------")

total = 0

for food in cart:

    price = menu.get(food)

    if price:
        total += price

        print(f"{food:<10} ${price:>5.2f}")

print("--------------------------------")
print(f"Total {total:>5.2f}")
print("--------------------------------")
