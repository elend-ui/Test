"""Inventory management for items."""

from typing import Dict, List, Optional

from models import Item


class Inventory:
    """In-memory collection of items keyed by id."""

    def __init__(self) -> None:
        self._items: Dict[int, Item] = {}

    def add_item(self, item: Item) -> None:
        """Add an item. Raises ValueError if the id already exists."""
        if item.id in self._items:
            raise ValueError(f"Item with id {item.id} already exists.")
        self._items[item.id] = item

    def remove_item(self, item_id: int) -> None:
        """Remove an item by id. Raises KeyError if it does not exist."""
        del self._items[item_id]

    def get_item(self, item_id: int) -> Optional[Item]:
        """Return the item with the given id, or None if not found."""
        return self._items.get(item_id)

    def list_items(self) -> List[Item]:
        """Return all items."""
        return list(self._items.values())

    def total_value(self) -> float:
        """Return the sum of all item prices."""
        return sum(item.price for item in self._items.values())
