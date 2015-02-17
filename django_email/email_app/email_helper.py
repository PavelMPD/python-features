from django.core.mail import EmailMessage


class EmailHelper():
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
        email.send()