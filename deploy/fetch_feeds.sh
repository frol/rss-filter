#!/bin/sh
source /www/rss_filter/env/bin/activate
python /www/rss_filter/project/manage.py fetch_feeds
