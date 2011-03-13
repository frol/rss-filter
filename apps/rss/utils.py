from .models import Setting

def user_filter(queryset):
    """
        Filter queryset using keywords
    """
    keywords = Setting.objects.get_keywords()
    if not keywords:
        return queryset
    result_queryset = queryset.none()
    for keyword in keywords.split(','):
        keyword = keyword.strip()
        result_queryset |= queryset.filter(title__icontains=keyword)
        result_queryset |= queryset.filter(content__icontains=keyword)
        result_queryset |= queryset.filter(link__icontains=keyword)
    return result_queryset

def user_filter_check_item(item):
    """
        Check feed item with keywords
    """
    keywords = Setting.objects.get_keywords()
    if not keywords:
        return True
    for keyword in keywords.split(','):
        keyword = keyword.strip().lower()
        if keyword in item.title.lower():
            return True
        if keyword in item.content.lower():
            return True
        if keyword in item.link.lower():
            return True
    return False
