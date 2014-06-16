from django import forms
from django.core.exceptions import ValidationError
import re

from musicblog.models import SongCarousel, SongPost, Genre

class SongPostForm(forms.ModelForm):

    def clean_soundcloud_url(self):

        iframe_start = '<iframe width="100%" height="100%" scrolling="no" frameborder="no" src="'
        iframe_end = '&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>'

        soundcloud_url = self.cleaned_data.get('soundcloud_url')

        url_segment = re.search(r'src="(.+?)&amp', soundcloud_url)

        if url_segment:

            new_soundcloud_url = iframe_start + url_segment.group(1) + iframe_end

            self.cleaned_data['soundcloud_url'] = new_soundcloud_url 

        return self.cleaned_data['soundcloud_url']
