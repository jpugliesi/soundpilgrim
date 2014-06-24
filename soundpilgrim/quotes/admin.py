from django.contrib import admin
from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    fields = ['created_on', 'text', 'quoter']
    list_display = ('quoter', 'text', 'created_on')
    list_filter = ['created_on']

    search_fields = ['song_title', 'artist']

admin.site.register(Quote, QuoteAdmin)
