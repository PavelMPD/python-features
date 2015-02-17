from django.core.mail import EmailMessage
from email_app.abstract_email_helper import AbstractEmailHelper


class EmailHelper(AbstractEmailHelper):
    def __init__(self):
        pass

    def send_info_email(self):
        self._send_info_email()

    def _send_info_email(self):
        subject = "Test email"
        message = "This email has been sent from Django application"
        from_email = "test@gmail.com"
        recipient_list = ["test1@gmail.com", "test1@gmail.com"]
        email = EmailMessage(subject, message, from_email, recipient_list)
        filename, content = self._get_info_file()
        email.attach(filename, content)
        email.send()

    def _get_info_file(self):
        filename = 'information.txt'
        content = 'Information text'
        return filename, content