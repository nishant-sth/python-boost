 ## Topic 2: Generators (Memory-Efficient Iteration)
Why It Matters: This is a critical concept for performance. Imagine you need to process a 10 GB log file or a database query that returns a million rows. If you load it all into a list in memory, your application will crash. Generators let you work with these huge sequences one item at a time, using almost no memory. Django's QuerySets are lazy and behave like generators for this exact reason.

# Core Concepts:

A generator is an iterator, but you can only iterate over it once.
A function becomes a generator function when it uses the yield keyword instead of return.
yield pauses the function, saves its state, and gives a value back to the caller. When the caller asks for the next item, the function resumes right where it left off.
Generator Expressions: Similar syntax to list comprehensions but with () instead of []. They create a generator object instead of a full list.
# Code In Action:
```

Python

import sys

# A function that builds a HUGE list in memory. This is BAD.
def list_of_squares(n):
    huge_list = []
    for i in range(n):
        huge_list.append(i * i)
    return huge_list

# A generator function that does the same thing. This is GOOD.
def generator_of_squares(n):
    for i in range(n):
        # 'yield' makes this a generator. It 'returns' one value at a time.
        yield i * i

# Let's see the memory difference for a million numbers
my_list = list_of_squares(1_000_000)
print(f"Memory used by list: {sys.getsizeof(my_list)} bytes")

my_gen = generator_of_squares(1_000_000)
print(f"Memory used by generator object: {sys.getsizeof(my_gen)} bytes")

# You can iterate over a generator just like a list
print("\nFirst 5 squares from generator:")
count = 0
for sq in my_gen:
    if count >= 5:
        break
    print(sq)
    count += 1
```
# Your Mission:

Write a generator function fibonacci(limit) that yields Fibonacci numbers up to a given limit. (The sequence starts 0, 1, 1, 2, 3, 5, 8...).
Write a script that calls this generator and prints each Fibonacci number it produces.
Create a "lazy" version of your list comprehension from the previous mission. Given prices = [10.99, 25.50, 9.75, 50.00, 105.25], create a generator expression that yields each price increased by 20%. Loop through the generator and print each new price.