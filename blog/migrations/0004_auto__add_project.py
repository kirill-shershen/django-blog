# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'blog_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'blog_project')


    models = {
        u'blog.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.project': {
            'Meta': {'ordering': "['priority', 'name']", 'object_name': 'Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']