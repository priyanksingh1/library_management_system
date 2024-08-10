import unittest
from datetime import date, timedelta
from src.user import UserManager
from src.book import BookManager
from src.borrowing import BorrowingManager
from src.overdue import OverdueManager

class TestOverdueManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()
        self.book_manager = BookManager()
        self.borrowing_manager = BorrowingManager()
        self.overdue_manager = OverdueManager()

        self.user = self.user_manager.register_user("abc", "abc@example.com", "password123")
        self.book = self.book_manager.add_book("12345", "Python 101", "abc", 2023)
        self.borrowed_book = self.borrowing_manager.borrow_book(self.user.email, self.book.isbn)
