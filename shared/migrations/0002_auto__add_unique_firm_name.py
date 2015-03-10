# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Firm', fields ['name']
        db.create_unique('firm', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Firm', fields ['name']
        db.delete_unique('firm', ['name'])


    models = {
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'f4505c41-2cd6-4352-aa53-6b9562a69c23'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'26946695-67fd-4928-be46-5d41b1b3343a'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'552c462e-9840-4c72-b717-4039be7883e7'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['shared']