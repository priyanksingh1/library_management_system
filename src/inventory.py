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

