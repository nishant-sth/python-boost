Topic 3: Code Quality (The Automated Inspector)
Why It Matters: When you work on a team, code style can't be a matter of personal preference. It must be consistent and readable. Furthermore, simple bugs like unused variables or typos should be caught automatically, not by a human. Linters and formatters are non-negotiable tools that automate this process, saving enormous amounts of time and preventing trivial arguments during code reviews.

Core Concepts:

Formatter (black or ruff format): An opinionated tool that automatically rewrites your code to conform to a single, consistent style.
Linter (ruff or flake8): A static analysis tool that scans your code for potential bugs, stylistic errors (like unused imports), and bad practices. We'll use ruff because it's an incredibly fast, all-in-one tool.
The Commands in Action:

Bash

# Inside your activated venv
# (venv) $ pip install ruff

# Create a badly formatted file named 'bad_code.py'
# --- File: bad_code.py ---
# import sys
# import os
#
# def my_func( a,b ):
#    x=a+b
#    return x
#
# result = my_func(5,10)
# print ( "Result is: ",result )
# --- End File ---

# 1. First, format the code automatically.
# (venv) $ ruff format bad_code.py
# Now look at the file. It will be beautifully formatted!

# 2. Next, check for bugs and unused imports.
# (venv) $ ruff check bad_code.py

# The output will be something like:
# bad_code.py:2:8: F401 [*] `os` imported but unused
# Found 1 error.
# [*] Solvable with `ruff --fix`.
Note: The best way to use these is with an editor extension (e.g., for VS Code) that formats and lints your code every time you save.

Your Mission:

In your api_project, install ruff.
Create a Python file and deliberately write some messy code: use inconsistent indentation, import a library but don't use it, and create a variable but never use it.
Run ruff format . to fix the styling.
Run ruff check . to find the unused import and variable errors.