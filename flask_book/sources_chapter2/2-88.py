ADMINS = ['yourname@example.com']

if app.debug:
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler('127.0.0.1',
                               'server-error@example.com',
                               ADMINS, 'YourApplication Failed')
    app.logger.addHandler(mail_handler)