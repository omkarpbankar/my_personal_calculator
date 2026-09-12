"""
main.py
=======
Demonstration of the `calculator_tools` package.

This script demonstrates:
1. The difference between Functions, Modules, Packages, and Imports.
2. Different styles of Python import statements.
3. Full functionality of arithmetic, statistical, and conversion modules.
4. Custom error handling with InvalidOperationError.
"""

import sys

# ===========================================================================
# DEMONSTRATION OF IMPORT STYLES
# ===========================================================================

# 1. Package Import:
# Imports the whole 'calculator_tools' package namespace (defined by calculator_tools/__init__.py)
import calculator_tools as calc

# 2. Module Import:
# Imports specific modules (individual .py files inside the package directory)
from calculator_tools import arithmetic as arith
from calculator_tools import statistics as stats
from calculator_tools import converter as conv

# 3. Specific Function Imports:
# Directly imports specific functions into local namespace
from calculator_tools.arithmetic import add, divide, percentage, percentage_of
from calculator_tools.statistics import mean, median, mode, standard_deviation
from calculator_tools.converter import convert_temperature, convert_length, convert_weight

# 4. Custom Exception Import:
# Imports our custom exception class to catch domain-specific errors
from calculator_tools.exceptions import InvalidOperationError


def print_banner(title: str):
    """Utility to print styled section headers."""
    print("\n" + "=" * 70)
    print(f" {title.upper()}")
    print("=" * 70)


def print_concept_explanations():
    """Explains core Python packaging concepts."""
    print_banner("Core Python Concepts: Function, Module, Package & Import")
    print("""
 1. FUNCTION:
    - A named, reusable block of executable code that performs a specific task.
    - Example: `def add(a, b): return a + b`
    
 2. MODULE:
    - A single Python file (`.py`) containing related functions, classes, and variables.
    - Example: `arithmetic.py`, `statistics.py`, `converter.py`, `exceptions.py`
    
 3. PACKAGE:
    - A directory containing an `__init__.py` file and one or more modules.
    - It allows hierarchical structuring of modules under a single namespace.
    - Example: `calculator_tools/` folder containing `__init__.py` and submodules.
    
 4. IMPORT:
    - The Python statement used to bind modules, packages, or specific functions
      into the current namespace.
    - Examples:
        * `import calculator_tools`                (Package import)
        * `from calculator_tools import arithmetic` (Module import)
        * `from calculator_tools import add`       (Function import)
        * `from calculator_tools.exceptions import InvalidOperationError` (Exception import)
""")


def demo_arithmetic():
    """Demonstrate basic arithmetic and percentage operations."""
    print_banner("1. Arithmetic & Percentage Operations (arithmetic.py)")

    # Basic arithmetic using package top-level aliases and module functions
    print(f"[*] add(15, 25, 10)                  -> Result: {add(15, 25, 10)}")
    print(f"[*] subtract(100, 37)                -> Result: {arith.subtract(100, 37)}")
    print(f"[*] multiply(4, 5, 2)                -> Result: {arith.multiply(4, 5, 2)}")
    print(f"[*] divide(100, 8)                   -> Result: {divide(100, 8)}")
    print(f"[*] power(2, 10)                     -> Result: {arith.power(2, 10)}")
    
    # Percentage calculations
    print(f"[*] percentage(45, 180) (45 of 180)  -> Result: {percentage(45, 180)}%")
    print(f"[*] percentage_of(15, 250) (15% of 250)-> Result: {percentage_of(15, 250)}")


def demo_statistics():
    """Demonstrate statistics and average calculation operations."""
    print_banner("2. Statistical Operations & Averages (statistics.py)")

    dataset = [12, 15, 12, 18, 22, 15, 12, 30, 25]
    print(f"Dataset: {dataset}\n")

    print(f"[*] mean(dataset) [or average]       -> Result: {mean(dataset):.2f}")
    print(f"[*] median(dataset)                  -> Result: {median(dataset)}")
    print(f"[*] mode(dataset)                    -> Result: {mode(dataset)}")
    print(f"[*] variance(dataset, sample=False)  -> Result: {stats.variance(dataset):.2f}")
    print(f"[*] standard_deviation(dataset)      -> Result: {standard_deviation(dataset):.2f}")


def demo_conversions():
    """Demonstrate temperature and unit conversions."""
    print_banner("3. Temperature & Unit Conversions (converter.py)")

    print("--- Temperature Conversions ---")
    print(f"[*] 100 C to Fahrenheit                -> {conv.celsius_to_fahrenheit(100)} F")
    print(f"[*] 98.6 F to Celsius                 -> {conv.fahrenheit_to_celsius(98.6):.2f} C")
    print(f"[*] 25 C to Kelvin                    -> {conv.celsius_to_kelvin(25)} K")
    print(f"[*] convert_temperature(300, 'K', 'C')-> {convert_temperature(300, 'K', 'C'):.2f} C")

    print("\n--- Length Conversions ---")
    print(f"[*] convert_length(10, 'km', 'mi')   -> {convert_length(10, 'km', 'mi'):.4f} miles")
    print(f"[*] convert_length(100, 'm', 'ft')   -> {convert_length(100, 'm', 'ft'):.2f} feet")
    print(f"[*] convert_length(6, 'ft', 'in')    -> {convert_length(6, 'ft', 'in'):.1f} inches")

    print("\n--- Weight/Mass Conversions ---")
    print(f"[*] convert_weight(5, 'kg', 'lb')    -> {convert_weight(5, 'kg', 'lb'):.4f} lbs")
    print(f"[*] convert_weight(16, 'oz', 'g')    -> {convert_weight(16, 'oz', 'g'):.2f} grams")


def demo_error_handling():
    """Demonstrate how custom InvalidOperationError catches invalid inputs and operations."""
    print_banner("4. Robust Error Handling (InvalidOperationError)")

    test_cases = [
        ("Division by Zero", lambda: divide(50, 0)),
        ("Invalid Data Type (string in arithmetic)", lambda: add(10, "twenty")),
        ("Invalid Data Type (boolean in math)", lambda: arith.multiply(10, True)),
        ("Empty Dataset for Average", lambda: mean([])),
        ("Invalid Data in Dataset", lambda: stats.median([10, 20, None, 40])),
        ("Violating Absolute Zero (-300°C to K)", lambda: conv.celsius_to_kelvin(-300)),
        ("Negative Length Value", lambda: convert_length(-10, "km", "m")),
        ("Unsupported Unit Conversion", lambda: convert_weight(10, "kilograms", "parsecs")),
    ]

    for label, action in test_cases:
        try:
            action()
            print(f"[-] FAILED to catch: {label}")
        except InvalidOperationError as exc:
            print(f"[+] CAUGHT EXPECTED ERROR ({label}):")
            print(f"    --> {exc}\n")


def main():
    """Main execution function."""
    print("\n" + "#" * 70)
    print(f"  CALCULATOR TOOLS PACKAGE DEMONSTRATION  (v{calc.__version__})")
    print("#" * 70)

    print_concept_explanations()
    demo_arithmetic()
    demo_statistics()
    demo_conversions()
    demo_error_handling()

    print_banner("Demonstration Complete")
    print("All modules and functions executed successfully with proper error handling!\n")


if __name__ == "__main__":
    main()
