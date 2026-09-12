"""
exceptions.py
=============
Custom exceptions for the calculator_tools package.
"""


class InvalidOperationError(Exception):
    """
    Exception raised for invalid calculator operations, invalid inputs,
    unsupported operations, or mathematical violations (e.g. division by zero).
    """

    def __init__(self, message: str = "Invalid operation performed."):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"InvalidOperationError: {self.message}"
