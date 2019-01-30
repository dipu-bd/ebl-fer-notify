# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from .crawler import download_pdf
from .reader import parse_pdf
from .storage import sync_result
from .notify import notify_result


def main():
    load_dotenv()
    pdf_file = download_pdf()
    result = parse_pdf(pdf_file)
    all_results = sync_result(result)
    notify_result(all_results)
# end def
