from django.contrib.syndication.feeds import Feed 
from django.conf import settings

from .models import FeedItem
from .utils import user_filter

ITEMS_PER_FEED = getattr(settings, 'ITEMS_PER_FEED', 20)

class AllItemsFeed(Feed):
    title = "RSS-Filter: All news"
    description = "All news from rss-filter"
    link = '/rss/all/'

    title_template = 'rss/feeds/title.html'
    description_template = 'rss/feeds/description.html'

    def item_link(self, obj):
        return obj.link

    def item_pubdate(self, item):
        return item.published_datetime
    
    def item_author_name(self, obj):
        return obj.author

    def items(self):
        return FeedItem.objects.order_by("-updated_datetime")[:ITEMS_PER_FEED]


class FilteredItemsFeed(AllItemsFeed):
    title = "RSS-Filter: Filtered news"
    description = "Filtered news from rss-filter"
    link = '/rss/filtered/'

    def items(self):
        return user_filter(FeedItem.objects.order_by("-updated_datetime"))[:ITEMS_PER_FEED]
