from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from .models import Feed, FeedItem, FavoriteItem
from .feeds import AllItemsFeed, FilteredItemsFeed

favorite_dict = {
    'queryset': FavoriteItem.objects.all().order_by('-feed_item__updated_datetime'),
    'template_object_name': 'feed_item',
}

feed_dict = {
    'queryset': Feed.objects.all().order_by('-id'),
    'template_object_name': 'feed',
}

rss_dict = {
    'all': AllItemsFeed,
    'filtered': FilteredItemsFeed,
}

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': 'filtered/'}, name='feed_item_list'),
    url(r'^(?P<filter_type>all|filtered)/$', 'rss.views.item_list', name='feed_item_list'),
    url(r'^favorites/$', 'django.views.generic.list_detail.object_list', favorite_dict, name='feed_favorite_item_list'),
    url(r'^mark_favorite/(?P<object_id>\d+)/$', 'rss.views.mark_favorite', name='feed_item_mark_favorite'),
    url(r'^unmark_favorite/(?P<object_id>\d+)/$', 'rss.views.unmark_favorite', name='feed_item_unmark_favorite'),
    url(r'^settings/$', 'rss.views.edit_settings', name='edit_settings'),
    url(r'^feed/$', 'django.views.generic.list_detail.object_list', feed_dict, name='feed_list'),
    url(r'^feed/add/$', 'rss.views.feed_add', name='feed_add'),
    url(r'^feed/delete/(?P<object_id>\d+)/$', 'rss.views.feed_delete', name='feed_delete'),
    url(r'^rss/(all|filtered)/$', 'django.contrib.syndication.views.feed', {'feed_dict': rss_dict}, name='rss'),
)
