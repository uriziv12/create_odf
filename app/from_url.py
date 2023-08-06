import pdfkit
# NOTE: you must have wkhtmltopdf installed in your machine to run this.
#   See: https://pythonexamples.org/python-convert-html-to-pdf/

pdfkit.from_url('https://www.google.com/', '../google.pdf')
print("../google.pdf created")

pdfkit.from_url('https://daf-yomi.com/DYItemDetails.aspx?itemId=62689', '../62689.pdf')
print("../62689.pdf created")
