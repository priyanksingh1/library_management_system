from datetime import timedelta
from src.models import BorrowedBook

class BorrowingManager:
    def __init__(self):
        self.borrowed_books = []
        self.renewal_period = timedelta(days=7)

