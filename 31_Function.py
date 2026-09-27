# 31. Function


def happy_birthday(name, age):
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print(f"Happy Birthday dear {name}!")
    print("Happy Birthday to you!")
    print(f"You are now {age} years old!")


def display_invoice(username, amount, due_date):
    print(f"Hello, {username}:")
    print(f"Your bill of: ${amount:.2f} is due : {due_date}")


def add_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2


def create_name(first_name, last_name):
    return f"{first_name.capitalize()} {last_name.capitalize()}"


happy_birthday("Alice", 25)
display_invoice("Alice", 167.35, "2023-10-01")

result = add_numbers(5, 10)
print(f"The sum is: {result}")

result = subtract_numbers(10, 5)
print(f"The difference is: {result}")

result = multiply_numbers(5, 10)
print(f"The product is: {result}")

result = divide_numbers(10, 2)
print(f"The quotient is: {result}")

full_name = create_name("john", "doe")
print(f"Full name: {full_name}")
