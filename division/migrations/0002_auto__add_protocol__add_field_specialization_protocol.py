# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Protocol'
        db.create_table('protocol', (
            ('id', self.gf('django.db.models.fields.CharField')(default='d9d8efab-3bd6-40ea-b46d-26ed7cc6b17d', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('path_to_view', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('division', ['Protocol'])

        # Adding field 'Specialization.protocol'
        db.add_column('specialization', 'protocol',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='specializations', null=True, blank=True, to=orm['division.Protocol']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Protocol'
        db.delete_table('protocol')

        # Deleting field 'Specialization.protocol'
        db.delete_column('specialization', 'protocol_id')


    models = {
        'defences.comission': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Comission', 'db_table': "'comission'"},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'7d788900-db52-4f83-8c2e-73db2ee15944'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'division.classletter': {
            'Meta': {'ordering': "['letter']", 'object_name': 'ClassLetter', 'db_table': "'class_letter'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'b8d1ec3b-fd26-4fce-b143-5f06e53fc2bf'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'division.mentor': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Mentor', 'db_table': "'mentor'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'a8459c68-e0e3-4b38-ba6c-d11f13fec801'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'mentors'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'division.protocol': {
            'Meta': {'ordering': "['name']", 'object_name': 'Protocol', 'db_table': "'protocol'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'6e055b24-df5a-46f5-81f3-97826e1918ff'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'path_to_view': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'division.specialization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specialization', 'db_table': "'specialization'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'788c4fe3-c60c-4c5c-899f-3582c53e8050'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'protocol': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'specializations'", 'null': 'True', 'blank': 'True', 'to': "orm['division.Protocol']"})
        },
        'division.student': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Student', 'db_table': "'student'"},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['defences.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'848c5d52-6d73-4bff-8aac-76f0dedc6f07'", 'max_length': '36', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'default': "'6db251c3-410b-48ba-a709-aa0451f5dbb7'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['reviewing.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reviewing.referee': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Referee', 'db_table': "'referee'"},
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'033a4548-7c7f-42c3-af49-6be361990fd8'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'referees'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'c9f578fe-cd53-40ed-ade9-0352cd23199c'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'f0ddc9e5-4aa1-4d0e-8045-be44f76e894d'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'6dbb8ba4-be98-4c9b-8732-66e080b3ba3a'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['division']