"""Unit tests for the UserService module."""

import unittest
from models import User
from services import UserService


class TestUserService(unittest.TestCase):
    """Test suite for UserService."""

    def test_user_service_initial_empty(self) -> None:
        """Test that UserService initializes with an empty user list."""
        service = UserService()
        self.assertEqual(service.get_users(), [])

    def test_add_and_get_users(self) -> None:
        """Test adding users and retrieving the user list."""
        service = UserService()
        user1 = User(id=1, name="Alice", email="alice@example.com")
        user2 = User(id=2, name="Bob")

        service.add_user(user1)
        service.add_user(user2)

        users = service.get_users()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0], user1)
        self.assertEqual(users[1], user2)


if __name__ == "__main__":
    unittest.main()
