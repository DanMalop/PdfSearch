from models.library import Library
from models.text import TextFile
from utils.tools import regexIgnoreSpaces, deleteNearQuotes
import re

class PdfSearch():
    def __init__(self,keyword: str, scope: int, library: Library):
        self.keyword = keyword.lower()
        self.scope = scope
        self.informList = []
        self.library = library
            
    def getInformList(self) -> list:
        for text in self.library.books:
            inform = self.getInform(text)
            self.informList.append(inform)
        return self.informList

    def getInform(self, text: TextFile) -> dict:
        inform = {}
        inform["title"] = text.title
        inform["author"] = text.author
        inform["content"] = ""
        for page, pageCont in enumerate(text.content):
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