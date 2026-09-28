# 37. List Comprehension

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(f"Normal doubles: {doubles}")

# List comprehension
doubles_expression = [x * 2 for x in range(1, 11)]

print(f"List comprehension doubles: {doubles_expression}")

triples = [y * 3 for y in range(1, 11)]

print(f"List comprehension triples: {triples}")

squares = [z * z for z in range(1, 11)]

print(f"List comprehension squares: {squares}")

fruits = ["apple", "orange", "banana", "coconut"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
first_letters_fruits = [fruit[0] for fruit in fruits]

print(f"Normal fruits: {fruits}")
print(f"List comprehension uppercase fruits: {uppercase_fruits}")
print(f"List comprehension capitalized fruits: {capitalized_fruits}")
print(f"List comprehension first letters of fruits: {first_letters_fruits}")

# Filtering with list comprehension
numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]

print(f"Positive numbers: {positive_numbers}")
print(f"Negative numbers: {negative_numbers}")
print(f"Even numbers: {even_numbers}")

grades = [85, 92, 78, 96, 88, 73, 91, 87]
passing_grades = [grade for grade in grades if grade >= 80]

print(f"Passing grades: {passing_grades}")
