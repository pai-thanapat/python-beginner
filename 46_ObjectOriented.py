# 46. Object Oriented

from base_class.base_car import Car

car1 = Car("Mustang", 2024, "yellow", False)
car2 = Car("Audi", 1998, "red", False)
car3 = Car("Tank", 2000, "green", True)

# Class Attribute
print(f"car 1 class : {car1}")
print(f"car 1 model : {car1.model}")
print(f"car 1 year : {car1.year}")
print(f"car 1 color : {car1.color}")
print(f"car 1 for sale : {car1.is_for_sale}")

print(f"car 2 color : {car2.color}")

print(f"car 3 model : {car3.model}")


# Class Method
car3.drive()

car2.stop()

car1.describe()
