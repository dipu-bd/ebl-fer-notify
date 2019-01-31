# -*- coding: utf-8 -*-
from datetime import datetime
from dotenv import load_dotenv
from .crawler import download_latest
from .reader import parse_pdf
from .storage import sync_result
from .notify import notify_result
from .configs import *


def main():
    print('-' * 80)
    print('Started "%s"' % datetime.now().isoformat())
    print('Current path:', curdir)

    load_dotenv()
    pdf_file = download_latest()
    result = parse_pdf(pdf_file)
    all_results = sync_result(result)
    notify_result(all_results)

    print('-' * 80)
# end def
