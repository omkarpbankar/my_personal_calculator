"""
arithmetic.py
=============
Basic arithmetic and percentage operations with input validation and error handling.
"""

from typing import Union, Sequence
from .exceptions import InvalidOperationError

Number = Union[int, float]


def _validate_number(val: any, param_name: str = "Argument") -> Number:
    """Validate that the given value is an int or float, and not a boolean."""
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise InvalidOperationError(
            f"{param_name} must be a valid number (int or float), got {type(val).__name__} ({repr(val)})"
        )
    return val


def add(*numbers: Number) -> Number:
    """
    Add two or more numbers.

    Example:
        >>> add(10, 5)
        15
        >>> add(1, 2, 3, 4)
        10
    """
    if len(numbers) < 2:
        raise InvalidOperationError("Addition requires at least 2 numbers.")
    
    total = 0
    for idx, num in enumerate(numbers):
        _validate_number(num, f"Argument {idx + 1}")
        total += num
    return total


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract b from a (a - b).

    Example:
        >>> subtract(10, 4)
        6
    """
    _validate_number(a, "First argument (a)")
    _validate_number(b, "Second argument (b)")
    return a - b


def multiply(*numbers: Number) -> Number:
    """
    Multiply two or more numbers.

    Example:
        >>> multiply(3, 4)
        12
        >>> multiply(2, 3, 4)
        24
    """
    if len(numbers) < 2:
        raise InvalidOperationError("Multiplication requires at least 2 numbers.")
    
    result = 1
    for idx, num in enumerate(numbers):
        _validate_number(num, f"Argument {idx + 1}")
        result *= num
    return result


def divide(a: Number, b: Number) -> float:
    """
    Divide a by b (a / b).
    
    Raises:
        InvalidOperationError: If b == 0 or if inputs are not numeric.

    Example:
        >>> divide(20, 4)
        5.0
    """
    _validate_number(a, "Numerator (a)")
    _validate_number(b, "Denominator (b)")
    
    if b == 0:
        raise InvalidOperationError("Division by zero is not allowed.")
    
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """
    Calculate base raised to the power of exponent (base ** exponent).

    Example:
        >>> power(2, 3)
        8
    """
    _validate_number(base, "Base")
    _validate_number(exponent, "Exponent")
    
    try:
        result = base ** exponent
        if isinstance(result, complex):
            raise InvalidOperationError("Negative base with non-integer power resulted in complex number.")
        return result
    except OverflowError as exc:
        raise InvalidOperationError(f"Calculation overflow: {exc}")


def percentage(part: Number, total: Number) -> float:
    """
    Calculate what percentage 'part' is of 'total'.
    Formula: (part / total) * 100

    Raises:
        InvalidOperationError: If total is 0.

    Example:
        >>> percentage(25, 100)
        25.0
        >>> percentage(50, 200)
        25.0
    """
    _validate_number(part, "Part")
    _validate_number(total, "Total")
    
    if total == 0:
        raise InvalidOperationError("Total cannot be zero when calculating percentage.")
    
    return (part / total) * 100.0


def percentage_of(percent: Number, total: Number) -> float:
    """
    Calculate 'percent'% of 'total'.
    Formula: (percent / 100) * total

    Example:
        >>> percentage_of(20, 150)
        30.0
    """
    _validate_number(percent, "Percent")
    _validate_number(total, "Total")
    
    return (percent / 100.0) * total
