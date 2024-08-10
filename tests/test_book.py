import unittest
from src.book import BookManager
from src.models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

# method tests if a book can be added successfully.
def test_add_book(self):
    book = self.book_manager.add_book("12321", "Python 103", "pqr", 2023)
    self.assertIsInstance(book, Book)
    self.assertEqual(book.title, "Python 103")

# method tests the handling of duplicates. It adds a book and then tries to add the same book again, expecting a ValueError to be raised.
def test_add_duplicate_book(self):
    self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    with self.assertRaises(ValueError):
        self.book_manager.add_book("12345", "Python 101", "abc", 2023)

# This method verifies that an existing book can be edited. It checks that the title is updated correctly.
def test_edit_book(self):
    self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    updated_book = self.book_manager.edit_book("12345", title="Advanced Python")
    self.assertEqual(updated_book.title, "Advanced Python")

# After deletion this method attempts to retrieve the book and expects a 'ValueError'
def test_delete_book(self):
    self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    self.book_manager.delete_book("12345")
    with self.assertRaises(ValueError):
        self.book_manager.get_book("12345")

# This method checks if the search functionality works correctly
def test_search_books(self):
    self.book_manager.add_book("12345", "Python 101", "abc", 2023)
    self.book_manager.add_book("67890", "Learning JavaScript", "xyz", 2021)
    results = self.book_manager.search_books("Python")
    self.assertEqual(len(results), 1)
    self.assertEqual(results[0].title, "Python 101")

if __name__ == '__main__':
    unittest.main()

