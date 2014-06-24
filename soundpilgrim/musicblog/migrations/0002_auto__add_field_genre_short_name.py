# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Genre.short_name'
        db.add_column(u'musicblog_genre', 'short_name',
                      self.gf('django.db.models.fields.CharField')(default='chill', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Genre.short_name'
        db.delete_column(u'musicblog_genre', 'short_name')


    models = {
        u'musicblog.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'musicblog.songcarousel': {
            'Meta': {'object_name': 'SongCarousel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song_carousel_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'musicblog.songpost': {
            'Meta': {'object_name': 'SongPost'},
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'created_on': ('django.db.models.fields.DateField', [], {}),
            'genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['musicblog.Genre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'song_carousel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['musicblog.SongCarousel']", 'null': 'True', 'blank': 'True'}),
            'song_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'soundcloud_url': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['musicblog']