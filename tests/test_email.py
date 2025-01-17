import os

from accounts.email_connection import Email
from django.test import TestCase


class EmailTest(TestCase):
    def test_email_connection(self):
        email = Email()
        self.assertIsNotNone(email.conn)

    def test_send_email(self):
        email = Email(debug=True)
        response = email.send_mail('test@test.com', 'Test Email', 'Hello, this is a test')
        self.assertIs(response, 0)
        self.assertEqual(email.debug, True)
        self.assertEqual(email.username, 'test@test.com')
