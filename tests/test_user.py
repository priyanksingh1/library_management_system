import unittest
from src.user import UserManager
from src.models import User

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

# Tests if a user can be registered successfully.
    def test_register_user(self):
        user = self.user_manager.register_user("abc", "abc@example.com", "password123")
        self.assertIsInstance(user, User)
        self.assertEqual(user.name, "abc")
        self.assertEqual(user.email, "abc@example.com")
