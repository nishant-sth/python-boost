## Topic 1: Classes and Objects (The Blueprint)
Why It Matters: This is the most critical concept in this phase. In Django, a database table is a class (a Model), a web page is a class (a View), and a user input form is a class (a Form). Everything is an object. This is how you model real-world concepts (like a User, a Product, or an Order) in your code.

# Core Concepts:

Class: A blueprint for creating objects.
Object (Instance): An individual occurrence of a class. You can have one Car class and many car objects.
__init__ (Constructor): A special method that runs when you create a new object. It's used to set up the object's initial state.
self: A reference to the current instance of the class. It's how an object refers to its own attributes and methods.
Attributes: Variables that belong to an object (e.g., car.color).
Methods: Functions that belong to an object (e.g., car.start_engine()).

# Code In Action:
```

class Dog:
    # The __init__ method is the constructor for the class.
    # It sets up the initial attributes for any new Dog object.
    def __init__(self, name: str, breed: str, age: int):
        self.name = name
        self.breed = breed
        self.age = age
        self.is_sitting = False
        print(f"{self.name} the {self.breed} has been created!")

    # This is a method. It's a function that belongs to the class.
    # It can access and modify the object's attributes using 'self'.
    def bark(self):
        return f"{self.name} says: Woof!"

    def sit(self):
        print(f"{self.name} is now sitting.")
        self.is_sitting = True

    def stand(self):
        print(f"{self.name} is now standing.")
        self.is_sitting = False

# Creating two INSTANCES (objects) of the Dog class.
my_dog = Dog("Rex", "German Shepherd", 5)
your_dog = Dog("Buddy", "Golden Retriever", 2)

# Calling methods on the objects
print(my_dog.bark())
print(your_dog.bark())

# Accessing attributes and calling methods
print(f"Is {my_dog.name} sitting? {my_dog.is_sitting}")
my_dog.sit()
print(f"Is {my_dog.name} sitting now? {my_dog.is_sitting}")
```
# Your Mission:

Create a script ecommerce.py.
Inside, define a Product class.
The __init__ method should accept name, price, and initial_stock.
Create a method display() that prints the product's details in a clean format.
Create a method sell(quantity) that reduces the stock by the given quantity. Add a check to ensure you don't sell more than you have in stock.
Create a method restock(quantity) that increases the stock.
Create at least two different product objects (e.g., a "Laptop" and a "Mouse") and test all their methods.