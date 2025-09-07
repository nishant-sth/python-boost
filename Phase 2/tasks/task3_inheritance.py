# Your Mission:

# Create a base class Vehicle with an __init__ that takes make and model. It should also have a method get_info() that returns a string like "Make: Toyota, Model: Camry".
# Create a Car class that inherits from Vehicle. Its __init__ should also take number_of_doors. It should override the get_info() method to add the number of doors to the output string. Use super().get_info() to avoid rewriting code.
# Create a Motorcycle class that inherits from Vehicle. Its __init__ should also take type_of_bike (e.g., "Cruiser", "Sport"). It should also override get_info() to add the bike type.
# Create one Car object and one Motorcycle object and print their info using the get_info() method to see the different outputs.

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors
    
    def get_info(self):
        super().get_info()
        print(f"No of Doors: {self.number_of_doors}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, type_of_bike):
        super().__init__(make, model)
        self.type_of_bike = type_of_bike
    
    def get_info(self):
        super().get_info()
        print(f"Type: {self.type_of_bike}")


car = Car("Toyota", "Camry", 4)
motorcycle = Motorcycle("KTM", "ktm-390", "Sport")

car.get_info()
motorcycle.get_info()
