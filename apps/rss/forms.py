from django import forms

from .models import Feed, Setting

class EditSettings(forms.ModelForm):
    class Meta:
        model = Setting

    def __init__(self, *args, **kwargs):
        setting = Setting.objects.get_keyword_instance()
        return super(EditSettings, self).__init__(instance=setting, *args, **kwargs)

class AddFeed(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['feed_url']
