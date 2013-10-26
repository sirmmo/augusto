# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Issue', fields ['text']
        db.create_index(u'core_issue', ['text'])


    def backwards(self, orm):
        # Removing index on 'Issue', fields ['text']
        db.delete_index(u'core_issue', ['text'])


    models = {
        u'core.issue': {
            'Meta': {'object_name': 'Issue'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['core']