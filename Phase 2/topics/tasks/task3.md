# Your Mission:

Create a base class Vehicle with an __init__ that takes make and model. It should also have a method get_info() that returns a string like "Make: Toyota, Model: Camry".
Create a Car class that inherits from Vehicle. Its __init__ should also take number_of_doors. It should override the get_info() method to add the number of doors to the output string. Use super().get_info() to avoid rewriting code.
Create a Motorcycle class that inherits from Vehicle. Its __init__ should also take type_of_bike (e.g., "Cruiser", "Sport"). It should also override get_info() to add the bike type.
Create one Car object and one Motorcycle object and print their info using the get_info() method to see the different outputs.