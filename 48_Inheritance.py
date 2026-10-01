# 48. Inheritance


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is asleep.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")


dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Squeaky")


print(f"{dog.name} is alive: {dog.is_alive}")
print(f"{cat.name} is alive: {cat.is_alive}")
print(f"{mouse.name} is alive: {mouse.is_alive}")

dog.eat()
cat.sleep()

dog.speak()
cat.speak()
mouse.speak()
