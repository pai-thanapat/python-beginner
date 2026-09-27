# 21. Collection

fruit = "apple"

print(fruit)


# List
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)
print(fruits[1])
print(fruits[0:3])
print(fruits[::2])
print(fruits[::-1])

# print(dir(fruits))
# print(help(fruits))

# Count the elements in the list
print(f"Number of fruits: {len(fruits)}")

print(f"apple in fruits: {'apple' in fruits}")
print(f"pineapple in fruits: {'pineapple' in fruits}")

# Change the first element
fruits[0] = "pineapple"

# Add new element
fruits.append("pineapple")

# Remove an element
fruits.remove("pineapple")

# Insert an element at a specific index
fruits.insert(0, "pineapple")

# Sort the list
fruits.sort()

# Reverse the list
fruits.reverse()

# Get the index of an element
banana_index = fruits.index("banana")

print(f"banana index: {banana_index}")

# Count the amount of element
banana_count = fruits.count("banana")

print(f"banana count: {banana_count}")

print("------------------------------")

for x in fruits:
    print(x)

# Clear the list
fruits.clear()
print(fruits)
print("------------------------------")


# Set
fruits_set = {"apple", "orange", "banana", "coconut", "coconut"}

print(fruits_set)
print(len(fruits_set))
print("pineapple" in fruits_set)

fruits_set.add("pineapple")
print(fruits_set)

fruits_set.remove("apple")
print(fruits_set)

fruits_set.pop()
print(fruits_set)

fruits_set.clear()
print(fruits_set)
print("------------------------------")


# Tuple
fruits_tuple = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits_tuple)

apple_index = fruits_tuple.index("apple")
print(f"apple index: {apple_index}")

coconut_count = fruits_tuple.count("coconut")
print(f"coconut count: {coconut_count}")

for x in fruits_tuple:
    print(x)
