# -*- coding: utf-8 -*-
import smtplib


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
    # end def

    def send_message(self, email, subject, body):
        ''' This must be removed '''
        if not email:
            return
        # end if
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
            "Content-Type: text/html",
        ]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            email,
            headers + "\r\n\r\n" + body
        )
    # end def
# end class
