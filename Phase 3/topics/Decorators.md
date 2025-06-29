## Topic 3: Decorators (Enhancing Functions)
Why It Matters: This is framework magic, demystified. Decorators are a way to add functionality to an existing function (like checking if a user is logged in, timing how long a function takes, or registering a URL route) without changing the function's code itself. Django's @login_required is a decorator. Master this, and you'll understand a huge part of how modern frameworks operate.

# Core Concepts:

In Python, functions are first-class objects. They can be passed as arguments to other functions.
A decorator is a function that takes another function as an argument, defines a new "wrapper" function inside it, adds some behavior to the wrapper, calls the original function from within the wrapper, and returns the wrapper.
The @ symbol is just "syntactic sugar" for this process.

# Code In Action:
```

Python

# This is our decorator. It's a function that takes a function as input.
def timer_decorator(func):
    # The wrapper function is what actually gets called.
    # *args and **kwargs ensure it can work with any function, regardless of its arguments.
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs) # Call the original function
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to run.")
        return result
    # The decorator returns the wrapper function.
    return wrapper

# Applying the decorator with the '@' syntax.
@timer_decorator
def slow_function(delay_seconds):
    """A sample function that takes some time to run."""
    import time
    print(f"Running slow_function with a delay of {delay_seconds}s...")
    time.sleep(delay_seconds)
    return "Done!"

# When we call slow_function, we are actually calling the 'wrapper' inside the decorator.
slow_function(delay_seconds=2)

# --- Without the '@' syntax, it looks like this: ---
# def another_slow_function():
#     time.sleep(1)
#
# timed_function = timer_decorator(another_slow_function)
# timed_function()
```

# Your Mission:

Write a decorator called @debug_info.
This decorator should print the name of the function being called, the arguments it was called with (args and kwargs), and the value it returns.
Create a simple function add(a, b) that returns their sum.
Apply your @debug_info decorator to the add function and call it (e.g., add(5, 10)) to see your debug output.