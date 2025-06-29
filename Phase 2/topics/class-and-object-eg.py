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