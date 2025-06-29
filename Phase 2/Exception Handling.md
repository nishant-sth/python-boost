## Topic 4: Exception Handling (Preparing for Failure)
Why It Matters: In the real world, things go wrong. Users enter text where a number is expected, files you try to read don't exist, servers you try to contact are down. If you don't handle these errors, your program will crash. try...except blocks make your code robust and resilient.

# Core Concepts:

try: The block of code that might fail.
except: The block of code that runs if an error occurs in the try block. You should catch specific exceptions (e.g., ValueError, FileNotFoundError).
else: The block that runs if no error occurs.
finally: The block that runs no matter what, whether there was an error or not. Perfect for cleanup tasks.
raise: How you can trigger an error yourself.

# Code In Action:
```

def process_user_age():
    age_str = input("Please enter your age: ")
    try:
        # TRY to convert the input string to an integer
        age_num = int(age_str)
        if age_num < 0:
            # We RAISE our own error if the logic is invalid
            raise ValueError("Age cannot be negative.")
    except ValueError as e:
        # This block runs IF int() fails (e.g., input is "abc")
        # OR if we raised our own ValueError.
        print(f"Error: Invalid age provided. Please enter a positive number. ({e})")
        return None # Exit the function
    else:
        # This block runs ONLY IF the try block succeeded without any errors.
        print("Thank you! Your age has been successfully recorded.")
        return age_num
    finally:
        # This block ALWAYS runs, for cleanup.
        print("--- Age validation complete. ---")

# Let's run it
user_age = process_user_age()
if user_age is not None:
    print(f"In 10 years, you will be {user_age + 10} years old.")
```

# Your Mission:

Take your Product class from the first mission in this phase.
Modify the sell(quantity) method.
Use a try...except block.
First, ensure the quantity is an integer. If not, raise a TypeError with a clear message.
Second, ensure the quantity is a positive number. If not, raise a ValueError.
The existing check for selling more stock than you have should also be a ValueError.
Write code outside the class to test these error conditions. For example, try to call my_product.sell("five") or my_product.sell(-1).