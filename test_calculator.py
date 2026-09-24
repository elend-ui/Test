"""Unit tests for the Calculator module."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test suite for Calculator operations."""

    def test_multiply(self) -> None:
        """Test multiplication functionality."""
        self.assertEqual(Calculator.multiply(2.0, 3.0), 6.0)
        self.assertEqual(Calculator.multiply(-1.0, 5.0), -5.0)
        self.assertEqual(Calculator.multiply(0.0, 10.0), 0.0)

    def test_divide(self) -> None:
        """Test division functionality."""
        self.assertEqual(Calculator.divide(6.0, 2.0), 3.0)
        self.assertEqual(Calculator.divide(-10.0, 2.0), -5.0)

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            Calculator.divide(1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
