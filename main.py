from PyPDF2 import PdfFileWriter, PdfFileReader

user_input = input("Enter pdf file address: ")
input_pdf = PdfFileReader(open(f"{user_input}.pdf", "rb"))

for i in range(input_pdf.numPages):
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)

print(f"Done!\n")
