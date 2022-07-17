[![Python Version](http://img.shields.io/badge/Python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# tdl-warmup-python


## 1. Requirements

- `Python 3.7` (note: support for `Python 2.x` has been dropped)
- `pip` (ensure it supports `Python 3.7`)


## 2. How to start

- Install dependencies `pip install -r requirements.txt`
- Open `lib/send_command_to_server.py`
- Read the comments as documentation, they will guide through the rest of the setup

## 3. Testing

- Run `PYTHONPATH=src python -m pytest -q test/solution_tests/` to run all test

## 4. Linting

- Run `flake8 src/checkout` to check formatting on "checkout" source code
