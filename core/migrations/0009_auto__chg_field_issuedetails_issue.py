# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'IssueDetails.issue'
        db.alter_column(u'core_issuedetails', 'issue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Issue'], unique=True, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'IssueDetails.issue'
        raise RuntimeError("Cannot reverse this migration. 'IssueDetails.issue' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'IssueDetails.issue'
        db.alter_column(u'core_issuedetails', 'issue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Issue'], unique=True))

    models = {
        u'core.issue': {
            'Meta': {'object_name': 'Issue'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'core.issuedetails': {
            'Meta': {'ordering': "['nyear', 'nnumber']", 'object_name': 'IssueDetails'},
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Issue']", 'unique': 'True', 'null': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nnumber': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'number': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nyear': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['core']