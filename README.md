# BDS: Banking Digital Solutions

A Django web application for exploring personal savings against UK interest rates and inflation, built as my A-level Computer Science NEA (non-exam assessment) project.

Users register and log in, manage a simulated account balance, and see how that balance would grow at the current Bank Rate once inflation is taken into account. The live figures come from the Bank of England's website. A chart shows the history of the Bank Rate.

## Features

- **Accounts.** Registration and login with email and password, using a custom `Account` user model. Passwords are hashed with Django's bcrypt-SHA256 hasher, and duplicate emails are rejected.
- **Profile.** Change your username and upload a profile picture from the main menu.
- **Balance.** Deposit and withdraw from a simulated balance. Amounts are validated as whole numbers or exactly two decimal places.
- **Savings calculator.** The current Bank Rate and inflation rate are scraped from the Bank of England homepage. The page shows the interest a year would earn at that rate and the inflation-adjusted total.
- **Econometrics.** A Chart.js line chart of the Bank Rate from March 2008 to March 2023, drawn from 867 Bank of England observations.
- **About page.**

## Technology

| Area | Technology |
|---|---|
| Backend | Python 3.11, Django 4.2 |
| Database | SQLite |
| Security | bcrypt (`BCryptSHA256PasswordHasher`), CSRF protection, login-required views |
| Data collection | `requests` and BeautifulSoup |
| Frontend | Django templates, CSS, JavaScript, jQuery, Chart.js, Moment.js |
| Testing | Django test framework, GitHub Actions |

## Project structure

```
BDS/
├── manage.py
├── requirements.txt
├── BDS/                 # project package: settings, URLs, base template, shared static files
│   ├── templates/menu.html
│   ├── media/images/    # uploaded profile pictures (default avatar included)
│   └── Charts/          # saved copy of the Bank of England Database viewer, kept for reference
├── home/                # Account model, landing, login and registration pages
└── menu/                # main menu, balance, econometrics and about pages
    ├── functions.py     # amount validation and Bank of England scrapers
    └── static/BoE.json  # Bank Rate history used by the chart
```

## Running locally

```bash
cd BDS
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000/. The balance page needs internet access, because it reads the live rates from the Bank of England website.

### Configuration

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | a development-only key | Set this in any shared environment |
| `DJANGO_DEBUG` | `True` | Set to `False` outside local development |
| `DJANGO_ALLOWED_HOSTS` | empty | Comma-separated host names |

## Tests

```bash
cd BDS
python manage.py test
```

The suite has 17 tests. They cover:
- page rendering;
- registration and login;
- access control on the menu pages;
- deposits and withdrawals;
- the savings calculation;
- profile changes;
- amount validation.

The Bank of England scrapers are patched in the tests, so the suite runs offline.

## Limitations

- **The scrapers are fragile.** They depend on the structure of the Bank of England homepage; if the page changes, the balance page stops working.
- **Balances are simulated.** No real money or banking integration is involved, and a withdrawal isn't checked against the balance.
- **Development configuration.** The settings are for local use: debug mode is on by default, and the static-files configuration serves the project directory. They are not suitable for deployment as they stand.
- **An unused helper.** `home/hash.py` contains a bcrypt helper that the views no longer use; Django's password hasher is used instead.

## Data

Bank Rate history and the live rates are from the [Bank of England](https://www.bankofengland.co.uk/). The `Charts` folder is a saved copy of the Bank of England Database viewer page, kept as reference material, and it includes the third-party libraries that page loads.

## Author

Muhammad Hussain ([mh-husssain](https://github.com/mh-husssain))
