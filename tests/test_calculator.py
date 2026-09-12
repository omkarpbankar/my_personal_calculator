"""
test_calculator.py
==================
Comprehensive test suite for the calculator_tools package.
"""

import unittest
import calculator_tools as calc
from calculator_tools.exceptions import InvalidOperationError
from calculator_tools import arithmetic, statistics, converter


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(arithmetic.add(5, 7), 12)
        self.assertEqual(arithmetic.add(1, 2, 3, 4, 5), 15)
        self.assertEqual(arithmetic.add(-10, 10), 0)

    def test_addition_invalid(self):
        with self.assertRaises(InvalidOperationError):
            arithmetic.add(5)
        with self.assertRaises(InvalidOperationError):
            arithmetic.add("10", 5)
        with self.assertRaises(InvalidOperationError):
            arithmetic.add(True, 5)

    def test_subtraction(self):
        self.assertEqual(arithmetic.subtract(10, 4), 6)
        self.assertEqual(arithmetic.subtract(4, 10), -6)

    def test_subtraction_invalid(self):
        with self.assertRaises(InvalidOperationError):
            arithmetic.subtract("a", 2)

    def test_multiplication(self):
        self.assertEqual(arithmetic.multiply(3, 4), 12)
        self.assertEqual(arithmetic.multiply(2, 3, 4), 24)
        self.assertEqual(arithmetic.multiply(5, 0), 0)

    def test_multiplication_invalid(self):
        with self.assertRaises(InvalidOperationError):
            arithmetic.multiply(3)
        with self.assertRaises(InvalidOperationError):
            arithmetic.multiply(3, None)

    def test_division(self):
        self.assertEqual(arithmetic.divide(10, 2), 5.0)
        self.assertAlmostEqual(arithmetic.divide(10, 3), 3.3333333333333335)

    def test_division_by_zero(self):
        with self.assertRaises(InvalidOperationError) as ctx:
            arithmetic.divide(10, 0)
        self.assertIn("Division by zero", str(ctx.exception))

    def test_power(self):
        self.assertEqual(arithmetic.power(2, 3), 8)
        self.assertEqual(arithmetic.power(9, 0.5), 3.0)

    def test_percentage(self):
        self.assertEqual(arithmetic.percentage(25, 100), 25.0)
        self.assertEqual(arithmetic.percentage(50, 200), 25.0)

    def test_percentage_zero_total(self):
        with self.assertRaises(InvalidOperationError):
            arithmetic.percentage(25, 0)

    def test_percentage_of(self):
        self.assertEqual(arithmetic.percentage_of(20, 150), 30.0)


class TestStatistics(unittest.TestCase):
    def test_mean_and_average(self):
        data = [10, 20, 30, 40]
        self.assertEqual(statistics.mean(data), 25.0)
        self.assertEqual(statistics.average(data), 25.0)

    def test_mean_empty_or_invalid(self):
        with self.assertRaises(InvalidOperationError):
            statistics.mean([])
        with self.assertRaises(InvalidOperationError):
            statistics.mean([1, 2, "three"])
        with self.assertRaises(InvalidOperationError):
            statistics.mean(None)

    def test_median(self):
        self.assertEqual(statistics.median([1, 3, 5]), 3.0)
        self.assertEqual(statistics.median([1, 2, 3, 4]), 2.5)

    def test_mode(self):
        self.assertEqual(statistics.mode([1, 2, 2, 3]), [2])
        self.assertEqual(statistics.mode([1, 1, 2, 2, 3]), [1, 2])

    def test_variance_and_std_dev(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        self.assertEqual(statistics.variance(data, sample=False), 4.0)
        self.assertEqual(statistics.standard_deviation(data, sample=False), 2.0)
        self.assertAlmostEqual(statistics.variance(data, sample=True), 4.571428571428571)


class TestConverter(unittest.TestCase):
    def test_temperature_celsius_fahrenheit(self):
        self.assertEqual(converter.celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(converter.celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(converter.fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(converter.fahrenheit_to_celsius(212), 100.0)

    def test_temperature_kelvin(self):
        self.assertEqual(converter.celsius_to_kelvin(0), 273.15)
        self.assertEqual(converter.kelvin_to_celsius(273.15), 0.0)

    def test_temperature_absolute_zero_violation(self):
        with self.assertRaises(InvalidOperationError):
            converter.celsius_to_kelvin(-300)
        with self.assertRaises(InvalidOperationError):
            converter.kelvin_to_celsius(-1)

    def test_convert_temperature_unified(self):
        self.assertEqual(converter.convert_temperature(100, "C", "F"), 212.0)
        self.assertEqual(converter.convert_temperature(0, "C", "K"), 273.15)
        self.assertEqual(converter.convert_temperature(32, "F", "C"), 0.0)

    def test_convert_temperature_invalid_unit(self):
        with self.assertRaises(InvalidOperationError):
            converter.convert_temperature(100, "Rankine", "F")

    def test_convert_length(self):
        self.assertEqual(converter.convert_length(1, "km", "m"), 1000.0)
        self.assertAlmostEqual(converter.convert_length(1, "mi", "km"), 1.609344)
        self.assertAlmostEqual(converter.convert_length(12, "in", "ft"), 1.0)

    def test_convert_length_invalid(self):
        with self.assertRaises(InvalidOperationError):
            converter.convert_length(-5, "m", "km")
        with self.assertRaises(InvalidOperationError):
            converter.convert_length(5, "lightyears", "km")

    def test_convert_weight(self):
        self.assertEqual(converter.convert_weight(1, "kg", "g"), 1000.0)
        self.assertAlmostEqual(converter.convert_weight(1, "lb", "oz"), 16.0)

    def test_convert_weight_invalid(self):
        with self.assertRaises(InvalidOperationError):
            converter.convert_weight(-10, "kg", "lb")
        with self.assertRaises(InvalidOperationError):
            converter.convert_weight(10, "stone", "kg")


class TestPackageImports(unittest.TestCase):
    def test_top_level_exports(self):
        self.assertTrue(hasattr(calc, "add"))
        self.assertTrue(hasattr(calc, "mean"))
        self.assertTrue(hasattr(calc, "convert_length"))
        self.assertTrue(hasattr(calc, "InvalidOperationError"))
        self.assertEqual(calc.add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
