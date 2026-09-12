"""
statistics.py
=============
Statistical analysis functions (mean, average, median, mode, variance, standard deviation)
with validation and error handling.
"""

from typing import Sequence, Union, List
from collections import Counter
import math
from .exceptions import InvalidOperationError

Number = Union[int, float]


def _validate_dataset(data: Sequence[Number]) -> List[Number]:
    """Validate that data is a non-empty sequence of numeric values."""
    if data is None or not hasattr(data, "__iter__"):
        raise InvalidOperationError("Data must be an iterable sequence of numbers (e.g. list, tuple).")
    
    clean_list = list(data)
    if len(clean_list) == 0:
        raise InvalidOperationError("Dataset cannot be empty.")
    
    for idx, item in enumerate(clean_list):
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            raise InvalidOperationError(
                f"Item at index {idx} must be a number (int or float), got {type(item).__name__} ({repr(item)})"
            )
    return clean_list


def mean(data: Sequence[Number]) -> float:
    """
    Calculate the arithmetic mean of a sequence of numbers.

    Raises:
        InvalidOperationError: If the dataset is empty or contains invalid types.

    Example:
        >>> mean([10, 20, 30, 40])
        25.0
    """
    valid_data = _validate_dataset(data)
    return sum(valid_data) / len(valid_data)


# Alias for mean
average = mean


def median(data: Sequence[Number]) -> float:
    """
    Calculate the median (middle value) of a sequence of numbers.

    Example:
        >>> median([1, 3, 5])
        3.0
        >>> median([1, 2, 3, 4])
        2.5
    """
    valid_data = _validate_dataset(data)
    sorted_data = sorted(valid_data)
    n = len(sorted_data)
    mid = n // 2
    
    if n % 2 != 0:
        return float(sorted_data[mid])
    else:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0


def mode(data: Sequence[Number]) -> List[Number]:
    """
    Calculate the mode(s) (most frequent values) of a sequence.
    Returns a list of most common values.

    Example:
        >>> mode([1, 2, 2, 3, 4])
        [2]
        >>> mode([1, 1, 2, 2])
        [1, 2]
    """
    valid_data = _validate_dataset(data)
    counts = Counter(valid_data)
    max_count = max(counts.values())
    
    modes = [val for val, count in counts.items() if count == max_count]
    return sorted(modes)


def variance(data: Sequence[Number], sample: bool = False) -> float:
    """
    Calculate the variance of a dataset.
    
    Args:
        data: Sequence of numbers.
        sample: If True, calculates sample variance (n-1 degrees of freedom),
                otherwise population variance (n degrees of freedom).
    
    Example:
        >>> variance([2, 4, 4, 4, 5, 5, 7, 9])
        4.0
    """
    valid_data = _validate_dataset(data)
    n = len(valid_data)
    
    if sample and n < 2:
        raise InvalidOperationError("Sample variance requires at least 2 data points.")
    
    m = mean(valid_data)
    sum_sq_diff = sum((x - m) ** 2 for x in valid_data)
    divisor = (n - 1) if sample else n
    return sum_sq_diff / divisor


def standard_deviation(data: Sequence[Number], sample: bool = False) -> float:
    """
    Calculate the standard deviation of a dataset.

    Example:
        >>> standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
        2.0
    """
    return math.sqrt(variance(data, sample=sample))
