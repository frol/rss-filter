from django.db import models

class Feed(models.Model):
    title = models.CharField(max_length=255, default="", blank=True)
    description = models.CharField(max_length=255, default="", blank=True)
    link = models.CharField(max_length=1000, default="", blank=True)
    feed_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return u"%s (%s)" % (self.title, self.feed_url)

    def save(self, *args, **kwargs):
        if not (self.feed_url.startswith("http://") or self.feed_url.startswith("https://")):
            self.feed_url = "http://%s" % self.feed_url
        return super(Feed, self).save(*args, **kwargs)


class FeedItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, default="", blank=True)
    link = models.CharField(max_length=1000)
    feed = models.ForeignKey(Feed, related_name='items')

    def __unicode__(self):
        return self.title

    def is_favorite(self):
        if self.favorite.all().count() > 0:
            return True
        return False


class FavoriteItem(models.Model):
    feed_item = models.ForeignKey(FeedItem, related_name='favorite')
    
    def __unicode__(self):
        return self.feed_item


class SettingManager(models.Manager):
    def get_email(self):
        return self.get_or_create(id=1)[0].email

    def get_keywords(self):
        return self.get_or_create(id=1)[0].keywords
    
    def get_keyword_instance(self):
        return self.get_or_create(id=1)[0]


class Setting(models.Model):
    email = models.EmailField()
    keywords = models.TextField(default="", blank=True)
    objects = SettingManager()
