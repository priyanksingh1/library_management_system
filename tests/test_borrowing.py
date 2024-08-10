import unittest
from src.user import UserManager
from src.book import BookManager
from src.borrowing import BorrowingManager
from src.models import Book, User, BorrowedBook

class TestBorrowingManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.book_manager = BookManager()
        self.borrowing_manager = BorrowingManager()

        # Create a user and a book
        self.user = self.user_manager.register_user("John Doe", "john@example.com", "password123")
        self.book = self.book_manager.add_book("12345", "Python 101", "John Doe", 2023)


if __name__ == '__main__':
    unittest.main()