import os
from models.book import Book

class Library:
    def __init__(self, folderPath: str) -> None:
        self.books = []
        self.folderPath = folderPath
        for filename in os.listdir(self.folderPath):
            book =Book(filename, folderPath)
            self.books.append(book)
