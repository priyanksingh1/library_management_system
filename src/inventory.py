class InventoryManager:
    def __init__(self):
        self.low_stock_threshold = 2

    def view_inventory(self):
        inventory = {}
        for book in self.book_manager.books.values():
            inventory[book.isbn] = {
                "title": book.title,
                "author": book.author,
                "copies": book.copies,
            }
        return inventory

    def update_inventory(self, isbn, action="borrow"):
        book = self._find_book(isbn)
        if action == "borrow":
            book.decrease_copies()
        elif action == "return":
            book.increase_copies()
        else:
            raise ValueError("Invalid action specified. Use 'borrow' or 'return'.")

    def low_stock_alert(self, isbn):
        book = self._find_book(isbn)
        return book.copies <= self.low_stock_threshold
