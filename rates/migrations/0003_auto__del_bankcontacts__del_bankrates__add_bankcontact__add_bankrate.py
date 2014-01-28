# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BankContacts'
        db.delete_table(u'rates_bankcontacts')

        # Deleting model 'BankRates'
        db.delete_table(u'rates_bankrates')

        # Adding model 'BankContact'
        db.create_table(u'rates_bankcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rates.Bank'])),
            ('contacttype', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'rates', ['BankContact'])

        # Adding model 'BankRate'
        db.create_table(u'rates_bankrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rates.Bank'])),
            ('rate', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('checktime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'rates', ['BankRate'])


    def backwards(self, orm):
        # Adding model 'BankContacts'
        db.create_table(u'rates_bankcontacts', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rates.Bank'])),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal(u'rates', ['BankContacts'])

        # Adding model 'BankRates'
        db.create_table(u'rates_bankrates', (
            ('checktime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('rate', self.gf('django.db.models.fields.CharField')(max_length=3)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rates.Bank'])),
        ))
        db.send_create_signal(u'rates', ['BankRates'])

        # Deleting model 'BankContact'
        db.delete_table(u'rates_bankcontact')

        # Deleting model 'BankRate'
        db.delete_table(u'rates_bankrate')


    models = {
        u'rates.bank': {
            'Meta': {'object_name': 'Bank'},
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
            'checktime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['rates']