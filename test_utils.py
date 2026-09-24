"""Unit tests for the utils module."""

import unittest
from utils import add, greet


class TestUtils(unittest.TestCase):
    """Test suite for helper utility functions."""

    def test_greet(self) -> None:
        """Test greet returns formatted greeting message."""
        self.assertEqual(greet("World"), "Hello, World!")
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_add(self) -> None:
        """Test addition of integers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
