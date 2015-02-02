# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Teacher'
        db.create_table(u'graduation_system_app_teacher', (
            ('id', self.gf('django.db.models.fields.CharField')(default='15413166966913896932', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('firm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Firm'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Teacher'])

        # Deleting field 'Referee.firm'
        db.delete_column(u'graduation_system_app_referee', 'firm_id')

        # Deleting field 'Referee.first_name'
        db.delete_column(u'graduation_system_app_referee', 'first_name')

        # Deleting field 'Referee.middle_name'
        db.delete_column(u'graduation_system_app_referee', 'middle_name')

        # Deleting field 'Referee.last_name'
        db.delete_column(u'graduation_system_app_referee', 'last_name')

        # Adding field 'Referee.teacher'
        db.add_column(u'graduation_system_app_referee', 'teacher',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Teacher'], blank=True, null=True),
                      keep_default=False)

        # Deleting field 'Mentor.first_name'
        db.delete_column(u'graduation_system_app_mentor', 'first_name')

        # Deleting field 'Mentor.last_name'
        db.delete_column(u'graduation_system_app_mentor', 'last_name')

        # Deleting field 'Mentor.middle_name'
        db.delete_column(u'graduation_system_app_mentor', 'middle_name')

        # Adding field 'Mentor.teacher'
        db.add_column(u'graduation_system_app_mentor', 'teacher',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Teacher'], blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Teacher'
        db.delete_table(u'graduation_system_app_teacher')

        # Adding field 'Referee.firm'
        db.add_column(u'graduation_system_app_referee', 'firm',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Firm'], blank=True, null=True),
                      keep_default=False)

        # Adding field 'Referee.first_name'
        db.add_column(u'graduation_system_app_referee', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Referee.middle_name'
        db.add_column(u'graduation_system_app_referee', 'middle_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Referee.last_name'
        db.add_column(u'graduation_system_app_referee', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Deleting field 'Referee.teacher'
        db.delete_column(u'graduation_system_app_referee', 'teacher_id')

        # Adding field 'Mentor.first_name'
        db.add_column(u'graduation_system_app_mentor', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Mentor.last_name'
        db.add_column(u'graduation_system_app_mentor', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Mentor.middle_name'
        db.add_column(u'graduation_system_app_mentor', 'middle_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Mentor.teacher'
        db.delete_column(u'graduation_system_app_mentor', 'teacher_id')


    models = {
        'graduation_system_app.firm': {
            'Meta': {'object_name': 'Firm'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530088912425444'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.klass': {
            'Meta': {'object_name': 'Klass'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530084617458148'", 'max_length': '36', 'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530093207392740'", 'max_length': '36', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referee': {
            'Meta': {'object_name': 'Referee'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530076027523556'", 'max_length': '36', 'primary_key': 'True'}),
            'referal': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530097502360036'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530101797327332'", 'max_length': '36', 'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Klass']", 'blank': 'True', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530080322490852'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'172530106092294628'", 'max_length': '36', 'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']