import PyPDF3
import pyttsx3
import pdfplumber

pdf_file = 'oop.pdf'
book = open(pdf_file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages

finalText = ''
with pdfplumber.open(pdf_file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

        engine = pyttsx3.init()
        engine.save_to_file(finalText, 'oop.mp3')
        engine.runAndWait()





