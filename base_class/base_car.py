class Car:
    def __init__(self, model, year, color, is_for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.is_for_sale = is_for_sale

    def drive(self):

        print(f"You are driving {self.color} {self.model}.")

    def stop(self):

        print(f"Your {self.model} was stop.")

    def describe(self):
        print(f"Car's detail : {self.year} {self.color} {self.model}")
