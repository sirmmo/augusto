# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Issue.number'
        db.delete_column(u'core_issue', 'number')

        # Deleting field 'Issue.mode'
        db.delete_column(u'core_issue', 'mode')

        # Deleting field 'Issue.year'
        db.delete_column(u'core_issue', 'year')

        # Deleting field 'Issue.nyear'
        db.delete_column(u'core_issue', 'nyear')

        # Deleting field 'Issue.nnumber'
        db.delete_column(u'core_issue', 'nnumber')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Issue.number'
        raise RuntimeError("Cannot reverse this migration. 'Issue.number' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Issue.number'
        db.add_column(u'core_issue', 'number',
                      self.gf('django.db.models.fields.TextField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Issue.mode'
        raise RuntimeError("Cannot reverse this migration. 'Issue.mode' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Issue.mode'
        db.add_column(u'core_issue', 'mode',
                      self.gf('django.db.models.fields.TextField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Issue.year'
        raise RuntimeError("Cannot reverse this migration. 'Issue.year' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Issue.year'
        db.add_column(u'core_issue', 'year',
                      self.gf('django.db.models.fields.TextField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Issue.nyear'
        raise RuntimeError("Cannot reverse this migration. 'Issue.nyear' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Issue.nyear'
        db.add_column(u'core_issue', 'nyear',
                      self.gf('django.db.models.fields.IntegerField')(db_index=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Issue.nnumber'
        raise RuntimeError("Cannot reverse this migration. 'Issue.nnumber' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Issue.nnumber'
        db.add_column(u'core_issue', 'nnumber',
                      self.gf('django.db.models.fields.IntegerField')(db_index=True),
                      keep_default=False)


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
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Issue']", 'unique': 'True'}),
            'mode': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nnumber': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'number': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'nyear': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'year': ('django.db.models.fields.TextField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['core']