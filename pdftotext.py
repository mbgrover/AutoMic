#code source: https://python.plainenglish.io/how-to-read-and-write-pdf-files-using-python-7b930977fe58

# importing module
# (pip install PyPDF2)

import PyPDF2


def doTheThing(fileName, charList):
    # create a pdf file object
    pdfFileObj = open('static/files/' + fileName, 'rb')
    
    # create a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # 2D list for commands: bool[][] commands = [page][character]
    micCommands = []

    # for each page in the pdf
    for i in range(pdfReader.numPages):
        commandRow= [] # new page -> new row of commands, each col is a mic
        for x in range(len(charList)):
            commandRow.append(0)
        # create a list of all of the words on that page
        pageObj = pdfReader.getPage(i)
        words = pageObj.extract_text()
        words = words.split(' ')
        # create a shallow copy of the character list
        pageCharacterList = []
        for character in charList:
            pageCharacterList.append(character)
        for j in words: # for each word on the page
            for k in pageCharacterList: # compare each word with each character
                if k in j: # if the word is a character in the list
                    commandRow[charList.index(k)] = 1
                    pageCharacterList.remove(k)   # remove the name from the shallow list copy
        micCommands.append(commandRow)

    # closing the pdf file object
    pdfFileObj.close()

    micCommands.insert(0, charList)
    return micCommands
