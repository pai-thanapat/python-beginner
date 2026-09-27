# 2D Collection

fruits = ["apple", "orange", "banana", "coconut"]
vegatables = ["celery", "carrot", "potato"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegatables, meats]

print(groceries)
print(f"first item in the list is: {groceries[0][0]}")

for collection in groceries:

    for item in collection:
        print(item, end=" ")

    print()


# Exercise

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for row in num_pad:
    for num in row:

        print(num, end=" ")

    print()
