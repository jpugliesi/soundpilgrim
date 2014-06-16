# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotes_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateField')()),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('quoter', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quotes', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotes_quote')


    models = {
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'created_on': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quoter': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['quotes']