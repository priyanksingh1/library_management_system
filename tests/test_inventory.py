import unittest
from src.user import UserManager
from src.book import BookManager
from src.borrowing import BorrowingManager
from src.inventory import InventoryManager
from src.models import Book

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()
        self.inventory_manager = InventoryManager()
        self.borrowing_manager = BorrowingManager()

        # Add a book to the library
        self.book = self.book_manager.add_book("12345", "Python 101", "abc", 2023, copies=3)