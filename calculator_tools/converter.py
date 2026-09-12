"""
converter.py
============
Temperature and unit conversion functions with input validation and error handling.
"""

from typing import Union
from .exceptions import InvalidOperationError

Number = Union[int, float]


def _validate_number(val: any, param_name: str = "Value") -> Number:
    """Validate that the given value is an int or float, and not a boolean."""
    if isinstance(val, bool) or not isinstance(val, (int, float)):
        raise InvalidOperationError(
            f"{param_name} must be a valid number (int or float), got {type(val).__name__} ({repr(val)})"
        )
    return val


# ---------------------------------------------------------------------------
# Temperature Conversions
# ---------------------------------------------------------------------------

def celsius_to_fahrenheit(celsius: Number) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (C * 9/5) + 32
    """
    _validate_number(celsius, "Celsius temperature")
    if celsius < -273.15:
        raise InvalidOperationError(f"Temperature {celsius} C is below absolute zero (-273.15 C).")
    return (celsius * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(fahrenheit: Number) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (F - 32) * 5/9
    """
    _validate_number(fahrenheit, "Fahrenheit temperature")
    if fahrenheit < -459.67:
        raise InvalidOperationError(f"Temperature {fahrenheit} F is below absolute zero (-459.67 F).")
    return (fahrenheit - 32.0) * 5.0 / 9.0


def celsius_to_kelvin(celsius: Number) -> float:
    """
    Convert temperature from Celsius to Kelvin.
    Formula: C + 273.15
    """
    _validate_number(celsius, "Celsius temperature")
    if celsius < -273.15:
        raise InvalidOperationError(f"Temperature {celsius} C is below absolute zero (-273.15 C).")
    return celsius + 273.15


def kelvin_to_celsius(kelvin: Number) -> float:
    """
    Convert temperature from Kelvin to Celsius.
    Formula: K - 273.15
    """
    _validate_number(kelvin, "Kelvin temperature")
    if kelvin < 0:
        raise InvalidOperationError(f"Temperature {kelvin}K is below absolute zero (0K).")
    return kelvin - 273.15


