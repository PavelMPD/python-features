from django.test import TestCase
from email_app.email_post_office_helper import EmailPostOfficeHelper


class EmailHelperTests(TestCase):
    def setUp(self):
        None

    def test_send_info_email(self):
        email_helper = EmailPostOfficeHelper()
        email_helper.send_info_email()
