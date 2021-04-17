from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path

files = []
# with open('example.pdf', 'rb') as pdf_file:
#     pdf_reader = PdfFileReader(pdf_file)

#     for i in range(pdf_reader.numPages):
#         output = PdfFileWriter()
#         output.addPage(pdf_reader.getPage(i))
#         with open(f"Page_{i}.pdf", "wb") as the_output:
#             output.write(the_output)
#             files.append(the_output.name)

# print(files)
files = ['Page_0.pdf', 'Page_1.pdf', 'Page_2.pdf',
         'Page_3.pdf', 'Page_4.pdf', 'Page_5.pdf', 'Page_6.pdf']
for file in files:
    print(file)
    # pages = convert_from_path(file, 500)
    # page.save(f"pict_{file}.png", 'PNG')


# for i in range(pdf_reader.numPages):
#     with open(f"Page_{i}.pdf", "wb") as the_output:
