from PyPDF2 import PdfFileWriter, PdfFileReader

with open("10_11_merged.pdf", "rb") as in_f:
    input1 = PdfFileReader(in_f)
    output = PdfFileWriter()

    numPages = input1.getNumPages()
    print("document has %s pages." % numPages)

    for i in range(numPages):
        page = input1.getPage(i)
        print(page.mediaBox.getUpperRight_x(), page.mediaBox.getUpperRight_y())
        page.cropBox.lowerLeft = (80, 70)
        page.cropBox.upperRight = (550, 700)
        output.addPage(page)

    with open("out10.pdf", "wb") as out_f:
        output.write(out_f)