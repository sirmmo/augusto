# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Issue', fields ['number']
        db.create_index(u'core_issue', ['number'])

        # Adding index on 'Issue', fields ['mode']
        db.create_index(u'core_issue', ['mode'])

        # Adding index on 'Issue', fields ['year']
        db.create_index(u'core_issue', ['year'])


    def backwards(self, orm):
        # Removing index on 'Issue', fields ['year']
        db.delete_index(u'core_issue', ['year'])

        # Removing index on 'Issue', fields ['mode']
        db.delete_index(u'core_issue', ['mode'])

        # Removing index on 'Issue', fields ['number']
        db.delete_index(u'core_issue', ['number'])


    models = {
        u'core.issue': {
            'Meta': {'object_name': 'Issue'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'number': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['core']