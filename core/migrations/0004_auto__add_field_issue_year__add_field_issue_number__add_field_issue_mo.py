# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Issue.year'
        db.add_column(u'core_issue', 'year',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Issue.number'
        db.add_column(u'core_issue', 'number',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Issue.mode'
        db.add_column(u'core_issue', 'mode',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Issue.year'
        db.delete_column(u'core_issue', 'year')

        # Deleting field 'Issue.number'
        db.delete_column(u'core_issue', 'number')

        # Deleting field 'Issue.mode'
        db.delete_column(u'core_issue', 'mode')


    models = {
        u'core.issue': {
            'Meta': {'object_name': 'Issue'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'year': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']