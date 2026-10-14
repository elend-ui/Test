"""Unit tests for the validators module."""

import unittest
from models import Item, User
from validators import is_valid_email, validate_item, validate_user


class TestValidators(unittest.TestCase):
    """Test suite for validation helpers."""

    def test_is_valid_email(self) -> None:
        """Test email format checking."""
        self.assertTrue(is_valid_email("alice@example.com"))
        self.assertFalse(is_valid_email("alice@example"))
        self.assertFalse(is_valid_email("alice example.com"))
        self.assertFalse(is_valid_email(""))

    def test_validate_user(self) -> None:
        """Test user validation accepts valid users and rejects invalid ones."""
        validate_user(User(id=1, name="Alice", email="alice@example.com"))
        validate_user(User(id=2, name="Bob"))
        with self.assertRaises(ValueError):
            validate_user(User(id=3, name="  "))
        with self.assertRaises(ValueError):
            validate_user(User(id=4, name="Carol", email="not-an-email"))

    def test_validate_item(self) -> None:
        """Test item validation accepts valid items and rejects invalid ones."""
        validate_item(Item(id=1, title="Widget", price=0.0))
        with self.assertRaises(ValueError):
            validate_item(Item(id=2, title="", price=1.0))
        with self.assertRaises(ValueError):
            validate_item(Item(id=3, title="Gadget", price=-1.0))


if __name__ == "__main__":
    unittest.main()
