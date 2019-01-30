from dotenv import load_dotenv
from .crawler import download_pdf
from .reader import parse_pdf
from .notify import notify_result

def main():
    load_dotenv()
    pdf_file = download_pdf()
    result = parse_pdf(pdf_file)
    notify_result(result)
# end def
