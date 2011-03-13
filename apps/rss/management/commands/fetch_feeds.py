#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings

from lockfile import FileLock
from mailer import send_html_mail

import datetime
import feedparser
import os

from rss.models import Feed, FeedItem, Setting
from rss.utils import user_filter_check_item

LOCK_FILE = 'fetch_feed'

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Check whether it is already running or not
        lock = FileLock(os.path.join(
            settings.MEDIA_ROOT, LOCK_FILE
        ))
        try:
            lock.acquire(0)
        except:
            print 'It seems the command is processing already.'
            return
        
        feeds = Feed.objects.all()
        for feed in feeds:
            print "Processing `%s` feed..." % feed.feed_url
            self.process_feed(feed)

        lock.release()

    def process_feed(self, feed):
        # parse feed
        parsed_feed = feedparser.parse(feed.feed_url)
        if 'feed' not in parsed_feed or not parsed_feed['feed']:
            print "Feed info not found"
            return False

        feed_info = parsed_feed.get('feed')
        feed.title = feed_info.get('title')
        feed.description = feed_info.get('subtitle')
        feed.save()
    
        # add all feed items into database
        for entry in parsed_feed.get('entries'):
            feed_item, is_new = FeedItem.objects.get_or_create(feed=feed, title=entry.title)
            if 'summary' in entry:
                feed_item.content = entry.get('summary')
            elif 'subtitle' in entry:
                feed_item.content = entry.get('subtitle')
            feed_item.link = entry.get('link')

            time_struct = entry.get('updated_parsed')
            updated_datetime = datetime.datetime(time_struct.tm_year, time_struct.tm_mon, \
                                        time_struct.tm_mday, time_struct.tm_hour, \
                                        time_struct.tm_min, time_struct.tm_sec)
            feed_item.updated_datetime = updated_datetime
            if is_new:
                feed_item.published_datetime = updated_datetime
            feed_item.author = entry.get('author', '')

            feed_item.save()

            # send email notification only if new feed item apears with user's keywords
            if is_new and user_filter_check_item(feed_item):
                message = "<a href='%(link)s'>%(title)s</a><br><br>%(content)s" % (dict(link=feed_item.link, title=feed_item.title, content=feed_item.content))
                recipients = [Setting.objects.get_email()]
                send_html_mail("[Feed filter] New feed item", "", message, settings.DEFAULT_FROM_EMAIL, recipients)
