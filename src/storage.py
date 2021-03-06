# -*- coding: utf-8 -*-
import os
from datetime import date
from .configs import *


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
    if len(lines) == 0 or lines[0].split('\t')[1].strip() != today:
        lines = ['%s\t%s\n' % (result, today)] + lines
    # end if

    with open(csv_file, 'w') as fp:
        fp.writelines(lines)
    # end with

    print('Saved: %s (%d items)' % (csv_file, len(lines)))
    return csv_file
# end def
