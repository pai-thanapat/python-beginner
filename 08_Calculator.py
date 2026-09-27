# 8. Calculator

operator = input("Enter operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

is_valid = True

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    is_valid = False

    print(f"Operator {operator} is invalid.")

if is_valid:
    print(f"Result: {round(result, 2)}")
