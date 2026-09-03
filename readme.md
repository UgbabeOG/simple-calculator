# Simple Calculator

A tiny, dependency-free, command-line calculator written in Python. It
exposes four basic arithmetic helpers (`add`, `minus`, `multiply`, `divide`)
and ships with an interactive REPL-style entry point so you can perform
calculations from your terminal.

## Features

- **Addition**, **subtraction**, **multiplication**, and **division** of
  integers or floats.
- **Interactive CLI**: pick an operation from a numbered menu, enter two
  numbers, and read the formatted result.
- **Input validation**: non-numeric input prints a friendly error and
  re-prompts instead of crashing.
- **Safe division**: dividing by zero is caught and reported instead of
  raising an exception.
- **Zero runtime dependencies** — pure Python 3 standard library only.
- **Importable**: the arithmetic helpers can be reused from your own code.

## Requirements

- Python **3.10+** (uses PEP 604 union syntax, e.g. `int | float`).

No third-party packages are required.

## Installation

Clone the repository and (optionally) create a virtual environment:

```bash
git clone <your-repo-url> simple-calculator
cd simple-calculator
python3 -m venv .venv
source .venv/bin/activate
```

## Usage

Run the interactive calculator:

```bash
python src/calculator.py
```

You will see a menu like this:

```
--- simple calculator ---

select a number from one (1) to four (4)
1, Add calculation
2, Subtract calculation
3, Multiply calculation
4, Divide calculation
Enter your choice. options are [1, 2, 3, 4]:
```

Follow the prompts, for example:

```
Enter your choice. options are [1, 2, 3, 4]: 1
enter first number: 12
enter second number: 8
the value of 12.0 + 8.0 is :=> 20.0
```

Press `Ctrl+C` to exit the loop.

### Using the helpers from your own code

The functions in `src/calculator.py` are plain, importable helpers:

```python
from src.calculator import add, minus, multiply, divide

add(2, 3)        # 5
minus(10, 4)     # 6
multiply(7, 6)   # 42
divide(9, 2)     # 4.5
divide(1, 0)     # prints "cannot divide by 0; 0 must be greater than 0" and returns None
```

> Note: depending on how you run your code, you may prefer
> `from calculator import add, minus, multiply, divide` after adding `src/`
> to `sys.path` or running the file as a module.

## Project Structure

```
simple-calculator/
├── .gitignore
├── LICENSE
├── readme.md
└── src/
    └── calculator.py
```

## API Reference

### `add(first_number, second_number)`
Returns the sum of two numbers (`int | float`).

### `minus(a, b)`
Returns `a - b`.

### `multiply(a, b)`
Returns `a * b`.

### `divide(a, b)`
Returns `a / b` as a float. Returns `None` (after printing a warning) when
`b` is zero.

### `main()`
Runs the interactive CLI loop. Has no return value.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-change`.
3. Make your changes and ensure the module still runs end-to-end:
   `python src/calculator.py`.
4. Submit a pull request describing your change.

## License

This project is licensed under the terms of the [MIT License](LICENSE).