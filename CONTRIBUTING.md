# Contributing

Thanks for wanting to contribute! This file describes a small, friendly workflow for adding or improving exercises and solutions in this repository.

Basic workflow

- Fork this repository and clone your fork locally.
- Create a short-lived branch for your change: `git checkout -b feat/phase-1-fix-number-guess`.
- Make focused edits. Keep one logical change per commit.
- Run the repo helper script to list tasks and get a quick status: `python .\\scripts\\list_tasks.py`.
- Push your branch and open a Pull Request against `main` with a short summary of the change.

Where to put your work

- Reference material stays in `Phase X/topics/`.
- Solutions or task work should be saved under `Phase X/tasks/`.
  - You can overwrite the provided starter file (for example `Phase 1/tasks/number_guess.py`), or create a new file with a descriptive name (for example `Phase 1/tasks/number_guess_nishant.py`).

Commit message examples

- `fix(phase-1): correct input validation in number_guess` 
- `chore(docs): add contributing guide`

Pull request description template (short)

- What I changed:
- Why it helps:
- How to test it:

Useful commands (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\activate
where python
python .\scripts\list_tasks.py
```

If you'd like, maintainers can ask you to add a tiny test for the change (Phase 4 covers testing with pytest).

Thank you for contributing — clear, small steps make reviews fast and helpful!
