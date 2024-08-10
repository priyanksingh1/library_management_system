import unittest
from src.book import BookManager
from src.models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

# method tests if a book can be added successfully.
def test_add_book(self):
    book = self.book_manager.add_book("12345", "Python 101", "John Doe", 2023)
    self.assertIsInstance(book, Book)
    self.assertEqual(book.title, "Python 101")
