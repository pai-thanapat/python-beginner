# 49. Multiple Inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is asleep.")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing!")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bunny")
hawk = Hawk("Hawky")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()

fish.flee()
fish.hunt()

rabbit.eat()
hawk.sleep()
