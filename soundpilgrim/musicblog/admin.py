from django.contrib import admin
from musicblog.models import SongPost, SongCarousel, Genre

class SongPostAdmin(admin.ModelAdmin):
    fields = ['created_on', 'song_title', 'artist', 'genre', 'soundcloud_url']
    list_display = ('song_title', 'artist', 'genre', 'created_on')
    list_filter = ['created_on']

    search_fields = ['song_title', 'artist']

admin.site.register(SongPost, SongPostAdmin)
admin.site.register(SongCarousel)
