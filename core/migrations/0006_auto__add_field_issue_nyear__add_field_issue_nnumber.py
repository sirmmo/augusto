# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Issue.nyear'
        db.add_column(u'core_issue', 'nyear',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Issue.nnumber'
        db.add_column(u'core_issue', 'nnumber',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Issue.nyear'
        db.delete_column(u'core_issue', 'nyear')

        # Deleting field 'Issue.nnumber'
        db.delete_column(u'core_issue', 'nnumber')


    models = {
        u'core.issue': {
            'Meta': {'ordering': "['nyear', 'nnumber']", 'object_name': 'Issue'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nnumber': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'number': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nyear': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['core']