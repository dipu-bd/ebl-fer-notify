import os

website = 'https://www.ebl.com.bd/home/Foreign_Exchange_Rates'

curdir = os.path.abspath(os.path.join(__file__, '..', '..'))

data_folder = os.path.join(curdir, 'data')
pdf_folder = os.path.join(data_folder, 'ebl')

csv_file = os.path.join(data_folder, 'usd.csv')

mail_list_url = 'https://raw.githubusercontent.com/dipu-bd/ebl-fer-notify/master/mail.list'
