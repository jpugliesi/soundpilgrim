from django.db import models

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

    def __unicode__(self):
        return self.song_title + ' ' + self.artist + ' (' + unicode(self.genre) + ')'
