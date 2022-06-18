import pdfkit
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options = {
    'page-width': '300.0mm',
    'page-height': '424.0mm',
    'margin-top': '0.0mm',
    'margin-right': '0.0mm',
    'margin-bottom': '0.0mm',
    'margin-left': '0.0mm',

}

for i in range(45):
    print(i)
    pdfkit.from_url(f'http://127.0.0.1:5000/seal/{i}', f'1_seal_{i}.pdf', configuration=config, options=options)

