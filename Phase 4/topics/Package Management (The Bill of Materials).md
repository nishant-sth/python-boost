Topic 2: Package Management (The Bill of Materials)
Why It Matters: Real projects are built on the work of others. You'll use third-party libraries for everything from making HTTP requests to interacting with databases. pip is the tool to install them. A requirements.txt file is the manifest that lists every library and its exact version. This ensures that you, your teammates, and your production server all build the project with the identical set of dependencies, eliminating "it works on my machine" bugs.

Core Concepts:

pip: Python's package installer. It fetches packages from the Python Package Index (PyPI).
requirements.txt: A standard file for listing a project's dependencies.
pip freeze: A command that generates this list from your current environment.
The Commands in Action:

Bash

# Make sure your virtual environment from the previous step is active!

# (venv) $ pip install requests # Installs the 'requests' library
# (venv) $ pip install python-dotenv # Installs another useful library

# See what's installed in your isolated environment
# (venv) $ pip freeze

# Output will look something like this:
# certifi==2024.6.2
# charset-normalizer==3.3.2
# idna==3.7
# python-dotenv==1.0.1
# requests==2.32.3
# urllib3==2.2.2

# Save this exact list to a file
# (venv) $ pip freeze > requirements.txt

# Now, another developer (or a server) can replicate your environment perfectly
# (venv) $ pip install -r requirements.txt
Your Mission:

Activate the virtual environment inside your api_project.
Use pip to install the requests and Faker libraries.
Generate a requirements.txt file that contains these packages and their dependencies.
Open the file and look at the contents.
(Bonus) Create a second virtual environment, activate it, and use your new requirements.txt file to install the exact same packages.