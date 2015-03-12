# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comission.cabinet'
        db.add_column('comission', 'cabinet',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comission.cabinet'
        db.delete_column('comission', 'cabinet')


    models = {
        'defences.comission': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Comission', 'db_table': "'comission'"},
            'cabinet': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'f3c9dd57-ec6a-4920-b8c5-7dcaedfaabf1'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'c02680e3-8268-4f33-b880-366fe3a65d58'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'1fded5b3-7cf2-43e9-94cd-af00b9a802ff'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'cf1591fe-6a50-4dd1-a4df-1d4815c60a5c'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['defences']