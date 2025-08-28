"""List tasks across phases and print a small progress summary.

Usage:
    python scripts/list_tasks.py

This script looks for directories starting with "Phase" at the repo root and then
checks for a `tasks/` subfolder. For each file it prints a simple status check.
The status heuristic marks a file as "Likely incomplete" when it contains the
string "TODO" (case-insensitive) or has very few lines. This is intentionally
lightweight — use it as a quick checklist, not a perfect judgment.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

def file_status(path: Path) -> str:
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        return 'Unreadable'
    lower = text.lower()
    if 'todo' in lower:
        return 'Likely incomplete (TODO)'
    # Very short files are often starters
    if len(text.splitlines()) <= 3:
        return 'Likely incomplete (very short)'
    return 'Likely complete'


def main():
    phases = sorted([p for p in ROOT.iterdir() if p.is_dir() and p.name.lower().startswith('phase')])
    if not phases:
        print('No Phase directories found under', ROOT)
        return 1

    total_tasks = 0
    total_complete = 0

    for phase in phases:
        tasks_dir = phase / 'tasks'
        if not tasks_dir.exists() or not tasks_dir.is_dir():
            continue
        files = sorted([p for p in tasks_dir.iterdir() if p.is_file()])
        if not files:
            continue

        print(f'\n{phase.name} — {len(files)} task file(s)')
        phase_complete = 0
        for f in files:
            status = file_status(f)
            mark = '✓' if status == 'Likely complete' else '✗'
            if status == 'Likely complete':
                phase_complete += 1
            print(f'  {mark} {f.relative_to(ROOT)} — {status}')

        total_tasks += len(files)
        total_complete += phase_complete

    print('\nSummary:')
    print(f'  Total task files: {total_tasks}')
    print(f'  Likely complete: {total_complete}')
    print(f'  Likely incomplete: {total_tasks - total_complete}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
