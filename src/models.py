class User:
    def __init__(self, name, email, password, role="user"):
        self.name = name
        self.email = email
        self.password = password  # In real applications, never store plain text passwords!
        self.role = role

    def check_password(self, password):
        return self.password == password

class Book:
    def __init__(self, isbn, title, author, published_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.published_year = published_year

from datetime import date, timedelta

class BorrowedBook:
    def __init__(self, user, book, borrowed_date=None, due_date=None):
        self.user = user
        self.book = book
        self.borrowed_date = borrowed_date or date.today()
        self.due_date = due_date or (self.borrowed_date + timedelta(days=14))  # Default 2-week borrowing period

    def extend_due_date(self, days):
        self.due_date += timedelta(days=days)
