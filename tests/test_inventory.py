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

    def test_update_on_borrow(self):
        self.borrowing_manager.borrow_book("john@example.com", self.book.isbn)
        self.inventory_manager.update_inventory(self.book.isbn, action="borrow")
        self.assertEqual(self.book.copies, 2)

    def test_update_on_return(self):
        self.borrowing_manager.borrow_book("john@example.com", self.book.isbn)
        self.inventory_manager.update_inventory(self.book.isbn, action="borrow")
        self.inventory_manager.update_inventory(self.book.isbn, action="return")
        self.assertEqual(self.book.copies, 3)


if __name__ == '__main__':
    unittest.main()
