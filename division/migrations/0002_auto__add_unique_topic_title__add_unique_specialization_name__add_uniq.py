# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Topic', fields ['title']
        db.create_unique('topic', ['title'])

        # Adding unique constraint on 'Specialization', fields ['name']
        db.create_unique('specialization', ['name'])

        # Adding unique constraint on 'ClassLetter', fields ['letter']
        db.create_unique('class_letter', ['letter'])


    def backwards(self, orm):
        # Removing unique constraint on 'ClassLetter', fields ['letter']
        db.delete_unique('class_letter', ['letter'])

        # Removing unique constraint on 'Specialization', fields ['name']
        db.delete_unique('specialization', ['name'])

        # Removing unique constraint on 'Topic', fields ['title']
        db.delete_unique('topic', ['title'])


    models = {
        'defences.comission': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Comission', 'db_table': "'comission'"},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'888b9c69-d85f-48a0-9ce4-a7b54b1b22d6'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'division.classletter': {
            'Meta': {'ordering': "['letter']", 'object_name': 'ClassLetter', 'db_table': "'class_letter'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'85bafe84-e079-446c-bb03-bba2b899842e'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letter': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'division.mentor': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Mentor', 'db_table': "'mentor'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'f59f5b7c-62ca-4b37-a863-b446a560fd47'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'mentors'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'division.specialization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specialization', 'db_table': "'specialization'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'49c0ff7e-1eef-4fe5-8d10-15576514b88b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'division.student': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Student', 'db_table': "'student'"},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['defences.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'51fb3a8c-a0fe-4a40-96ba-e62f8c53753b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['reviewing.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Specialization']", 'blank': 'True', 'null': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'division.topic': {
            'Meta': {'ordering': "['title']", 'object_name': 'Topic', 'db_table': "'topic'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'cead9c06-dc51-47f9-b842-d32023b849a6'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['reviewing.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'reviewing.referee': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Referee', 'db_table': "'referee'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'d28a3857-0ae3-4e76-b0d0-eace436ad11a'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'referees'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'3c61d985-fb02-4e58-904a-76abf9e1d12d'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'6f0160c0-7192-4f3a-b677-7c892fd3af57'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'131da13a-64a3-4cc9-be00-3783173246e9'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['division']