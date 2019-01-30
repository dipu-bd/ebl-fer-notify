# -*- coding: utf-8 -*-
import os
from smtplib import SMTP_SSL


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
    with open('mail.list') as fp:
        emails = [x.strip() for x in fp.readlines() if x.strip()]
    # end with

    user = os.getenv('GMAIL_USER', '')
    password = os.getenv('GMAIL_PASSWORD', '')
    mail_fmt = 'From: %s\nTo: %s\nSubject: %s\n\n%s'
    subject = 'EBL Foreign Exchange Rate Notification'

    print('Opening SMTP SSL server')
    with SMTP_SSL('smtp.gmail.com', 465) as server:
        print('Logging in...')
        server.login(user, password)
        for email in emails:
            print('Seding email to %s' % email)
            email_text = mail_fmt % (user, email, subject, msg)
            server.sendmail(user, email, email_text)
            print('Email sent to %s' % email)
        # end for
    # end with
# end def
