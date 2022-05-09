from models.library import Library
from models.book import Book
from utils.tools import regexIgnoreSpaces, deleteNearQuotes
import re

class PdfSearch():
    def __init__(self,keyword: str, scope: int, library: Library):
        self.keyword = keyword.lower()
        self.scope = scope
        self.informList = []
        self.library = library
            
    def getInformList(self) -> list:
        for book in self.library.books:
            inform = self.getInform(book)
            self.informList.append(inform)
        return self.informList

    def getInform(self,book: Book) -> dict:
        inform = {}
        inform["title"] = book.title
        inform["author"] = book.author
        inform["content"] = ""
        for page, pageCont in enumerate(book.content):
            text = pageCont.lower().replace("\n", "").replace("¶", "")
            reExpression = regexIgnoreSpaces(self.keyword)
            quotesMatchObj = re.finditer(reExpression, text)
            totalIndexQuotesList = [quote.span() for quote in quotesMatchObj]

            fragments = ""
            if totalIndexQuotesList != []:
                indexQuotesList = deleteNearQuotes(totalIndexQuotesList, self.scope)

                for indexQuote in indexQuotesList:
                    fragment = f"<li>{text[indexQuote[0] - self.scope//2 : indexQuote[1] + self.scope//2]}</li>"
                    fragments += fragment if len(fragment) > self.scope//2 else ""

            if fragments != "":
                inform["content"] += f"<h5>Page: {page + 1}</h5>" 
                inform["content"] += "<ul>" 
                inform["content"] += fragments
                                            
            inform["content"] += "</ul>" if inform["content"] != "" else "" 

        return inform