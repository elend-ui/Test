"""Validation helpers for application models."""

import re
from models import Item, User

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    """Return True if the email has a basic valid format."""
    return bool(_EMAIL_PATTERN.match(email))


def validate_user(user: User) -> None:
    """Raise ValueError if the user has invalid data."""
    if not user.name.strip():
        raise ValueError("User name must not be empty.")
    if user.email is not None and not is_valid_email(user.email):
        raise ValueError(f"Invalid email: {user.email}")


def validate_item(item: Item) -> None:
    """Raise ValueError if the item has invalid data."""
    if not item.title.strip():
        raise ValueError("Item title must not be empty.")
    if item.price < 0:
        raise ValueError("Item price must not be negative.")
