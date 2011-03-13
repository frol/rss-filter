RSS filter
====================

Usage
-----

After you add feeds in web run `./manage.py fetch_feeds`

Installation
------------

1. Configure local\_settings.py:
`DATABASE_ENGINE = 'mysql'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'rss_filter'   # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'username@gmail.com'
EMAIL_HOST_PASSWORD = 'userpass'
EMAIL_PORT = 587
EMAIL_USE_TLS = True`
2. Syncdb `./manage.py fetch_feeds`
3. Profit
