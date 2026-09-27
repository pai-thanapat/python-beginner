# 9. Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg or lb): ")

is_valid = True

if unit == "kg":
    converted_weight = weight * 2.20462
    convert_unit = "lb"

elif unit == "lb":
    converted_weight = weight / 2.20462
    convert_unit = "kg"
else:
    print(f"Unit {unit} is invalid.")
    is_valid = False

if is_valid:
    print(
        f"Converted weight from {weight} {unit} is {round(converted_weight, 2)} {convert_unit}"
    )
