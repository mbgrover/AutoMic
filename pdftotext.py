#code source: https://python.plainenglish.io/how-to-read-and-write-pdf-files-using-python-7b930977fe58

# importing module
# (pip install PyPDF2)
import PyPDF2
 
# create a pdf file object
pdfFileObj = open('file.pdf', 'rb')
 
# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
 
# closing the pdf file object
pdfFileObj.close()