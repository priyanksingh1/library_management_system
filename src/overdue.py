from datetime import date

class OverdueManager:
    def __init__(self):
        self.fine_per_day = 10

    def check_overdue_books(self):
        overdue_books = []
        for borrowed_book in self.borrowing_manager.borrowed_books:
            if borrowed_book.due_date < date.today():
                overdue_books.append(borrowed_book)
        return overdue_books

    def calculate_fine(self, user_email, book_isbn):
        borrowed_book = self.borrowing_manager._find_borrowed_book(user_email, book_isbn)
        if borrowed_book.due_date >= date.today():
            return 0
        overdue_days = (date.today() - borrowed_book.due_date).days
        return overdue_days * self.fine_per_day