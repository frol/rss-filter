from django.http import HttpResponseRedirect, Http404 
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.views.generic import list_detail

from misc.json_encode import JSONResponse 
from .forms import AddFeed, EditSettings
from .models import Feed, FeedItem, FavoriteItem
from .utils import user_filter

def item_list(request, filter_type, template_name='rss/feeditem_list.html'):
    if filter_type == 'all':
        feed_item_list = FeedItem.objects.all()
    else:
        feed_item_list = user_filter(FeedItem.objects.all())
    feed_item_list = feed_item_list.order_by('-updated_datetime')
    return render_to_response(template_name, {'feed_item_list': feed_item_list}, context_instance=RequestContext(request))

def mark_favorite(request, object_id):
    """
        Mark new item as favorite
    """
    feed_item = get_object_or_404(FeedItem, id=object_id)
    fav_item, is_new = FavoriteItem.objects.get_or_create(feed_item=feed_item)
    if request.is_ajax():
        return JSONResponse({'status': 'ok', 'text': 'Marked as favorite'}, False)
    return redirect(request.META.get('HTTP_REFERER', 'feed_item_list'))

def unmark_favorite(request, object_id):
    """
        Unmark new item favorite status
    """
    fav_item = get_object_or_404(FavoriteItem, feed_item__id=object_id)
    fav_item.delete()
    if request.is_ajax():
        return JSONResponse({'status': 'ok', 'text': 'Unmarked favorite'}, False)
    return redirect(request.META.get('HTTP_REFERER', 'feed_item_list'))

def edit_settings(request, form_class=EditSettings, template_name='rss/edit_settings'):
    """
        Select email for notification and keywords for filtering feed items
    """
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('feed_item_list')
    else:
        form = form_class()

    if request.is_ajax():
        template_name += '_ajax'
    template_name += '.html'
    return render_to_response(template_name, {'form': form}, context_instance=RequestContext(request))

def feed_add(request, form_class=AddFeed, template_name='rss/feed_add'):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('feed_list')
    else:
        form = form_class()

    if request.is_ajax():
        template_name += '_ajax'
    template_name += '.html'
    return render_to_response(template_name, {'form': form}, context_instance=RequestContext(request))

def feed_delete(request, object_id):
    feed = get_object_or_404(Feed, id=object_id)
    feed.delete()
    return redirect(request.META.get('HTTP_REFERER', 'feed_list'))
