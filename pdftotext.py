#code source: https://python.plainenglish.io/how-to-read-and-write-pdf-files-using-python-7b930977fe58

# importing module
# (pip install PyPDF2)
import PyPDF2
 
# create a pdf file object
pdfFileObj = open('file.pdf', 'rb')
 
# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# create a list of characters to look for in the PDF (CASE SENSITIVE)
characterList = []
characterList.append("LORIN")
characterList.append("NAN")
characterList.append("MILES")
characterList.append("RASHAAD")

# for each page in the pdf
for i in range(pdfReader.numPages):
    # create a list of all of the words on that page
    pageObj = pdfReader.getPage(i)
    words = pageObj.extract_text()
    words = words.split(' ');
    # print the page number
    print()
    print()
    print(i)
    # create a shallow copy of the character list
    pageCharacterList = []
    for character in characterList:
        pageCharacterList.append(character)
    for j in words: # for each word on the page
        for k in pageCharacterList: # compare each word with each character
            if k in j: # if the word is a character in the list
                print(k)    # print the character name
                pageCharacterList.remove(k)   # remove the name from the shallow list copy

# closing the pdf file object
pdfFileObj.close()