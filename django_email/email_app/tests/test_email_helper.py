from django.test import TestCase
from email_app.email_helper import EmailHelper


class EmailHelperTests(TestCase):
    def setUp(self):
        None

    def test_send_info_email(self):
        email_helper = EmailHelper()
        email_helper.send_info_email()