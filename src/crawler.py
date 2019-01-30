import os
from datetime import date
import requests
from bs4 import BeautifulSoup

website = 'https://www.ebl.com.bd/home/Foreign_Exchange_Rates'
pdf_folder = os.path.join('data', 'ebl')


def download_latest():
    response = requests.get(website)
    soup = BeautifulSoup(response.text, 'lxml')
    href = soup.select('td.bodytext a.menu')[0]['href']

    response = requests.get(href)
    pdf_data = response.content

    today = date.today().isoformat()
    os.makedirs(pdf_folder, exist_ok=True)
    filename = os.path.join(pdf_folder, '%s.pdf' % today)
    with open(filename, 'wb') as fp:
        fp.write(pdf_data)
    # end with

    return filename
# end def
