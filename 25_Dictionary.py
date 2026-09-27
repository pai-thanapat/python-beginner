# 25. Dictionary

capitals = {
    "USA": "Washington, D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# Get value
capital = capitals.get("USA")
print(f"Capital of USA: {capital}")

# Result of getting non-existing key
no_key = capitals.get("Germany")
print(f"Capital of Germany: {no_key}")

if capitals.get("japan"):

    print("Capital of Japan is: ", capitals.get("japan"))
else:

    print("Capital of Japan is not found in the dictionary.")

# Add new key-value pair
capitals.update({"Germany": "Berlin"})

print(f"Capital of Germany: {capitals['Germany']}")

# Update existing key-value pair
capitals.update({"USA": "Washington"})

print(capitals)

# Remove key-value pair
capitals.pop("China")

print(capitals)

# Remove last key-value pair
capitals.popitem()

print(capitals)

# Get all keys
keys = capitals.keys()

for key in keys:
    print(key)

# Get all values
values = capitals.values()

for value in values:
    print(value)

# Get all key-value pairs
items = capitals.items()

for key, value in items:
    print(f"{key}: {value}")

# Clear all key-value pairs
capitals.clear()

print(capitals)
