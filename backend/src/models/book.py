from models.text import TextFile

class Book(TextFile):
    def __init__(self, fileName, folderPath: str) -> None:
        super().__init__(fileName, folderPath)
        self.type = "Book"
        self.editorial = ""

    def setEditorial(self, editorial: str):
        self.editorial = editorial