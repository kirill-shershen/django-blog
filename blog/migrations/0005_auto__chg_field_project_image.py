# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'blog_project', 'image', self.gf('django.db.models.fields.CharField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'Project.image'
        db.alter_column(u'blog_project', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['blog']