from telnetlib import DO
from models.text import TextFile

class Paper(TextFile):
    def __init__(self, fileName, folderPath: str) -> None:
        super().__init__(fileName, folderPath)
        self.type = "Scientific paper"
        self.repoSource = ""
        self.DOI = ""
    
    def setRepoSource(self, repository: str):
        self.repoSource = repository
    
    def setDOI(self, DOI: str):
        self.DOI = DOI