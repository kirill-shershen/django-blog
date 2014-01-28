# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bank'
        db.create_table(u'rates_bank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('URL', self.gf('django.db.models.fields.URLField')(max_length=300, blank=True)),
            ('xpath', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
        ))
        db.send_create_signal(u'rates', ['Bank'])


    def backwards(self, orm):
        # Deleting model 'Bank'
        db.delete_table(u'rates_bank')


    models = {
        u'rates.bank': {
            'Meta': {'object_name': 'Bank'},
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'xpath': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        }
    }

    complete_apps = ['rates']