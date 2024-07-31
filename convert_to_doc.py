# Import the required modules
from pdf2docx import Converter

# Keeping the PDF's location in a separate variable
pdf_file = r".\Relatório de estágio Lucas Galdino.pdf"

# Maintaining the Document's path in a separate variable
docx_file = r".\Relatório de estágio Lucas Galdino.docx"

# Using the built-in function, convert the PDF file to a document file by saving it in a variable.
cv = Converter(pdf_file)

# Storing the Document in the variable's initialised path
cv.convert(docx_file)

# Conversion closure through the function close()
cv.close()
