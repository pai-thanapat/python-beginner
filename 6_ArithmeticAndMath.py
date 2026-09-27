# 6. Arithmetic and Math

import math

# Operators
friends = 4

friends = friends + 1

print(friends)

friends += 1

print(friends)

friends = friends - 2

print(friends)

friends -= 2

print(friends)

friends = friends * 3

print(friends)

friends *= 3

print(friends)

friends = friends / 2

print(friends)

friends /= 2

print(friends)

friends = friends**2

print(friends)

friends **= 2

print(friends)

friends = friends % 3

print(friends)

friends %= 3

print(friends)
print("------------------------------")

# Math Functions
x = 3.14
y = -4
z = 5

roundx = round(x)
absy = abs(y)
power = pow(z, 2)
maximum = max(x, y, z)
minimum = min(x, y, z)

print(roundx)
print(absy)
print(power)
print(maximum)
print(minimum)

sqrtz = math.sqrt(9)
ceil = math.ceil(9.1)
floor = math.floor(9.9)

print(math.pi)
print(math.e)
print(sqrtz)
print(ceil)
print(floor)


# Exercise 1

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle is: {round(circumference, 2)}")


# Exercise 2

radius = float(input("Enter the radius of the circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}")


# Exercise 3

a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of the hypotenuse is: {round(c, 2)}")
