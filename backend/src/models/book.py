import os
import PyPDF2 as pdf

class Book():
    def __init__(self, fileName, folderPath: str) -> None:
        self.folderPath = folderPath
        self.fileName = fileName
        fullName = os.path.splitext(self.fileName)
        self.name = fullName[0]
        self.extension = fullName[1]
        try:
            assert(self.extension == ".pdf")
        except TypeError:
            print(f"The extension ${self.extension} is not compatible")

        self.title = ""
        self.author = ""
        self.numPages = 0
        self.content = []

        with open(os.path.join(self.folderPath, self.fileName), 'rb') as f:
            pdfReader = pdf.PdfFileReader(f)
            self.numPages = pdfReader.numPages
            pdfInfo = pdfReader.getDocumentInfo()
            self.title = pdfInfo.title if (pdfReader.getDocumentInfo().title != None or pdfReader.getDocumentInfo().title != "UNTITELED") else self.name
            self.author = pdfInfo.author

            for page in range(0, self.numPages):
                pageObj = pdfReader.getPage(page)
                self.content.append(pageObj.extractText())

    def setTitle(self, title):
        self.title = title

