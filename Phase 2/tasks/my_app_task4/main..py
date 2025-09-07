# Import the User class FROM the user module WITHIN the models package
from models.user import User

# Import the entire formatter module from the utils package
from utils import formatter
from utils.calculator import add

print(formatter.format_as_header("Application Start"))

user1 = User("Alice")
user2 = User("Bob")

print(f"Created user: {user1}")
print(f"Created user: {user2}")

print(formatter.format_as_header("Application End"))

a = int(input("Enter a first number "))
b = int(input("Enter the second number "))

result = add(a, b)

print (f"The sum of {a} and {b} is {result}.")