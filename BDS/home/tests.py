from django.contrib.messages import get_messages
from django.test import TestCase

from .models import Account


def message_texts(response):
    return [str(message) for message in get_messages(response.wsgi_request)]


class PageTests(TestCase):
    def test_landing_login_and_register_pages_render(self):
        for url in ('/home/', '/home/login/', '/home/register/'):
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_root_redirects_to_landing_page(self):
        self.assertRedirects(self.client.get('/'), '/home/', fetch_redirect_response=False)


class RegistrationTests(TestCase):
    def test_register_creates_account_with_hashed_password(self):
        response = self.client.post('/home/register/', {'email': 'new@example.com', 'password': 'S3cure-pass'})

        self.assertRedirects(response, '/home', fetch_redirect_response=False)
        account = Account.objects.get(email='new@example.com')
        self.assertNotEqual(account.password, 'S3cure-pass')
        self.assertTrue(account.check_password('S3cure-pass'))

    def test_register_rejects_an_email_that_already_exists(self):
        Account.objects.create_user(username='taken@example.com', email='taken@example.com', password='x')

        response = self.client.post('/home/register/', {'email': 'taken@example.com', 'password': 'other'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Email exists, please use another!', message_texts(response))
        self.assertEqual(Account.objects.filter(email='taken@example.com').count(), 1)


class LoginTests(TestCase):
    def setUp(self):
        Account.objects.create_user(username='user@example.com', email='user@example.com', password='S3cure-pass')

    def test_correct_password_logs_in_and_opens_the_menu(self):
        response = self.client.post('/home/login/', {'email': 'user@example.com', 'password': 'S3cure-pass'})

        self.assertRedirects(response, '/menu', fetch_redirect_response=False)
        self.assertIn('_auth_user_id', self.client.session)

    def test_wrong_password_shows_an_error(self):
        response = self.client.post('/home/login/', {'email': 'user@example.com', 'password': 'wrong'})

        self.assertEqual(response.status_code, 200)
        self.assertIn('Email or password is incorrect!', message_texts(response))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_unknown_email_shows_an_error(self):
        response = self.client.post('/home/login/', {'email': 'nobody@example.com', 'password': 'x'})

        self.assertIn('Email or password is incorrect!', message_texts(response))
