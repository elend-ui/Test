"""Unit tests for the validators module."""

import unittest
from models import Item, User
from validators import is_valid_email, validate_item, validate_user


class TestValidators(unittest.TestCase):
    """Test suite for validation helpers."""

    def test_is_valid_email(self) -> None:
        """Test email format validation."""
        self.assertTrue(is_valid_email("alice@example.com"))
        self.assertFalse(is_valid_email("alice@example"))
        self.assertFalse(is_valid_email("alice example.com"))
        self.assertFalse(is_valid_email(""))

    def test_validate_user_valid(self) -> None:
        """Test that valid users pass validation."""
        validate_user(User(id=1, name="Alice", email="alice@example.com"))
        validate_user(User(id=2, name="Bob"))

    def test_validate_user_invalid(self) -> None:
        """Test that invalid users raise ValueError."""
        with self.assertRaises(ValueError):
            validate_user(User(id=0, name="Alice"))
        with self.assertRaises(ValueError):
            validate_user(User(id=1, name="  "))
        with self.assertRaises(ValueError):
            validate_user(User(id=1, name="Alice", email="not-an-email"))

    def test_validate_item_valid(self) -> None:
        """Test that valid items pass validation."""
        validate_item(Item(id=1, title="Widget", price=19.99))
        validate_item(Item(id=2, title="Freebie", price=0.0))

    def test_validate_item_invalid(self) -> None:
        """Test that invalid items raise ValueError."""
        with self.assertRaises(ValueError):
            validate_item(Item(id=-1, title="Widget", price=1.0))
        with self.assertRaises(ValueError):
            validate_item(Item(id=1, title="", price=1.0))
        with self.assertRaises(ValueError):
            validate_item(Item(id=1, title="Widget", price=-5.0))


if __name__ == "__main__":
    unittest.main()
