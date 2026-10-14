"""Business logic for managing items."""

from typing import List, Optional
from models import Item


class ItemService:
    """Service for managing items."""

    def __init__(self) -> None:
        self._items: List[Item] = []

    def add_item(self, item: Item) -> None:
        """Add a new item."""
        self._items.append(item)

    def get_items(self) -> List[Item]:
        """Return all items."""
        return list(self._items)

    def get_item(self, item_id: int) -> Optional[Item]:
        """Return the item with the given id, or None if not found."""
        for item in self._items:
            if item.id == item_id:
                return item
        return None

    def total_price(self) -> float:
        """Return the sum of all item prices."""
        return sum(item.price for item in self._items)