def convert_temperature(value: Number, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between Celsius ('C'), Fahrenheit ('F'), and Kelvin ('K').

    Raises:
        InvalidOperationError: If unit is unsupported or value violates physical limits.

    Example:
        >>> convert_temperature(100, 'C', 'F')
        212.0
    """
    _validate_number(value, "Temperature value")
    
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise InvalidOperationError("Temperature units must be strings.")
    
    u_from = from_unit.strip().upper()
    u_to = to_unit.strip().upper()
    
    valid_units = {"C", "CELSIUS", "F", "FAHRENHEIT", "K", "KELVIN"}
    if u_from not in valid_units:
        raise InvalidOperationError(f"Unsupported source temperature unit: '{from_unit}'. Valid units: C, F, K.")
    if u_to not in valid_units:
        raise InvalidOperationError(f"Unsupported target temperature unit: '{to_unit}'. Valid units: C, F, K.")

    # Canonicalize unit names
    u_from = u_from[0]
    u_to = u_to[0]
    
    # First convert to Celsius
    if u_from == 'C':
        celsius = celsius_to_kelvin(value) - 273.15  # will check <= -273.15
        celsius = value
        if celsius < -273.15:
            raise InvalidOperationError(f"Temperature {celsius}°C is below absolute zero.")
    elif u_from == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif u_from == 'K':
        celsius = kelvin_to_celsius(value)
    
    # Convert from Celsius to target
    if u_to == 'C':
        return celsius
    elif u_to == 'F':
        return celsius_to_fahrenheit(celsius)
    elif u_to == 'K':
        return celsius_to_kelvin(celsius)


# ---------------------------------------------------------------------------
# Simple Unit Conversions: Length and Mass/Weight
# ---------------------------------------------------------------------------

# Base unit: Meter (m)
LENGTH_CONVERSIONS_TO_METERS = {
    "m": 1.0,
    "meter": 1.0,
    "meters": 1.0,
    "km": 1000.0,
    "kilometer": 1000.0,
    "kilometers": 1000.0,
    "cm": 0.01,
    "centimeter": 0.01,
    "centimeters": 0.01,
    "mm": 0.001,
    "millimeter": 0.001,
    "millimeters": 0.001,
    "mi": 1609.344,
    "mile": 1609.344,
    "miles": 1609.344,
    "yd": 0.9144,
    "yard": 0.9144,
    "yards": 0.9144,
    "ft": 0.3048,
    "foot": 0.3048,
    "feet": 0.3048,
    "in": 0.0254,
    "inch": 0.0254,
    "inches": 0.0254,
}

# Base unit: Kilogram (kg)
WEIGHT_CONVERSIONS_TO_KG = {
    "kg": 1.0,
    "kilogram": 1.0,
    "kilograms": 1.0,
    "g": 0.001,
    "gram": 0.001,
    "grams": 0.001,
    "mg": 0.000001,
    "milligram": 0.000001,
    "milligrams": 0.000001,
    "lb": 0.45359237,
    "lbs": 0.45359237,
    "pound": 0.45359237,
    "pounds": 0.45359237,
    "oz": 0.028349523125,
    "ounce": 0.028349523125,
    "ounces": 0.028349523125,
}


def convert_length(value: Number, from_unit: str, to_unit: str) -> float:
    """
    Convert length between units:
    Supported units: m, km, cm, mm, mi, yd, ft, in.

    Raises:
        InvalidOperationError: For negative length or unsupported unit.

    Example:
        >>> convert_length(5, 'km', 'mi')
        3.1068559611866697
    """
    _validate_number(value, "Length value")
    if value < 0:
        raise InvalidOperationError(f"Length cannot be negative: {value}")
    
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise InvalidOperationError("Unit names must be strings.")
    
    u_from = from_unit.strip().lower()
    u_to = to_unit.strip().lower()
    
    if u_from not in LENGTH_CONVERSIONS_TO_METERS:
        raise InvalidOperationError(
            f"Unsupported length unit: '{from_unit}'. Supported units: {list(LENGTH_CONVERSIONS_TO_METERS.keys())}"
        )
    if u_to not in LENGTH_CONVERSIONS_TO_METERS:
        raise InvalidOperationError(
            f"Unsupported length unit: '{to_unit}'. Supported units: {list(LENGTH_CONVERSIONS_TO_METERS.keys())}"
        )
    
    meters = value * LENGTH_CONVERSIONS_TO_METERS[u_from]
    result = meters / LENGTH_CONVERSIONS_TO_METERS[u_to]
    return result


def convert_weight(value: Number, from_unit: str, to_unit: str) -> float:
    """
    Convert mass/weight between units:
    Supported units: kg, g, mg, lb, oz.

    Raises:
        InvalidOperationError: For negative mass or unsupported unit.

    Example:
        >>> convert_weight(10, 'kg', 'lb')
        22.046226218487757
    """
    _validate_number(value, "Weight value")
    if value < 0:
        raise InvalidOperationError(f"Weight cannot be negative: {value}")
    
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise InvalidOperationError("Unit names must be strings.")
        
    u_from = from_unit.strip().lower()
    u_to = to_unit.strip().lower()
    
    if u_from not in WEIGHT_CONVERSIONS_TO_KG:
        raise InvalidOperationError(
            f"Unsupported weight unit: '{from_unit}'. Supported units: {list(WEIGHT_CONVERSIONS_TO_KG.keys())}"
        )
    if u_to not in WEIGHT_CONVERSIONS_TO_KG:
        raise InvalidOperationError(
            f"Unsupported weight unit: '{to_unit}'. Supported units: {list(WEIGHT_CONVERSIONS_TO_KG.keys())}"
        )
    
    kg = value * WEIGHT_CONVERSIONS_TO_KG[u_from]
    result = kg / WEIGHT_CONVERSIONS_TO_KG[u_to]
    return result
