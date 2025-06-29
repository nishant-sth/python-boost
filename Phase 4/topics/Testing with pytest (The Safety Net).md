## Topic 4: Testing with pytest (The Safety Net)
Why It Matters: How do you know your code actually works? How do you prevent a new feature from breaking an existing one? You write automated tests. Code without tests is brittle and dangerous to change. pytest is the standard for testing in the Python community because it's powerful and has a simple, clean syntax.

# Core Concepts:

Tests are just Python functions that verify your code behaves as expected.
Test files should be named test_*.py or *_test.py.
Test functions must be named test_*.
The assert keyword is used to check if a condition is true. If it's false, the test fails.

# The Code and Commands in Action:
```
Create a file: calculator.py

Python

def add(x, y):
    """Adds two numbers together."""
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    return x + y
Create a test file: test_calculator.py

Python

# Import the function you want to test
from calculator import add
import pytest # Import pytest to use its features

# A simple test case for the "happy path"
def test_add_positive_numbers():
    assert add(2, 3) == 5

# Another test for a different scenario
def test_add_negative_numbers():
    assert add(-1, -1) == -2

# A test for an edge case
def test_add_zero():
    assert add(5, 0) == 5

# A test to check that your error handling works
def test_add_raises_type_error_for_strings():
    with pytest.raises(TypeError):
        add("two", "three")
Run the tests from your terminal:

Bash

# (venv) $ pip install pytest
# (venv) $ pytest

# Pytest will automatically discover and run your tests.
# You'll get a clean output showing how many tests passed or failed.
```

# Your Mission:

In your api_project, create a file validators.py.
Copy your validate_password function from the Phase 1 mission into this file.
Install pytest.
Create a test_validators.py file.
Inside the test file, write at least four separate test functions:
test_valid_password that asserts True for a good password.
test_password_too_short that asserts False for a short password.
test_password_missing_uppercase that asserts False.
test_password_missing_number that asserts False.
Run pytest and see all your tests pass.