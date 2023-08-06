import pdfkit
# NOTE: you must have wkhtmltopdf installed in your machine to run this.
#   See: https://pythonexamples.org/python-convert-html-to-pdf/

html_str = '<h2>Heading 2</h2><p>Sample paragraph.</p><p>Sample paragraph.</p>'
pdfkit.from_string(html_str, '../sample.pdf')
