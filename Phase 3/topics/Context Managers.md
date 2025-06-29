## Topic 4: Context Managers (Safe Resource Handling)
Why It Matters: How do you guarantee that a file is closed or a database connection is released, even if your code crashes halfway through? The with statement. This is the standard for managing resources safely. It makes your code cleaner and prevents resource leaks, which are a serious type of bug in long-running backend applications.

# Core Concepts:

The with statement creates a temporary "context" for a block of code.
To create your own context manager, you make a class with two special methods: __enter__ (the setup code, which runs at the start of the with block) and __exit__ (the teardown code, which always runs at the end, even if errors occurred).
A simpler way is to use the @contextmanager decorator from the contextlib library.

# Code In Action:

```
Python

from contextlib import contextmanager

# The CLASS-BASED way to create a context manager
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print("INIT: Preparing to handle file.")

    def __enter__(self):
        # Runs at the start of the 'with' block.
        # Its return value is assigned to the 'as' variable.
        print("ENTER: Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Runs at the end of the 'with' block, NO MATTER WHAT.
        # exc_type, exc_val, exc_tb will contain error info if an error occurred.
        if self.file:
            self.file.close()
        print("EXIT: File closed.")

print("--- Using Class-Based Context Manager ---")
with FileHandler('hello.txt', 'w') as f:
    print("WITH BLOCK: Writing to file.")
    f.write('Hello, context manager!')


# The simpler DECORATOR-BASED way
@contextmanager
def simple_timer(name):
    import time
    try:
        print(f"TIMER '{name}': Starting...")
        start_time = time.time()
        yield # The code inside the 'with' block runs here.
    finally:
        end_time = time.time()
        print(f"TIMER '{name}': Finished in {end_time - start_time:.4f}s.")

print("\n--- Using Decorator-Based Context Manager ---")
with simple_timer("My Process"):
    print("WITH BLOCK: Doing some work...")
    time.sleep(1)
```

# Your Mission:

Create a context manager (using either the class or decorator method, your choice) called SuppressErrors.
It should take a list of exception types to ignore (e.g., [ValueError, TypeError]).
Inside the with block, if an error occurs that is in the list of ignored exceptions, the context manager should "swallow" the error and print a message like "Suppressed a ValueError." The program should not crash.
If an error occurs that is not in the list, it should crash as normal.
Test it by putting code that raises a ValueError inside a with SuppressErrors([ValueError]): block and see that it doesn't crash. Then test it with a ZeroDivisionError to see that it does crash.