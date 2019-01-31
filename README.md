# EBL USD Exchange Rate Notifications

Send emails daily about the USD exchange rate of EBL.

- First install requirements
- Copy `.env.example` file to `.env`
- Add a gmail address and password. The gmail address should allow insecure apps. [How to do it?](https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833)
- Run `python3 __main__.py` for a single execution.

## To get added to auto email server
- To receive notifications, add your email to the `mail.list` file.
- Notifications are sent daily at `3AM GMT`.
