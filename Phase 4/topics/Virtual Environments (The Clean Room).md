Topic 1: Virtual Environments (The Clean Room)
Why It Matters: This is the single most important rule of professional Python development. It is not optional. Without a virtual environment, every project on your computer uses the same pool of installed libraries. What happens when Project A needs requests version 1.5 but Project B needs version 2.0? Chaos. A virtual environment is an isolated, self-contained directory that holds a specific version of Python and all the libraries for a single project, ensuring projects don't interfere with each other.

Core Concepts:

An isolated environment for each project.
The venv module is built into Python.
"Activating" an environment means your terminal will use the Python and pip installers from inside that environment, not the global ones.
The Commands in Action:

Bash

# 1. Create a new directory for your project and navigate into it
mkdir my-professional-project
cd my-professional-project

# 2. Create the virtual environment. 'venv' is the name of the directory it creates.
#    You can also use '.venv' which is a common convention.
python -m venv venv

# 3. Activate the environment. Your terminal prompt will change to show it's active.
#    On macOS/Linux:
source venv/bin/activate
#    On Windows (PowerShell):
#    .\venv\Scripts\Activate.ps1
#    On Windows (CMD):
#    .\venv\Scripts\activate.bat

# (venv) your-computer:my-professional-project$ <-- Your prompt now looks like this

# 4. To check, see which python interpreter you're using. It should point inside your project.
#    On macOS/Linux:
which python
#    On Windows:
#    where python

# 5. When you're done working on the project, deactivate it.
deactivate

# your-computer:my-professional-project$ <-- Prompt returns to normal
Your Mission:

Create a new project folder named api_project.
Inside it, create a virtual environment named .venv.
Activate the environment.
Verify that your system is using the Python interpreter from within the .venv directory.
Deactivate the environment.