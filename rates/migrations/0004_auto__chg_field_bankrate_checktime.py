# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'BankRate.checktime'
        db.alter_column(u'rates_bankrate', 'checktime', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'BankRate.checktime'
        db.alter_column(u'rates_bankrate', 'checktime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'rates.bank': {
            'Meta': {'ordering': "['name']", 'object_name': 'Bank'},
            'URL': ('django.db.models.fields.URLField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'xpath': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        u'rates.bankcontact': {
            'Meta': {'object_name': 'BankContact'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rates.Bank']"}),
            'contacttype': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'rates.bankrate': {
            'Meta': {'object_name': 'BankRate'},
            'bank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rates.Bank']"}),
            'checktime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['rates']