# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table('graduation_system_app_classletter', 'class_letter')
        db.rename_table('graduation_system_app_comission', 'comission')
        db.rename_table('graduation_system_app_comission_members_of_comission', 'comission_members_of_comission')
        db.rename_table('graduation_system_app_firm', 'firm')
        db.rename_table('graduation_system_app_mentor', 'mentor')
        db.rename_table('graduation_system_app_referee', 'referee')
        db.rename_table('graduation_system_app_referal', 'referal')
        db.rename_table('graduation_system_app_season', 'season')
        db.rename_table('graduation_system_app_specialization', 'specialization')
        db.rename_table('graduation_system_app_student', 'student')
        db.rename_table('graduation_system_app_teacher', 'teacher')
        db.rename_table('graduation_system_app_topic', 'topic')

    def backwards(self, orm):
        db.rename_table('class_letter', 'graduation_system_app_classletter')
        db.rename_table('comission', 'graduation_system_app_comission')
        db.rename_table('comission_members_of_comission', 'graduation_system_app_comission_members_of_comission')
        db.rename_table('firm', 'graduation_system_app_firm')
        db.rename_table('mentor', 'graduation_system_app_mentor')
        db.rename_table('referee', 'graduation_system_app_referee')
        db.rename_table('referal', 'graduation_system_app_referal')
        db.rename_table('season', 'graduation_system_app_season')
        db.rename_table('specialization', 'graduation_system_app_specialization')
        db.rename_table('student', 'graduation_system_app_student')
        db.rename_table('teacher', 'graduation_system_app_teacher')
        db.rename_table('topic', 'graduation_system_app_topic')

    models = {
        'graduation_system_app.classletter': {
            'Meta': {'object_name': 'ClassLetter', 'db_table': "'class_letter'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'3afc8208-ebb5-40fd-a5a8-aa62100513fa'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.comission': {
            'Meta': {'object_name': 'Comission', 'db_table': "'comission'"},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'6ff6f9a9-9120-41fe-b6aa-98e2bc4ad4dd'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['graduation_system_app.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.firm': {
            'Meta': {'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'931b0310-4923-43c5-add4-51640f177220'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor', 'db_table': "'mentor'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8329c07e-2777-44e9-81e7-02c78e1df441'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['graduation_system_app.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'mentors'", 'null': 'True', 'blank': 'True', 'to': "orm['graduation_system_app.Teacher']"})
        },
        'graduation_system_app.referal': {
            'Meta': {'object_name': 'Referal', 'db_table': "'referal'"},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'b69fcd60-2995-4147-887e-70b6ccf9804e'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referals'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referee': {
            'Meta': {'object_name': 'Referee', 'db_table': "'referee'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'93180433-147e-486e-b0ba-5cf2049810f3'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['graduation_system_app.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'referees'", 'null': 'True', 'blank': 'True', 'to': "orm['graduation_system_app.Teacher']"})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'5f37dba9-c327-468e-81ab-9778d81fd374'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.specialization': {
            'Meta': {'object_name': 'Specialization', 'db_table': "'specialization'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'574ae7d3-c1b8-462a-b3ef-8102cbf9c16b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student', 'db_table': "'student'"},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'912e446e-c5ab-4234-99d9-1cee2f69297b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['graduation_system_app.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Specialization']", 'blank': 'True', 'null': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.teacher': {
            'Meta': {'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'db269d5b-00ab-4abd-9b21-2a6b78534521'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic', 'db_table': "'topic'"},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'75a61c46-f007-4bc4-b7af-40f1f9369a0c'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['graduation_system_app.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']
