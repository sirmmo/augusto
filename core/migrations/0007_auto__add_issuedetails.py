# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IssueDetails'
        db.create_table(u'core_issuedetails', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Issue'], unique=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('year', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('nyear', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('number', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('nnumber', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('mode', self.gf('django.db.models.fields.TextField')(db_index=True)),
        ))
        db.send_create_signal(u'core', ['IssueDetails'])


    def backwards(self, orm):
        # Deleting model 'IssueDetails'
        db.delete_table(u'core_issuedetails')


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