# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'graduation_system_app_topic', (
            ('id', self.gf('django.db.models.fields.CharField')(default='868170140338426340', max_length=36, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('graduation_system_app', ['Topic'])

        # Adding model 'Klass'
        db.create_table(u'graduation_system_app_klass', (
            ('id', self.gf('django.db.models.fields.CharField')(default='868170136043459044', max_length=36, primary_key=True)),
            ('classLetter', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('specialization', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('graduation_system_app', ['Klass'])

        # Adding model 'Student'
        db.create_table(u'graduation_system_app_student', (
            ('id', self.gf('django.db.models.fields.CharField')(default='868170131748491748', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graduation_system_app.Klass'], null=True, blank=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graduation_system_app.Topic'], null=True, blank=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graduation_system_app.Mentor'], null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.FloatField')(default=2.0, blank=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Student'])

        # Adding model 'Mentor'
        db.create_table(u'graduation_system_app_mentor', (
            ('id', self.gf('django.db.models.fields.CharField')(default='868170127453524452', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('graduation_system_app', ['Mentor'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'graduation_system_app_topic')

        # Deleting model 'Klass'
        db.delete_table(u'graduation_system_app_klass')

        # Deleting model 'Student'
        db.delete_table(u'graduation_system_app_student')

        # Deleting model 'Mentor'
        db.delete_table(u'graduation_system_app_mentor')


    models = {
        'graduation_system_app.klass': {
            'Meta': {'object_name': 'Klass'},
            'classLetter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'868857330810819044'", 'max_length': '36', 'primary_key': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'868857322220884452'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'868857326515851748'", 'max_length': '36', 'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Klass']", 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Mentor']", 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Topic']", 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'868857335105786340'", 'max_length': '36', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']