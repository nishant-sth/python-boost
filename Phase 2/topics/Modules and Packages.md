## Topic 3: Modules and Packages (Organizing Your Project)
Why It Matters: You cannot build a real application in a single file. It becomes unreadable and unmanageable. Modules (single files) and packages (directories of modules) are how you organize your code into logical, reusable units. A Django project is just a Python package, and each Django "app" is another Python package inside it.

# Core Concepts:

Module: Any Python file (.py).
Package: A directory containing a special __init__.py file (can be empty) and other modules/packages.
import: The statement used to bring code from one module into another.
from ... import ...: The statement to import a specific class or function from a module.

# Code In Action:
```
Imagine your project has this file structure:

my_app/
├── main.py
└── models/
    ├── __init__.py  (This file can be empty. It tells Python this is a package)
    └── user.py
└── utils/
    ├── __init__.py
    └── formatter.py
File: my_app/models/user.py

Python

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User({self.name})"
File: my_app/utils/formatter.py

Python

def format_as_header(text: str) -> str:
    return f"\n--- {text.upper()} ---\n"
File: my_app/main.py

Python

# Import the User class FROM the user module WITHIN the models package
from models.user import User

# Import the entire formatter module from the utils package
from utils import formatter

print(formatter.format_as_header("Application Start"))

user1 = User("Alice")
user2 = User("Bob")

print(f"Created user: {user1}")
print(f"Created user: {user2}")

print(formatter.format_as_header("Application End"))
```

# Your Mission:

Create the exact directory structure shown above.
Place the code into the correct files.
From the top-level directory (my_app/), run the command python main.py and see the output.
Add a new file utils/calculator.py with a function add(a, b) that returns their sum.
Import and use this add function in main.py.