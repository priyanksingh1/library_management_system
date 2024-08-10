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

    def edit_book(self, isbn, title=None, author=None, published_year=None):
        book = self.get_book(isbn)
        if title:
            book.title = title
        if author:
            book.author = author
        if published_year:
            book.published_year = published_year
        return book

    def delete_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        del self.books[isbn]

    def get_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not found.")
        return self.books[isbn]

