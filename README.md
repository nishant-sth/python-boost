# Python Boost — Hands-on Python Skills Repository

A curated, exercise-driven collection of Python learning materials and small projects organized by phased topics (variables, functions, OOP, testing, packaging, etc.). This repository is designed so others can fork it, reproduce the learning environment, run examples, and contribute improvements.

---

## Who this is for
- Beginners and intermediate Python developers who want a practical, structured path.
- Instructors who want ready-made exercises.
- Contributors who want to add exercises, tests, or tooling.

---

## Repository overview
Top-level folders group content by Phase and Topic, e.g.:

- Phase 1: basics (variables, functions, data structures)
- Phase 2: OOP, modules, error handling
- Phase 3: generators, decorators, context managers
- Phase 4: virtual environments, package management, testing

(See the repo tree for exact filenames and topic Markdown files.)

---

## Quickstart (fork -> run)
1. Fork the repo on GitHub and clone your fork:
   - git clone https://github.com/<your-username>/<repo>.git

2. Change into the project directory:
   - cd python-boost

3. Create and activate a virtual environment (recommended name: .venv)

   PowerShell (Windows):
   - python -m venv .venv
   - .\.venv\Scripts\Activate.ps1

   CMD (Windows):
   - python -m venv .venv
   - .\.venv\Scripts\activate.bat

   macOS / Linux (bash/zsh):
   - python3 -m venv .venv
   - source .venv/bin/activate

4. Verify the interpreter points inside `.venv`:
   - PowerShell/CMD: where python
   - macOS/Linux: which python

5. Install dependencies (if a requirements.txt exists):

## Working with topic tasks

This repository is organized by phases and topics. Many topics include one or more exercises (task files) that you should complete and save in the corresponding `tasks/` folder for that phase. Working inside the `tasks/` folders helps you follow the curriculum, keep your solutions organized, and practice best practices.

How to use the tasks:
- Locate the tasks for a phase in `Phase X/tasks/` (for example, see `Phase 1/tasks/`).
- Open the task file (for example `Phase 1/tasks/number_guess.py`) and implement or edit the script to complete the exercise.
- Save your solution back into the same `tasks/` folder. You can overwrite the example file or create a new file using a clear name like `number_guess_nishant.py`.
- Commit your changes frequently and keep one commit per focused change when possible.

Example (Phase 1):
- The `Phase 1/tasks/` folder already contains starter scripts such as `number_guess.py`, `student_grades.py`, and `password_validation.py`.
- Complete the task by editing the file and then run it with Python (PowerShell example):

```powershell
python .\Phase 1\tasks\number_guess.py
python .\Phase 1\tasks\student_grades.py
```

Tips and best practices:
- Use a virtual environment before running or installing packages.
- Keep topic source files in `Phase X/topics/` (reference material) and your solutions in `Phase X/tasks/`.
- Add tests or small assertions for functions where appropriate (Phase 4 focuses on testing with pytest).
- Follow simple naming: readable filenames, descriptive variable names, and small functions.

If you'd like, I can also:
- Add a CONTRIBUTING.md with recommended workflow and commit examples.
- Create a short script that lists all task files across phases so you can track progress.
   - pip install -r requirements.txt

   To install common tooling used in the exercises:
   - pip install pytest ruff requests faker

6. Run tests:
   - pytest

7. Format & lint:
   - ruff format .
   - ruff check .

---

## Recommended development workflow
- Create a topic branch: git checkout -b feature/your-change
- Run tests locally: pytest
- Run formatter and linter: ruff format . && ruff check .
- Commit with a clear message and open a PR to the upstream repository.

Commit message template:
- feat(topic): short description
- fix(topic): short description
- docs: update README or topic content

---

## Testing
- Many topics include pytest examples and small test files (e.g., for validators).
- To run all tests: pytest
- To run a single file: pytest path/to/test_file.py

---

## Virtual environments & dependency management
- Always use a venv per project.
- Use `pip freeze > requirements.txt` to capture exact package versions.
- Recreate an environment with `pip install -r requirements.txt`.

---

## Code quality
- Formatting: use ruff (or black if preferred).
  - ruff format .
- Static analysis / linting: ruff check .
- Add editor integrations (VS Code, PyCharm) for autoformat on save.

---

## Example: Create an api_project and run tests
1. mkdir api_project && cd api_project
2. python -m venv .venv
3. Activate .venv
4. pip install pytest
5. Add validators.py and test_validators.py (see Phase 4 topics)
6. Run pytest

---

## Project structure (example)
- Phase 1/
  - veriables-data-types.py
  - functions.py
  - data-structures.py
  - ...
- Phase 2/
  - Modules and Packages.md
  - Inheritance.md
  - ...
- Phase 3/
  - Decorators.md
  - Generators.md
  - ...
- Phase 4/
  - Virtual Environments (The Clean Room).md
  - Testing with pytest (The Safety Net).md
  - Package Management (The Bill of Materials).md

---

## Contributing
- Fork the repo
- Create a branch for your change
- Keep changes small and focused
- Add or update tests where applicable
- Run the formatter and linter before submitting a PR
- Write an informative PR description and reference relevant issue(s)

---

## License
This repository is best published with a permissive license such as the MIT License. Add `LICENSE` to the repository root if you want to allow reuse and contributions easily.

---

## Code of Conduct
Be respectful and constructive. Open-source communities thrive on kindness and clarity. If you are contributing exercises or corrections, keep language neutral and inclusive.

---

## Contact / Maintainers
- Prefer issues and pull requests for discussion.
- For private contact, add your preferred method (email or handle) to the repo settings or CONTRIBUTING.md.

---

Enjoy learning and teaching Python — contributions welcome!
