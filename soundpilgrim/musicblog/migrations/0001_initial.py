# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SongCarousel'
        db.create_table(u'musicblog_songcarousel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('song_carousel_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'musicblog', ['SongCarousel'])

        # Adding model 'Genre'
        db.create_table(u'musicblog_genre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'musicblog', ['Genre'])

        # Adding model 'SongPost'
        db.create_table(u'musicblog_songpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateField')()),
            ('song_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('genre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['musicblog.Genre'])),
            ('soundcloud_url', self.gf('django.db.models.fields.TextField')()),
            ('song_carousel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['musicblog.SongCarousel'], null=True, blank=True)),
        ))
        db.send_create_signal(u'musicblog', ['SongPost'])


    def backwards(self, orm):
        # Deleting model 'SongCarousel'
        db.delete_table(u'musicblog_songcarousel')

        # Deleting model 'Genre'
        db.delete_table(u'musicblog_genre')

        # Deleting model 'SongPost'
        db.delete_table(u'musicblog_songpost')


    models = {
        u'musicblog.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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