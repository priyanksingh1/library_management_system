import unittest
from src.book import BookManager
from src.models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

# method tests if a book can be added successfully.
def test_add_book(self):
    book = self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    self.assertIsInstance(book, Book)
    self.assertEqual(book.title, "Python 101")

# method tests the handling of duplicates. It adds a book and then tries to add the same book again, expecting a ValueError to be raised.
def test_add_duplicate_book(self):
    self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    with self.assertRaises(ValueError):
        self.book_manager.add_book("12345", "Python 101", "abc", 2023)
