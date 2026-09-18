"""Business logic and services."""

from typing import List
from models import Item, User


class UserService:
    """Service for managing users."""

    def __init__(self) -> None:
        self._users: List[User] = []

    def add_user(self, user: User) -> None:
        """Add a new user."""
        self._users.append(user)

    def get_users(self) -> List[User]:
        """Return all users."""
        return list(self._users)
