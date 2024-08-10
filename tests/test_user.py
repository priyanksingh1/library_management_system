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

# Ensures that attempting to register a user with an existing email raises a 'ValueError'.
    def test_duplicate_email(self):
        self.user_manager.register_user("abc", "abc@example.com", "password123")
        with self.assertRaises(ValueError):
            self.user_manager.register_user("abc", "abc@example.com", "password456")

# Tests if a user can log in with correct credentials.
    def test_user_authentication(self):
        self.user_manager.register_user("abc", "abc@example.com", "password123")
        user = self.user_manager.authenticate_user("abc@example.com", "password123")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "abc")

#  Ensures that invalid credentials raise a 'ValueError'.
    def test_invalid_credentials(self):
        self.user_manager.register_user("abc", "abc@example.com", "password123")
        with self.assertRaises(ValueError):
            self.user_manager.authenticate_user("abc@example.com", "wrongpassword")

# Verifies that users can be assigned roles other than the default "user".
    def test_role_based_access(self):
        user = self.user_manager.register_user("Admin User", "admin@example.com", "adminpass", role="admin")
        self.assertEqual(user.role, "admin")

if __name__ == '__main__':
    unittest.main()