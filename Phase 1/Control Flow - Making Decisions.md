# Topic 3: Control Flow: Making Decisions
Why It Matters: Your application needs to make decisions and perform repetitive tasks. Control flow is how you tell the computer what to do and when. Validating a password? Looping through a list of products? This is it.

# Core Concepts:

if, elif, else: For making decisions based on conditions.
for loop: For iterating over a sequence (like a list, tuple, or dictionary).
while loop: For repeating a block of code as long as a condition is true.
Code In Action:

## 🧑‍💻 Code
```
    # if/elif/else: Check a user's permission level
user_role = "admin"

if user_role == "admin":
    print("Full access granted.")
elif user_role == "editor":
    print("Can write and edit posts.")
else:
    print("Read-only access.")

# for loop: Print all items in a shopping cart
cart_items = ["Milk", "Bread", "Eggs"]
print("\nItems in your cart:")
for item in cart_items:
    print(f"- {item}")

# while loop: A simple countdown
count = 3
while count > 0:
    print(f"{count}...")
    count -= 1 # Crucial: Don't forget to change the condition variable!
print("Go!")
```
# Your Mission:

The Number Guessing Game: Write a script that generates a random number between 1 and 100.
Use a while loop to repeatedly ask the user to guess the number.
Inside the loop, use if/elif/else to tell the user if their guess is too high, too low, or correct.
If they guess correctly, print a success message and break the loop.
Bonus: Keep track of the number of guesses and print it at the end.