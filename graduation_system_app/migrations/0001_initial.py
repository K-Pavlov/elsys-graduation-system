# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mentor'
        db.create_table(u'graduation_system_app_mentor', (
            ('id', self.gf('django.db.models.fields.CharField')(default='17783102016211587556', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('graduation_system_app', ['Mentor'])

        # Adding model 'Topic'
        db.create_table(u'graduation_system_app_topic', (
            ('id', self.gf('django.db.models.fields.CharField')(default='17783789206683980260', max_length=36, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('graduation_system_app', ['Topic'])

        # Adding model 'Student'
        db.create_table(u'graduation_system_app_student', (
            ('id', self.gf('django.db.models.fields.CharField')(default='17783102011916620260', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('class_letter', self.gf('django.db.models.fields.CharField')(default='', max_length=1, null=True, blank=True)),
            ('specialization', self.gf('django.db.models.fields.CharField')(default='', max_length=150, null=True, blank=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Topic'], blank=True, null=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Mentor'], blank=True, null=True)),
            ('grade', self.gf('django.db.models.fields.FloatField')(default=2.0, blank=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Mentor'
        db.delete_table(u'graduation_system_app_mentor')

        # Deleting model 'Topic'
        db.delete_table(u'graduation_system_app_topic')

        # Deleting model 'Student'
        db.delete_table(u'graduation_system_app_student')


    models = {
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'17783789215273914852'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'class_letter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'17783789210978947556'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'17783789219568882148'", 'max_length': '36', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']