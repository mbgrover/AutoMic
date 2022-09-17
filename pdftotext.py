#code source: https://python.plainenglish.io/how-to-read-and-write-pdf-files-using-python-7b930977fe58

# importing module
# (pip install PyPDF2)
import PyPDF2
 
# create a pdf file object
pdfFileObj = open('file.pdf', 'rb')
 
# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

characterList = []
characterList.append("LORIN")
characterList.append("NAN")
characterList.append("MILES")
characterList.append("RASHAAD")
 
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    words = pageObj.extract_text()
    words = words.split(' ');
    print()
    print()
    print(i)
    pageCharacterList = []
    for character in characterList:
        pageCharacterList.append(character)
    for j in words:
        for k in pageCharacterList:
            if k in j:
                print(k)
                pageCharacterList.remove(k)

# closing the pdf file object
pdfFileObj.close()