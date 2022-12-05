from PyPDF2 import PdfFileWriter, PdfFileReader


class Document:
    def __init__(self, path):
        self.path = path

    def separatePages(self):
        input_pdf = PdfFileReader(open(f"{self.path}", "rb"))

        for i in range(input_pdf.numPages):
            output = PdfFileWriter()
            output.addPage(input_pdf.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)

    def extractPage(self):
        input_pdf = PdfFileReader(open(f"{self.path}", "rb"))
        page = int(input("Gimme the page to extract: "))
        output = PdfFileWriter()

        output.addPage(input_pdf.getPage(page))
        with open("document-page%s.pdf" % page, "wb") as outputStream:
            output.write(outputStream)
            outputStream.close()


myDocument = Document(input("Gimme the path: "))
myDocument.extractMultiplePages()
