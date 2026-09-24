"""Unit tests for data models."""

import unittest
from models import Item, User


class TestModels(unittest.TestCase):
    """Test suite for data models."""

    def test_user_creation(self) -> None:
        """Test creating User instance with and without optional email."""
        user = User(id=1, name="Alice", email="alice@example.com")
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

        user_no_email = User(id=2, name="Bob")
        self.assertIsNone(user_no_email.email)

    def test_item_creation(self) -> None:
        """Test creating Item instance."""
        item = Item(id=1, title="Widget", price=19.99)
        self.assertEqual(item.id, 1)
        self.assertEqual(item.title, "Widget")
        self.assertEqual(item.price, 19.99)


if __name__ == "__main__":
    unittest.main()
