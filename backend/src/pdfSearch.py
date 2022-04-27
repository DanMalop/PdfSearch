import PyPDF2 as pdf
import os

def search(folder: str, keyword: str, scope: int, ignoreSpaces: bool) -> list:
    
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
                
                name = pdfInfo.title if pdfReader.getDocumentInfo().title != (None | "UNTITLED") else fullName[0]
                inform["title"] = name
                inform["author"] = pdfInfo.author
                inform["content"] = ""
                        

                for page in range(0, num_pages):
                    pageObj = pdfReader.getPage(page)
                    text = pageObj.extractText()
                    text = text.lower().replace("\n", "").replace("¶", "")
                    text = text.replace(" ", "") if ignoreSpaces else text
                    
                    index = text.find(keyword)
                    #print(f"indice: {index} y keyword: {keyword}")
                    fragmets = ""
                    while index >= 0:                        
                        fragment = f"<li>{text[index - scope//2 : index + scope//2]}</li>"
                        text = text[index + scope : :]
                        index = text.find(keyword)
                        fragmets += fragment if len(fragment) > scope//2 else ""
                        
                    if fragmets != "":
                        inform["content"] += f"<h5>Page: {page + 1}</h5>" 
                        inform["content"] += "<ul>" 
                        inform["content"] += fragmets
                                            
                    inform["content"] += "</ul>" if inform["content"] != "" else ""
                    
        informList.append(inform)

    return informList
