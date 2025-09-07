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