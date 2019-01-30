from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def parse_pdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Process 1st page contained in the document.
    with open(pdf_file, 'rb') as fp:
        page = next(PDFPage.get_pages(fp))
        interpreter.process_page(page)
        body = retstr.getvalue()
    # end with

    text = body.replace('\n\n', '\n')
    text = text.split('All Card Related Payment')[1]
    text = text.split('Currency')[1]
    text = text.split('USD')[1]
    text = text.split('Rate')[1]
    text = text.strip().split('\n')[0]

    return text
# end def
