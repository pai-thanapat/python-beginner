# 53. Static Method


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions


is_cook_valid = Employee.is_valid_position("Cook")
is_driver_valid = Employee.is_valid_position("Driver")

print(f"Is 'Cook' a valid position? {is_cook_valid}")
print(f"Is 'Driver' a valid position? {is_driver_valid}")


employee1 = Employee("John Doe", "Manager")
employee2 = Employee("Jane Smith", "Cashier")
employee3 = Employee("Bob Johnson", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
