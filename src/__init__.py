from datetime import timedelta
from src.models import BorrowedBook

class BorrowingManager:
    def __init__(self):
        self.borrowed_books = []
        self.renewal_period = timedelta(days=7)

    def borrow_book(self, user_email, book_isbn):
        # Check if the book is available
        book = self._find_book(book_isbn)
        if not book.available:
            raise ValueError("Book is already borrowed or reserved.")

        user = self._find_user(user_email)
        borrowed_book = BorrowedBook(user, book)
        self.borrowed_books.append(borrowed_book)
        book.available = False
        return borrowed_book

    def return_book(self, user_email, book_isbn):
        borrowed_book = self._find_borrowed_book(user_email, book_isbn)
        self.borrowed_books.remove(borrowed_book)
        borrowed_book.book.available = True

