import os
from models.text import TextFile

class Library:
    def __init__(self, folderPath: str) -> None:
        self.books = []
        self.folderPath = folderPath
        for filename in os.listdir(self.folderPath):
            book =TextFile(filename, folderPath)
            self.books.append(book)