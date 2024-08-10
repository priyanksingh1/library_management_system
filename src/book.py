from src.models import Book

class BookManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, published_year):
        if isbn in self.books:
            raise ValueError("Book with this ISBN already exists.")
        book = Book(isbn, title, author, published_year)
        self.books[isbn] = book
        return book
