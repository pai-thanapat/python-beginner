# 36. Membership Operator


# String
word = "APPLE"

letter = input("Guess a letter: ")

if letter.lower() in word.lower():
    print(f"There is a letter '{letter}' in the word!")
else:
    print(f"Sorry, the letter '{letter}' is not in the word.")


# Set
students = {"John", "Mary", "Bob", "Alice"}

student = input("Enter a student's name: ")

if student not in students:
    print(f"{student} is not a student in the class.")
else:
    print(f"{student} is a student in the class.")


# Dictionary
grades = {"John": "A", "Mary": "B", "Bob": "C"}

student = input("Enter a student's name: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"{student} is not in the grade book.")


# Email Validation
email = "john@example.com"

if "@" in email and "." in email:
    print("This is a valid email address.")
else:
    print("This is not a valid email address.")
