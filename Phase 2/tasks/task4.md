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


# Your Mission:

Create the exact directory structure shown above.
Place the code into the correct files.
From the top-level directory (my_app/), run the command python main.py and see the output.
Add a new file utils/calculator.py with a function add(a, b) that returns their sum.
Import and use this add function in main.py.