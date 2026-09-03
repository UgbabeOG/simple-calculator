"""Simple command-line calculator module.

Provides basic arithmetic operations (addition, subtraction, multiplication,
division) and an interactive REPL-style entry point that lets a user pick an
operation, enter two numbers, and see the result.

This module can be imported for its helper functions or executed directly:

    $ python -m src.calculator
"""

from __future__ import annotations


import utils.transport
import utils.session
def add(first_number: int | float, second_number: int | float) -> int | float:
    """Return the sum of two numbers.

    Args:
        first_number: The left-hand operand.
        second_number: The right-hand operand.

    Returns:
        The arithmetic sum ``first_number + second_number``. The result is
        returned as an ``int`` when both operands are ints (and their sum fits
        in an int) and as a ``float`` otherwise.

    Examples:
        >>> add(2, 3)
        5
        >>> add(1.5, 2.5)
        4.0
    """
    return first_number + second_number


def minus(a: int | float, b: int | float) -> int | float:
    """Return ``a`` minus ``b``.

    Args:
        a: The minuend (the value to subtract from).
        b: The subtrahend (the value to subtract).

    Returns:
        The arithmetic difference ``a - b``.

    Examples:
        >>> minus(10, 3)
        7
        >>> minus(2.5, 0.5)
        2.0
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of two numbers.

    Args:
        a: The left-hand factor.
        b: The right-hand factor.

    Returns:
        The arithmetic product ``a * b``.

    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 2)
        5.0
    """
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """Return ``a`` divided by ``b``.

    Args:
        a: The dividend (numerator).
        b: The divisor (denominator).

    Returns:
        The arithmetic quotient ``a / b`` as a ``float``. Returns ``None`` when
        ``b`` is zero, after printing a user-facing error message.

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        print(f"cannot divide by 0; {b} must be greater than 0")
        return None
    return a / b


def main() -> None:
    """Run the interactive calculator loop.

    Continuously prompts the user to pick an operation (1=add, 2=subtract,
    3=multiply, 4=divide), reads two numeric operands, prints the formatted
    result, and loops until interrupted (Ctrl+C / EOF). Invalid menu choices
    and non-numeric input are handled gracefully without crashing the loop.

    This function performs all I/O via ``print`` and ``input`` and has no
    return value.
    """
    print("--- simple calculator ---")
    while True:
        print("\nselect a number from one (1) to four (4)")
        print("1, Add calculation")
        print("2, Subtract calculation")
        print("3, Multiply calculation")
        print("4, Divide calculation")
        choices = input("Enter your choice. options are [1, 2, 3, 4]: ")
        choices = choices.lower().strip()
        if choices in ("1", "2", "3", "4"):
            try:
                num1 = float(input("enter first number: "))
                num2 = float(input("enter second number: "))
            except ValueError:
                print("enter a valid number")
                continue
            if choices == "1":
                print(f"the value of {num1} + {num2} is :=> {add(num1, num2)}")
            elif choices == "2":
                print(f"{num1} - {num2} = {minus(num1, num2)}")
            elif choices == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choices == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}\n")


if __name__ == "__main__":
    main()