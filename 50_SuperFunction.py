# 50. Super Function


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"It is a {self.color} shape and {'filled' if self.is_filled else 'not filled'}."
        )


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)

        self.radius = radius

    def describe(self):
        super().describe()

        print(f"It is a circle with an area of {3.14 * self.radius ** 2}.")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)

        self.width = width

    def describe(self):
        super().describe()

        print(f"It is a square with an area of {self.width ** 2}.")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)

        self.width = width
        self.height = height

    def describe(self):
        super().describe()

        print(f"It is a triangle with an area of {0.5 * self.width * self.height}.")


circle = Circle(color="Red", is_filled=True, radius=5)

print(
    f"Circle: Color={circle.color}, Is Filled={circle.is_filled}, Radius={circle.radius}"
)

square = Square(color="Blue", is_filled=False, width=10)

print(
    f"Square: Color={square.color}, Is Filled={square.is_filled}, Width={square.width}"
)

triangle = Triangle(color="Green", is_filled=True, width=8, height=6)

print(
    f"Triangle: Color={triangle.color}, Is Filled={triangle.is_filled}, Width={triangle.width}, Height={triangle.height}"
)

circle.describe()
square.describe()
triangle.describe()
