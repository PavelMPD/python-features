from email_app.abstract_email_helper import AbstractEmailHelper
from post_office import mail


class EmailPostOfficeHelper(AbstractEmailHelper):
    def __init__(self):
        pass

    def send_info_email(self):
        self._send_info_email()


    def _send_info_email(self):
        mail.send(
            'test@gmail.com',
            'test@gmail.com',
            subject='Test email',
            message='This email has been sent from Django application'
        )