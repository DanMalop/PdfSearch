import string

def RegexIgnoreSpaces(keyword: string) -> string:
    regexExpression = "".join([leter + " ?" for leter in keyword])
    return regexExpression
    
def deleteNearQuotes(quotesList: list, scope: int) -> list:
    processedList = [quotesList[0]]
    lastAppend = quotesList[0][0]
    
    for i in range(1, len(quotesList)):
        if quotesList[i][0] - lastAppend > int(scope*0.5):
            processedList.append(quotesList[i])
            lastAppend = quotesList[i][0]

    return processedList
            
        



