#code source: https://python.plainenglish.io/how-to-read-and-write-pdf-files-using-python-7b930977fe58

# importing module
# (pip install PyPDF2)

import PyPDF2
 
# create a pdf file object
pdfFileObj = open('file.pdf', 'rb')
 
# create a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# create a list of characters to look for in the PDF (CASE SENSITIVE)
print("Enter the name of the characters in all CAPITAL LETTERS you'd like to be mic'ed followed by pressing ENTER")
print("To stop adding mics, enter 'n'")
characterList=[]
cnt = 1
isAdding = True
while (isAdding):
    name = input()
    if (name == 'n'):
        isAdding = False
        break
    characterList.append(name)
    print("Mic " + str(cnt),": ", name)
    cnt = cnt+1
#characterList.append("LORIN")
#characterList.append("NAN")
#characterList.append("MILES")
#characterList.append("RASHAAD")

# 2D list for commands: bool[][] commands = [page][character]
micCommands = []

# for each page in the pdf
for i in range(pdfReader.numPages):
    commandRow= [] # new page -> new row of commands, each col is a mic
    for x in range(len(characterList)):
        commandRow.append(0);
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
                commandRow[characterList.index(k)] = 1
                pageCharacterList.remove(k)   # remove the name from the shallow list copy
    micCommands.append(commandRow)

# closing the pdf file object
pdfFileObj.close()
print()
print()

for row in micCommands:
    for entry in row:
        print(entry, end=", ")
    print()

import tkinter as tk
from tkinter import ttk
from tkinter import * 


root = Tk()

# This is the section of code which creates the main window
root.geometry('1000x600')
root.configure(background='#F0FFFF')
root.title('Mic Control')

pageNumber = 0

# This is a function which increases the progress bar value by the given increment amount
def makeProgress():
	progessBarOne['value']=progessBarOne['value']+1
	root.update_idletasks()

# This is the section of code which creates a color style to be used with the progress bar
progessBarOne_style = ttk.Style()
progessBarOne_style.theme_use('clam')
progessBarOne_style.configure('progessBarOne.Horizontal.TProgressbar', foreground='#F0F8FF', background='#F0F8FF')


# This is the section of code which creates a progress bar
progessBarOne=ttk.Progressbar(root, style='progessBarOne.Horizontal.TProgressbar', orient='horizontal', length=376, mode='determinate', maximum=1, value=0)
progessBarOne.place(x=372, y=33)

# This is the section of code which creates a button
Button(root, text='Next Page', bg='#F0F8FF', font=('arial', 12, 'normal'), command=makeProgress).place(x=341, y=351)



root.mainloop()