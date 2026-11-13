# log-level-counter

A small Python tool that counts INFO, WARN, and ERROR lines in a log file, with pytest tests.

## What it does

`count_levels(path)` reads a log file and returns a dictionary of counts per level. Blank lines are skipped and unrecognized levels are ignored.

## Why I built it

Log triage starts with knowing what kind of problems a log contains. I built this to practice that in Python, with tests that cover edge cases like blank lines.

## Run it

    python3 count_levels.py

## Run the tests

    python3 -m venv .venv
    source .venv/bin/activate
    pip install pytest
    pytest -v

## What I learned

- A blank line in a log crashed my first version with an IndexError. I wrote a test that reproduces it, and confirmed the test fails when the fix is removed.
- A test that has never failed proves very little. I broke the function on purpose to check that my test would catch the bug.
