# -*- coding: utf-8 -*-
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def parse_pdf(pdf_file):
    print('Parsing pdf...')
    
    # Create meta objects
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Process 1st page of the document
    with open(pdf_file, 'rb') as fp:
        page = next(PDFPage.get_pages(fp))
        interpreter.process_page(page)
        body = retstr.getvalue()
    # end with

    # Extract rate from body
    text = body.replace('\n\n', '\n')
    text = text.split('All Card Related Payment')[1]
    text = text.split('Currency')[1]
    text = text.split('USD')[1]
    text = text.split('Rate')[1]
    text = text.strip().split('\n')[0]

    print('USD Rate: %s' % text)
    return text
# end def
