# 52. Duck Typing


class Animal:
    is_alive = True


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Car:
    is_alive = True

    def speak(self):
        return "Beep!"


dog = Dog()
cat = Cat()
car = Car()

animals = [dog, cat, car]

for animal in animals:
    print(f"{animal.__class__.__name__} says: {animal.speak()}")
    print(f"Is {animal.__class__.__name__} alive? {'Yes' if animal.is_alive else 'No'}")
