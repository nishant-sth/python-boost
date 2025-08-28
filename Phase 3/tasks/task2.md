# Your Mission:

Create a context manager (using either the class or decorator method, your choice) called SuppressErrors.
It should take a list of exception types to ignore (e.g., [ValueError, TypeError]).
Inside the with block, if an error occurs that is in the list of ignored exceptions, the context manager should "swallow" the error and print a message like "Suppressed a ValueError." The program should not crash.
If an error occurs that is not in the list, it should crash as normal.
Test it by putting code that raises a ValueError inside a with SuppressErrors([ValueError]): block and see that it doesn't crash. Then test it with a ZeroDivisionError to see that it does crash.