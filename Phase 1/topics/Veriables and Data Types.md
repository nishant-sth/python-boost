
## Topic 1: Variables and Basic Data Types
Why It Matters: This is the most fundamental concept. All data in your application, from a user's ID to a product's name, is stored in variables using these types.

# Core Concepts:

Variables are just names pointing to objects in memory.
int: Whole numbers (e.g., 10, -5).
float: Numbers with a decimal point (e.g., 99.99, 3.14).
str: Text, enclosed in ' or " (e.g., 'hello', "user@example.com").
bool: Represents True or False. Crucial for logic.

## Code
```

# A user's profile information
user_name = "alex"  # str: for text
user_age = 32      # int: for whole numbers
account_balance = 150.75  # float: for financial data
is_active_subscriber = True # bool: for state (yes/no)

# You can print them to see their values
print(f"User: {user_name}, Age: {user_age}")
print(f"Balance: ${account_balance}")
print(f"Is Active? {is_active_subscriber}")

# You can also check their types
print(f"Type of user_name is: {type(user_name)}")

```
# Your Mission:

Create a script product.py.
Inside, create variables for a product: name (str), price (float), quantity_in_stock (int), and is_on_sale (bool).
Assign realistic values to them.
Write a print statement that displays all the product's information in a readable sentence.
Calculate the total value of the inventory for that product (price * quantity_in_stock) and print it.