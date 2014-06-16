from django.db import models
import re

class SongCarousel(models.Model):
    song_carousel_title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.song_carousel_title

class Genre(models.Model):
    genre_name = models.CharField('Genre', max_length = 50, null=False)

    def __unicode__(self):
        return self.genre_name

class SongPost(models.Model):
    created_on = models.DateField('Date Created', null=False, editable=True)
    song_title = models.CharField(max_length=200, null=False)
    artist = models.CharField(max_length=200, null=False)
    genre = models.ForeignKey(Genre, null=False)
    soundcloud_url = models.TextField(null=False)
    song_carousel = models.ForeignKey(SongCarousel, blank=True, null=True)

    def is_in_song_carousel(self):
        return self.song_carousel
    is_in_song_carousel.boolean = True
    is_in_song_carousel.short_description = 'In Song Carousel?'

    def save(self, *args, **kwargs):
        self.full_clean()
        super(SongPost, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        self.soundcloud_url = clean_soundcloud_url(self.soundcloud_url)
        super(SongPost, self).clean(*args, **kwargs)

    def __unicode__(self):
        return self.song_title + ' - ' + self.artist + ' (' + unicode(self.genre) + ')'

# Helper functions

def clean_soundcloud_url(old_soundcloud_url):

    iframe_start = '<iframe width="100%" height="100%" scrolling="no" frameborder="no" src="'
    iframe_end = '&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>'


    url_segment = re.search(r'src="(.+?)&amp', old_soundcloud_url)
    
    new_soundcloud_url = ""
    if url_segment:

        new_soundcloud_url = iframe_start + url_segment.group(1) + iframe_end
    else:
        new_soundcloud_url = ""

    return new_soundcloud_url 
