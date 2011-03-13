RSS filter
====================

Usage
-----

After you add feeds in web run `./manage.py fetch_feeds`

Installation
------------

1. Install requirements `pip install -r deploy/requirements.txt`
2. Configure local\_settings.py:
3. Syncdb `./manage.py syncdb`
4. Profit

Settings
--------

    DATABASE_ENGINE = 'mysql'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'rss_filter'   # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'username@gmail.com'
    EMAIL_HOST_PASSWORD = 'userpass'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
