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

    def renew_book(self, user_email, book_isbn):
        borrowed_book = self._find_borrowed_book(user_email, book_isbn)
        borrowed_book.extend_due_date(self.renewal_period.days)
        return borrowed_book

    def reserve_book(self, user_email, book_isbn):
        # Allow reservation only if the book is currently borrowed
        book = self._find_book(book_isbn)
        if book.available:
            raise ValueError("Book is currently available and cannot be reserved.")

        user = self._find_user(user_email)
        reserved_book = BorrowedBook(user, book, borrowed_date=None, due_date=None)
        self.borrowed_books.append(reserved_book)
        return reserved_book

    def find_book(self, isbn):
        for book in self.book_manager.books.values():
            if book.isbn == isbn:
                return book
        raise ValueError("Book not found.")

    def find_user(self, email):
        for user in self.user_manager.users.values():
            if user.email == email:
                return user
        raise ValueError("User not found.")

    def find_borrowed_book(self, user_email, book_isbn):
        for borrowed_book in self.borrowed_books:
            if borrowed_book.user.email == user_email and borrowed_book.book.isbn == book_isbn:
                return borrowed_book
        raise ValueError("Borrowed book not found.")
