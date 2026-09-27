# 3. Typecasting

name = "Bro Code"
age = 21
gpa = 3.4
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# Cast to Integer
gpa = int(gpa)

print(gpa)

# Cast to Float
age = float(age)

print(age)

# Cast to String
age = str(age)

print(f"Age: {age}, Type: {type(age)}")

age += "1"
print(age)

# Cast to Boolean
name = bool(name)
print(name)

empty_string = bool("")
print(empty_string)
