# 13. String Methods

name = input("Enter your name : ")

# Length of string
length = len(name)

print(f"Letter count : {length}")

# Find FIRST position in string
empty_position = name.find(" ")
first_position = name.find("RRR")

print(f"First Position of empty : {empty_position}")
print(f"First position of RRR : {first_position}")

# Find LAST position in string
last_position = name.rfind(" ")

print(f"Last position of empty : {last_position}")

# Capitalize
capitalize_name = name.capitalize()
print(capitalize_name)

# Upper case
upper_case = name.upper()
print(upper_case)

# Lower case
lower_case = name.lower()
print(lower_case)

# Is string digit
is_digit = name.isdigit()
print(f"is digit ? : {is_digit}")

# Is string alphabet
is_alphabet = name.isalpha()
print(f"is alphabet ? : {is_alphabet}")

phone_number = input("Enter your phone number : ")

# Count
dash_amount = phone_number.count("-")
print(f"Amount of dashes(-) in phone number : {dash_amount}")

# Replace
replace_dashes = phone_number.replace("-", "")
print(f"Phone number : {replace_dashes}")


# For more detail use : print(help(str))


# Exercise

username = input("Enter username : ")

if len(username) > 12:
    print("Username is too long")
elif username.find(" ") != -1:
    print("Username should not contain space")
elif not username.isalpha():
    print("Username should only contain letters")
else:
    print("Welcome : " + username)
