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
        self.book = self.book_manager.add_book("12345", "Python 101", "abc", 2023, copies=3)

    def test_view_inventory(self):
        inventory = self.inventory_manager.view_inventory()
        self.assertIn(self.book.isbn, inventory)
        self.assertEqual(inventory[self.book.isbn]['title'], "Python 101")
        self.assertEqual(inventory[self.book.isbn]['copies'], 3)

