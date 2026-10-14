# 51. Polymorphism

from abc import ABC, abstractmethod


class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Pizza(Circle):
    def __init__(self, topping, size):
        super().__init__(size)

        self.topping = topping


circle = Circle(4)
square = Square(5)
triangle = Triangle(6, 7)
pizza = Pizza("Pepperoni", 12)

shapes = [circle, square, triangle, pizza]

for shape in shapes:
    print(f"Area of {shape.__class__.__name__}: {shape.area()}")
