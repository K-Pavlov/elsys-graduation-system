# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Klass'
        db.create_table(u'graduation_system_app_klass', (
            ('id', self.gf('django.db.models.fields.CharField')(default='8651166771006869988', max_length=36, primary_key=True)),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graduation_system_app', ['Klass'])

        # Deleting field 'Student.class_letter'
        db.delete_column(u'graduation_system_app_student', 'class_letter')

        # Deleting field 'Student.specialization'
        db.delete_column(u'graduation_system_app_student', 'specialization')

        # Adding field 'Student.klass'
        db.add_column(u'graduation_system_app_student', 'klass',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Klass'], blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Klass'
        db.delete_table(u'graduation_system_app_klass')

        # Adding field 'Student.class_letter'
        db.add_column(u'graduation_system_app_student', 'class_letter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Student.specialization'
        db.add_column(u'graduation_system_app_student', 'specialization',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Student.klass'
        db.delete_column(u'graduation_system_app_student', 'klass_id')


    models = {
        'graduation_system_app.firm': {
            'Meta': {'object_name': 'Firm'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185379866186212'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.klass': {
            'Meta': {'object_name': 'Klass'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185401341022692'", 'max_length': '36', 'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185388456120804'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referee': {
            'Meta': {'object_name': 'Referee'},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185392751088100'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referal': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185397046055396'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185384161153508'", 'max_length': '36', 'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Klass']", 'blank': 'True', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'8653185375571218916'", 'max_length': '36', 'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']