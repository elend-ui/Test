"""Validation helpers for application data models."""

import re

from models import Item, User

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_valid_email(email: str) -> bool:
    """Return True if the email has a basic valid format."""
    return bool(_EMAIL_PATTERN.match(email))


def validate_user(user: User) -> None:
    """Validate a User. Raises ValueError if any field is invalid."""
    if user.id <= 0:
        raise ValueError("User id must be positive.")
    if not user.name.strip():
        raise ValueError("User name must not be empty.")
    if user.email is not None and not is_valid_email(user.email):
        raise ValueError("User email is invalid.")


def validate_item(item: Item) -> None:
    """Validate an Item. Raises ValueError if any field is invalid."""
    if item.id <= 0:
        raise ValueError("Item id must be positive.")
    if not item.title.strip():
        raise ValueError("Item title must not be empty.")
    if item.price < 0:
        raise ValueError("Item price must not be negative.")
