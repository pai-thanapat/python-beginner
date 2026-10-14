# 56. Property


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width cannot be negative.")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height cannot be negative.")

    @width.deleter
    def width(self):
        del self._width

        print("Width has been deleted.")

    @height.deleter
    def height(self):
        del self._height

        print("Height has been deleted.")


rectangle = Rectangle(3, 4)

print(f"Width: {rectangle.width}, Height: {rectangle.height}")

rectangle.width = 5
rectangle.height = 6

print(f"Width: {rectangle.width}, Height: {rectangle.height}")

del rectangle.width
del rectangle.height
