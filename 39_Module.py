# 39. Module

# print(help("modules"))

import math
from module import ModuleExample as module_example

print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")

# Custom Mudule
pi = module_example.pi

print(f"Pi from module: {pi}")

square_result = module_example.square(5)

print(f"Square of 5: {square_result}")

cube_result = module_example.cube(3)

print(f"Cube of 3: {cube_result}")

circumference_result = module_example.circumference(4)

print(f"Circumference of circle with radius 4: {circumference_result}")

area_result = module_example.area(4)

print(f"Area of circle with radius 4: {area_result}")
