# -*- coding: utf-8 -*-
from smtplib import SMTP


def get_message(all_results):
    if len(all_results) == 0:
        return 'Not enough data.'
    # end if

    first = [x.strip() for x in all_results[0].split('\t')]

    msg = 'Current rate is "%s" for "%s".\n' % (first[0], first[1])
    if len(all_results) == 1:
        return msg
    # end if

    second = [x.strip() for x in all_results[1].split('\t')]

    first_rate = float(first[0])
    second_rate = float(second[0])

    if first_rate == second_rate:
        msg += ' No change since "%s".' % second[1]
    elif first_rate < second_rate:
        diff = second_rate - first_rate
        msg += 'Decreased by "%.4f" than "%s".\n' % (diff, second[1])
    else:
        diff = first_rate - second_rate
        msg += 'Increased by "%.4f" than "%s".\n' % (diff, second[1])
    # end if

    return msg.strip()
# end def


def notify_result(csv_file):
    print('Processing result...')
    all_results = []
    try:
        with open(csv_file, 'r') as fp:
            all_results = fp.readlines()
        # end with
    except Exception as err:
        pass
    # end try

    msg = get_message(all_results)
    print(msg)

    print('Sending email...')
    host = ''
    port = ''
    with SMTP(host, port) as smtp:
        pass
# end def
