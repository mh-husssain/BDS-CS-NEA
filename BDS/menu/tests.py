from decimal import Decimal
from unittest.mock import patch

from django.contrib.messages import get_messages
from django.test import SimpleTestCase, TestCase

from home.models import Account

from .functions import validate


def message_texts(response):
    return [str(message) for message in get_messages(response.wsgi_request)]


class ValidateTests(SimpleTestCase):
    def test_accepts_whole_amounts_and_two_decimal_places(self):
        for amount in ('100', '0', '12.50', '.99'):
            with self.subTest(amount=amount):
                self.assertTrue(validate(amount))

    def test_rejects_badly_formatted_amounts(self):
        for amount in ('12.5', '12.505', '1.2.3', '-5', '10a', '£10', '.', ''):
            with self.subTest(amount=amount):
                self.assertFalse(validate(amount))

    def test_rejects_a_missing_amount(self):
        self.assertFalse(validate(None))


class MenuAccessTests(TestCase):
    def test_menu_pages_require_login(self):
        for url in ('/menu/', '/menu/balance/', '/menu/econometrics', '/menu/about-us'):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 302)
                self.assertTrue(response['Location'].startswith('/home'))

    def test_logout_ends_the_session(self):
        account = Account.objects.create_user(username='u@example.com', email='u@example.com', password='x')
        self.client.force_login(account)

        self.assertRedirects(self.client.get('/menu/logout'), '/home', fetch_redirect_response=False)
        self.assertNotIn('_auth_user_id', self.client.session)


@patch('menu.views.scrapeInterest', return_value='5.25%')
@patch('menu.views.scrapeInflation', return_value='4.6%')
class BalanceTests(TestCase):
    """The live Bank of England figures are patched so the tests are repeatable and offline."""

    def setUp(self):
        self.account = Account.objects.create_user(
            username='saver@example.com', email='saver@example.com', password='x', balance=Decimal('1000.00')
        )
        self.client.force_login(self.account)

    def test_shows_rates_and_projected_savings(self, _inflation, _interest):
        response = self.client.get('/menu/balance/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['interest'], '5.25%')
        self.assertEqual(response.context['inflation'], '4.6%')
        self.assertEqual(response.context['saving'], Decimal('52.50'))  # 1000.00 at 5.25%
        self.assertEqual(response.context['total'], Decimal('1004.08'))  # (1000 + 52.50) less 4.6% inflation

    def test_valid_deposit_increases_the_balance(self, _inflation, _interest):
        response = self.client.post('/menu/balance/', {'form': 'DEPOSIT', 'deposit': '250.75'})

        self.assertRedirects(response, '/menu/balance', fetch_redirect_response=False)
        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, Decimal('1250.75'))

    def test_valid_withdrawal_decreases_the_balance(self, _inflation, _interest):
        self.client.post('/menu/balance/', {'form': 'WITHDRAW', 'withdraw': '100'})

        self.account.refresh_from_db()
        self.assertEqual(self.account.balance, Decimal('900.00'))

    def test_invalid_amounts_leave_the_balance_unchanged(self, _inflation, _interest):
        for form, field, amount in (('DEPOSIT', 'deposit', '12.5'), ('WITHDRAW', 'withdraw', 'ten'), ('DEPOSIT', 'deposit', '')):
            with self.subTest(form=form, amount=amount):
                response = self.client.post('/menu/balance/', {'form': form, field: amount})

                self.assertEqual(response.status_code, 200)
                self.assertIn('Enter a valid amount!', message_texts(response))
                self.account.refresh_from_db()
                self.assertEqual(self.account.balance, Decimal('1000.00'))


class ProfileTests(TestCase):
    def test_changing_the_username_on_the_main_menu(self):
        account = Account.objects.create_user(username='old-name', email='me@example.com', password='x')
        self.client.force_login(account)

        response = self.client.post('/menu/', {'username': 'new-name'})

        self.assertRedirects(response, '/menu/', fetch_redirect_response=False)
        account.refresh_from_db()
        self.assertEqual(account.username, 'new-name')
