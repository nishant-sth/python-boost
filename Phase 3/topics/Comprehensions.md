## Topic 1: Comprehensions (The Pythonic Way to Create Collections)
Why It Matters: Writing a for loop to build a list is fine. But a comprehension is often more readable, more concise, and faster. It's a clear signal that you're fluent in the language. They are used constantly for transforming data.

# Core Concepts:

List Comprehension: A compact way to create a list from an existing iterable. [expression for item in iterable if condition]
Dictionary Comprehension: The same concept, but for creating dictionaries. {key_expression: value_expression for item in iterable if condition}

# Code In Action:
```
Python

# --- The old way with a for loop ---
numbers = [1, 2, 3, 4, 5, 6]
squares = []
for num in numbers:
    if num % 2 == 0: # only for even numbers
        squares.append(num * num)
print(f"Old way: {squares}")

# --- The new way with a List Comprehension ---
# Read it like a sentence: "[square the number] [for each number] [in the numbers list] [if the number is even]."
squares_comp = [num * num for num in numbers if num % 2 == 0]
print(f"Comprehension: {squares_comp}")


# --- Dictionary Comprehension ---
# Let's create a dictionary mapping a user ID to a username
users = [
    (101, "alex"),
    (202, "barb"),
    (305, "charlie")
]
user_map = {user_id: username for user_id, username in users}
print(f"User map: {user_map}")
```
# Your Mission:

You are given a list of strings: words = ["hello", "world", "python", "is", "fun"].
Use a list comprehension to create a new list called upper_words that contains all the words from the original list, but in uppercase.
You have a list of product prices: prices = [10.99, 25.50, 9.75, 50.00, 105.25]. Use a list comprehension to create a new list called prices_with_tax where each price is increased by 20%.
Use a dictionary comprehension and the words list to create a dictionary where the keys are the words and the values are the lengths of the words.