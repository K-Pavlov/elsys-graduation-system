# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Season'
        db.create_table('season', (
            ('id', self.gf('django.db.models.fields.CharField')(default='c577ff8f-00af-4390-9e74-6cc5f439ea13', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal('shared', ['Season'])

        # Adding model 'Firm'
        db.create_table('firm', (
            ('id', self.gf('django.db.models.fields.CharField')(default='20d21554-ff8f-47b8-9081-ca6b90703d9d', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('shared', ['Firm'])

        # Adding model 'Teacher'
        db.create_table('teacher', (
            ('id', self.gf('django.db.models.fields.CharField')(default='b6aada66-8550-4f20-9057-16b13ec556e1', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('firm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teachers', on_delete=models.SET_NULL, default='', to=orm['shared.Firm'], blank=True, null=True)),
        ))
        db.send_create_signal('shared', ['Teacher'])


    def backwards(self, orm):
        # Deleting model 'Season'
        db.delete_table('season')

        # Deleting model 'Firm'
        db.delete_table('firm')

        # Deleting model 'Teacher'
        db.delete_table('teacher')


    models = {
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'46279162-9f7f-43b0-a59a-cd6c969e258b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'021e8a30-cc18-4f04-991b-629631fdeea0'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'262dbd80-4d65-49fd-a36e-ace57b6747b9'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['shared']