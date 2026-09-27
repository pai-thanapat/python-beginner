# 12. Conditional Expression

positive_num = 5

print(f"{positive_num} is {('Positive' if positive_num > 0 else 'Negative')}")

negative_num = -3

print(f"{negative_num} is {('Positive' if negative_num > 0 else 'Negative')}")

odd_even = "Even" if positive_num % 2 == 0 else "Odd"

print(f"{positive_num} is {odd_even}")

a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b

print(f"Maximum number between {a} and {b} is {max_num}")
print(f"Minimum number between {a} and {b} is {min_num}")

age = 20

is_adult = "Adult" if age >= 18 else "Child"

print(f"Age {age} is considered as {is_adult}")

temperature = 30

is_hot = "Hot" if temperature > 25 else "Cold"

print(f"Temperature {temperature} is considered as {is_hot}")

user_role = "Admin"

access_level = "Full Access" if user_role == "Admin" else "Limited Access"

print(f"User role {user_role} has {access_level}")
