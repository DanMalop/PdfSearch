import PyPDF2 as pdf
import os
import re
import utils.tools as tools

def search(folder: str, keyword: str, scope: int) -> list:
    
    keyword = keyword.lower()
    informList = []
    listfiles = os.listdir(folder)

    for filename in listfiles:
        fullName = os.path.splitext(filename)
        inform = {}
        if fullName[1] == ".pdf":    
            with open(os.path.join(folder, filename), 'rb') as f:
                pdfReader = pdf.PdfFileReader(f)
                num_pages = pdfReader.numPages
                pdfInfo = pdfReader.getDocumentInfo()
                
                name = pdfInfo.title if (pdfReader.getDocumentInfo().title != None or pdfReader.getDocumentInfo().title != "UNTITELED") else fullName[0]
                inform["title"] = name
                inform["author"] = pdfInfo.author
                inform["content"] = ""
                        

                for page in range(0, num_pages):
                    pageObj = pdfReader.getPage(page)
                    text = pageObj.extractText()
                    text = text.lower().replace("\n", "").replace("¶", "")
                    #text = text.replace(" ", "") if ignoreSpaces else text

                    reExpression = tools.RegexIgnoreSpaces(keyword)
                    quotesMatchObj = re.finditer(reExpression, text)
                    totalIndexQuotesList = [quote.span() for quote in quotesMatchObj]
                    
                    fragments = ""
                    if totalIndexQuotesList != []:
                        indexQuotesList = tools.deleteNearQuotes(totalIndexQuotesList, scope)

                        for indexQuote in indexQuotesList:
                            fragment = f"<li>{text[indexQuote[0] - scope//2 : indexQuote[1] + scope//2]}</li>"
                            fragments += fragment if len(fragment) > scope//2 else ""
                    
                    if fragments != "":
                        inform["content"] += f"<h5>Page: {page + 1}</h5>" 
                        inform["content"] += "<ul>" 
                        inform["content"] += fragments
                                            
                    inform["content"] += "</ul>" if inform["content"] != "" else ""
                    
        informList.append(inform)

    return informList


#search("C:\\Users\\dd_18\\Documents\\ProyectosW\\web\\PdfSearch-web-app\\backend\\src\\files", "metodología", 400)
