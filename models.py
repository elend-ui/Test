"""Data models for the application."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    """User representation."""

    id: int
    name: str
    email: Optional[str] = None


@dataclass
class Item:
    """Item representation."""

    id: int
    title: str
    price: float
