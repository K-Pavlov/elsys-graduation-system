# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Season.year'
        db.alter_column(u'graduation_system_app_season', 'year', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # Changing field 'Season.year'
        db.alter_column(u'graduation_system_app_season', 'year', self.gf('graduation_system_app.models.season.YearYearField')(max_length=20))

    models = {
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10529895249726083556'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'10529852291463188964'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'class_letter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10529809346085196260'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10529852295758156260'", 'max_length': '36', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']