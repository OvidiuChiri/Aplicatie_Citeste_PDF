import pyttsx3 # is a text-to-speech conversion library in Python
import PyPDF2 # PyPDF2 is an open source pure-python PDF library capable
# of splitting, merging, cropping, and transforming the pages of PDF files.
book = open('oop.pdf', 'rb') # open and read text from a pdf file.
pdfReader = PyPDF2.PdfReader(book) # this is how you read from a pdf book
pages = len(pdfReader.pages)
print(pages)
speaker = pyttsx3.init() # speaker initialization
for num in range(0, pages):
    page = pdfReader.pages[71] # get a page number with pages or numPages.
    text = page.extract_text() # extract the text.
    speaker.setProperty('rate', 200)
    speaker.setProperty('volume', 1)
    speaker.say(text)
    speaker.runAndWait()









