"""Unit tests for the ItemService module."""

import unittest
from item_service import ItemService
from models import Item


class TestItemService(unittest.TestCase):
    """Test suite for ItemService."""

    def test_item_service_initial_empty(self) -> None:
        """Test that ItemService initializes with an empty item list."""
        service = ItemService()
        self.assertEqual(service.get_items(), [])
        self.assertEqual(service.total_price(), 0)

    def test_add_and_get_items(self) -> None:
        """Test adding items and retrieving them."""
        service = ItemService()
        item1 = Item(id=1, title="Widget", price=19.99)
        item2 = Item(id=2, title="Gadget", price=5.01)

        service.add_item(item1)
        service.add_item(item2)

        self.assertEqual(service.get_items(), [item1, item2])
        self.assertEqual(service.get_item(2), item2)
        self.assertIsNone(service.get_item(99))
        self.assertAlmostEqual(service.total_price(), 25.0)


if __name__ == "__main__":
    unittest.main()
