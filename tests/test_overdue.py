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

    def test_check_overdue_books(self):
        # Simulate overdue by setting borrowed date in the past
        self.borrowed_book.borrowed_date = date.today() - timedelta(days=15)
        overdue_books = self.overdue_manager.check_overdue_books()
        self.assertEqual(len(overdue_books), 1)
        self.assertEqual(overdue_books[0].user.email, self.user.email)

    def test_calculate_fine(self):
        # Simulate overdue by setting borrowed date in the past
        self.borrowed_book.borrowed_date = date.today() - timedelta(days=15)
        fine = self.overdue_manager.calculate_fine(self.user.email, self.book.isbn)
        self.assertEqual(fine, self.overdue_manager.fine_per_day * 1)  # 1 day overdue


if __name__ == '__main__':
    unittest.main()
