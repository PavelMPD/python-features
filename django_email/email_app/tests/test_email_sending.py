from django.test import TestCase
from django.conf import settings
from django.core.mail import send_mail


class EmailTests(TestCase):
    def setUp(self):
        None

    def test_send_email(self):
        self._send_email()

    def _send_email(self):
        subject = "Test email"
        message = "This email has been sent from Django application"
        from_email = "PavelMPD82@gmail.com"
        recipient_list = ["PavelMPD82@gmail.com", "OduvanchikBy@gmail.com"]
        fail_silently = False
        send_mail(subject, message, from_email, recipient_list, fail_silently)