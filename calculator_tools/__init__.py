"""
calculator_tools
================
A reusable Python package providing mathematical, statistical,
and unit conversion utilities with comprehensive error handling.

Package Modules:
    - arithmetic: Basic arithmetic and percentage operations
    - statistics: Summary statistics and data distribution metrics
    - converter: Temperature and unit conversions (length, weight)
    - exceptions: Custom exception definitions (InvalidOperationError)
"""

__version__ = "1.0.0"
__author__ = "Antigravity Team"

# Expose submodules
from . import arithmetic
from . import statistics
from . import converter
from . import exceptions

# Expose custom exception
from .exceptions import InvalidOperationError

# Expose key arithmetic functions at package level
from .arithmetic import (
    add,
    subtract,
    multiply,
    divide,
    power,
    percentage,
    percentage_of,
)

# Expose key statistical functions at package level
from .statistics import (
    mean,
    average,
    median,
    mode,
    variance,
    standard_deviation,
)

# Expose key conversion functions at package level
from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    convert_temperature,
    convert_length,
    convert_weight,
)

__all__ = [
    # Submodules
    "arithmetic",
    "statistics",
    "converter",
    "exceptions",
    # Exceptions
    "InvalidOperationError",
    # Arithmetic
    "add",
    "subtract",
    "multiply",
    "divide",
    "power",
    "percentage",
    "percentage_of",
    # Statistics
    "mean",
    "average",
    "median",
    "mode",
    "variance",
    "standard_deviation",
    # Converter
    "celsius_to_fahrenheit",
    "fahrenheit_to_celsius",
    "celsius_to_kelvin",
    "kelvin_to_celsius",
    "convert_temperature",
    "convert_length",
    "convert_weight",
]
