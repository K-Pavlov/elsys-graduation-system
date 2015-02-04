# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Referals'
        db.delete_table(u'graduation_system_app_referals')

        # Adding model 'Referal'
        db.create_table(u'graduation_system_app_referal', (
            ('id', self.gf('django.db.models.fields.CharField')(default='14842282662809244132', max_length=36, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referals', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Referee'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Referal'])


    def backwards(self, orm):
        # Adding model 'Referals'
        db.create_table(u'graduation_system_app_referals', (
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referals', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Referee'], blank=True, null=True)),
            ('id', self.gf('django.db.models.fields.CharField')(default='4890562512756216292', max_length=36, primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Referals'])

        # Deleting model 'Referal'
        db.delete_table(u'graduation_system_app_referal')


    models = {
        'graduation_system_app.classletter': {
            'Meta': {'object_name': 'ClassLetter'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845675686973084132'", 'max_length': '36', 'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.comission': {
            'Meta': {'object_name': 'Comission'},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845761586319004132'", 'max_length': '36', 'primary_key': 'True'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comissions'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.firm': {
            'Meta': {'object_name': 'Firm'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845761582024036836'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845417984640356836'", 'max_length': '36', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referal': {
            'Meta': {'object_name': 'Referal'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845675691268051428'", 'max_length': '36', 'primary_key': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referals'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referee': {
            'Meta': {'object_name': 'Referee'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845589783332196836'", 'max_length': '36', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845460934313316836'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.specialization': {
            'Meta': {'object_name': 'Specialization'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845460930018349540'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845460938608284132'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'specialization': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Specialization']", 'blank': 'True', 'null': 'True'}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Topic']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.teacher': {
            'Meta': {'object_name': 'Teacher'},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845718632351076836'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'14845546833659236836'", 'max_length': '36', 'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']