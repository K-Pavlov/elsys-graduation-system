# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mentor'
        db.create_table('mentor', (
            ('id', self.gf('django.db.models.fields.CharField')(default='f74d3236-cd22-4127-a564-a81ca585abcd', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['shared.Season'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='mentors', null=True, blank=True, to=orm['shared.Teacher'])),
        ))
        db.send_create_signal('division', ['Mentor'])

        # Adding model 'Topic'
        db.create_table('topic', (
            ('id', self.gf('django.db.models.fields.CharField')(default='56d75cfc-4736-45ce-8537-a1dc5e382a78', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['shared.Season'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topics', on_delete=models.SET_NULL, default='', to=orm['division.Mentor'], blank=True, null=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topics', on_delete=models.SET_NULL, default='', to=orm['reviewing.Referee'], blank=True, null=True)),
        ))
        db.send_create_signal('division', ['Topic'])

        # Adding model 'Specialization'
        db.create_table('specialization', (
            ('id', self.gf('django.db.models.fields.CharField')(default='0ee93894-86f7-4e72-bd5c-67a3b33e4f8f', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('division', ['Specialization'])

        # Adding model 'ClassLetter'
        db.create_table('class_letter', (
            ('id', self.gf('django.db.models.fields.CharField')(default='630c2aa7-4bd8-4960-a21d-9195b33620bb', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('division', ['ClassLetter'])

        # Adding model 'Student'
        db.create_table('student', (
            ('id', self.gf('django.db.models.fields.CharField')(default='247b534e-511b-4f3f-9189-385d64d74892', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['shared.Season'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grade', self.gf('django.db.models.fields.FloatField')(default=2.0, blank=True)),
            ('class_letter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['division.ClassLetter'], blank=True, null=True)),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['division.Specialization'], blank=True, null=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['division.Topic'], blank=True, null=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['division.Mentor'], blank=True, null=True)),
            ('comission', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['defences.Comission'], blank=True, null=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['reviewing.Referee'], blank=True, null=True)),
        ))
        db.send_create_signal('division', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Mentor'
        db.delete_table('mentor')

        # Deleting model 'Topic'
        db.delete_table('topic')

        # Deleting model 'Specialization'
        db.delete_table('specialization')

        # Deleting model 'ClassLetter'
        db.delete_table('class_letter')

        # Deleting model 'Student'
        db.delete_table('student')


    models = {
        'defences.comission': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Comission', 'db_table': "'comission'"},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'bcb551cc-2835-48c6-90e5-f2d93750e339'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'division.classletter': {
            'Meta': {'ordering': "['letter']", 'object_name': 'ClassLetter', 'db_table': "'class_letter'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'1006b4a1-16c1-456f-9803-62c7a27aadf3'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'division.mentor': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Mentor', 'db_table': "'mentor'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'80d361b0-be37-451a-bb7b-cd99fcb32c1f'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'mentors'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'division.specialization': {
            'Meta': {'ordering': "['name']", 'object_name': 'Specialization', 'db_table': "'specialization'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8040ed6b-335a-4172-acc6-bb16fb5530fe'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'division.student': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Student', 'db_table': "'student'"},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['defences.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'91ec8507-8b8b-4828-8dc9-c756bcd628fc'", 'max_length': '36', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'default': "'82d5c69f-fc1c-4ccd-aa3d-6039e8dbf8a4'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['division.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['reviewing.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reviewing.referee': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Referee', 'db_table': "'referee'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'04812747-8932-4845-bfe2-bf8d2378cf8e'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'referees'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8404dc56-c226-4acd-9972-4a369f1f8b95'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'5118d779-0642-4146-8ac1-4d2cc1f1bbfc'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'0ec9db93-47da-4d42-bdd8-3ccbc3cfe22c'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['division']