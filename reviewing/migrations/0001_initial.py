# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Referee'
        db.create_table('referee', (
            ('id', self.gf('django.db.models.fields.CharField')(default='2554aca4-7a21-4731-8371-bb27ac2629fc', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['shared.Season'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(default='', related_name='referees', null=True, blank=True, to=orm['shared.Teacher'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
        ))
        db.send_create_signal('reviewing', ['Referee'])

        # Adding model 'Referal'
        db.create_table('referal', (
            ('id', self.gf('django.db.models.fields.CharField')(default='51eedbe1-0874-4cc5-a00b-c09ffc554193', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referals', on_delete=models.SET_NULL, default='', to=orm['reviewing.Referee'], blank=True, null=True)),
        ))
        db.send_create_signal('reviewing', ['Referal'])


    def backwards(self, orm):
        # Deleting model 'Referee'
        db.delete_table('referee')

        # Deleting model 'Referal'
        db.delete_table('referal')


    models = {
        'reviewing.referal': {
            'Meta': {'ordering': "['referee']", 'object_name': 'Referal', 'db_table': "'referal'"},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'0b88cf1a-69ca-4c87-8359-40afee49c945'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referals'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['reviewing.Referee']", 'blank': 'True', 'null': 'True'})
        },
        'reviewing.referee': {
            'Meta': {'ordering': "['teacher']", 'object_name': 'Referee', 'db_table': "'referee'"},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'517df330-1eef-4959-9e4c-a850df5bde3b'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'related_name': "'referees'", 'null': 'True', 'blank': 'True', 'to': "orm['shared.Teacher']"})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'b41c919e-61c8-4ea6-ab8a-469896316959'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'51486f4a-174f-4ee4-afdf-0ee0fcb5e46f'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'f3b8db84-bd5b-4d3e-8ff6-c65ec91c7133'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reviewing']