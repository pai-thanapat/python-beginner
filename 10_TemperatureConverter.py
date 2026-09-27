# 10. Temperature Converter

unit = input("Enter the unit (C or F): ")
temperature = float(input("Enter the temperature: "))

is_valid = True

if unit == "C":
    converted_temperature = (temperature * 9 / 5) + 32
    convert_unit = "F"
elif unit == "F":
    converted_temperature = (temperature - 32) * 5 / 9
    convert_unit = "C"
else:
    print(f"Unit {unit} is invalid.")
    is_valid = False

if is_valid:
    print(
        f"Converted temperature from {temperature} {unit} is {round(converted_temperature, 2)} {convert_unit}"
    )
