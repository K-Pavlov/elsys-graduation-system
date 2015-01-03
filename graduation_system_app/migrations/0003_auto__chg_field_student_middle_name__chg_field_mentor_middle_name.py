# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Student.middle_name'
        db.alter_column(u'graduation_system_app_student', 'middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Mentor.middle_name'
        db.alter_column(u'graduation_system_app_mentor', 'middle_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Student.middle_name'
        db.alter_column(u'graduation_system_app_student', 'middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

        # Changing field 'Mentor.middle_name'
        db.alter_column(u'graduation_system_app_mentor', 'middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    models = {
        'graduation_system_app.klass': {
            'Meta': {'object_name': 'Klass'},
            'classLetter': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10772796609646825956'", 'max_length': '36', 'primary_key': 'True'}),
            'specialization': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10772796601056891364'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10772796605351858660'", 'max_length': '36', 'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Klass']", 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Mentor']", 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graduation_system_app.Topic']", 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'10772796613941793252'", 'max_length': '36', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']