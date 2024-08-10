import unittest
from src.book import BookManager
from src.models import Book

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.book_manager = BookManager()

#