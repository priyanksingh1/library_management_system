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
        self.user = self.user_manager.register_user("abc", "abc@example.com", "password123")
        self.book = self.book_manager.add_book("12345", "Python 101", "abc", 2023)

    def test_borrow_book(self):
        borrowed_book = self.borrowing_manager.borrow_book(self.user.email, self.book.isbn)
        self.assertIsInstance(borrowed_book, BorrowedBook)
        self.assertEqual(borrowed_book.book.isbn, self.book.isbn)
        self.assertEqual(borrowed_book.user.email, self.user.email)
        self.assertFalse(self.book.available)


if __name__ == '__main__':
    unittest.main()