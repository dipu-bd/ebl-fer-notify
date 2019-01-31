# -*- coding: utf-8 -*-
import os
from datetime import date

curdir = os.path.dirname(__file__)
data_folder = os.path.join(curdir, 'data')
csv_file = os.path.join(data_folder, 'usd.csv')
fieldnames = ['date', 'rate']


def sync_result(result):
    print('Saving result...')

    lines = []
    if not os.path.exists(csv_file):
        os.makedirs(data_folder, exist_ok=True)
    else:
        with open(csv_file, 'r') as fp:
            lines = fp.readlines()
        # end with
    # end if

    today = date.today().isoformat()
    if len(lines) and lines[0].split('\t')[1].strip() != today:
        lines = ['%s\t%s\n' % (result, today)] + lines
    # end if

    with open(csv_file, 'w') as fp:
        fp.writelines(lines)
    # end with

    print('Saved: %s (%d items)' % (csv_file, len(lines)))
    return csv_file
# end def
