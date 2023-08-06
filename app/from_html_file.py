import pdfkit
# NOTE: you must have wkhtmltopdf installed in your machine to run this.
#   See: https://pythonexamples.org/python-convert-html-to-pdf/

pdfkit.from_file("../html_file1.html", "../html_file1.pdf",)
