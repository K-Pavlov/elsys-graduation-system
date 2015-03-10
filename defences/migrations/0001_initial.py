# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comission'
        db.create_table('comission', (
            ('id', self.gf('django.db.models.fields.CharField')(default='7bf113e6-2cf5-4bca-8e24-d4cc80b115b6', max_length=36, primary_key=True)),
            ('is_deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['shared.Season'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(default='', null=True, blank=True)),
            ('head_of_comission', self.gf('django.db.models.fields.related.OneToOneField')(related_name='head_of_comission', unique=True, on_delete=models.SET_NULL, default='', to=orm['shared.Teacher'], blank=True, null=True)),
        ))
        db.send_create_signal('defences', ['Comission'])

        # Adding M2M table for field members_of_comission on 'Comission'
        m2m_table_name = db.shorten_name('comission_members_of_comission')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comission', models.ForeignKey(orm['defences.comission'], null=False)),
            ('teacher', models.ForeignKey(orm['shared.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comission_id', 'teacher_id'])


    def backwards(self, orm):
        # Deleting model 'Comission'
        db.delete_table('comission')

        # Removing M2M table for field members_of_comission on 'Comission'
        db.delete_table(db.shorten_name('comission_members_of_comission'))


    models = {
        'defences.comission': {
            'Meta': {'ordering': "['start_time']", 'object_name': 'Comission', 'db_table': "'comission'"},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'66b6a540-ae14-4d1b-afb9-f453cfd9a085'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['shared.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'default': "''", 'to': "orm['shared.Season']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        },
        'shared.firm': {
            'Meta': {'ordering': "['name']", 'object_name': 'Firm', 'db_table': "'firm'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'6f1402c9-da06-4c35-917c-870ff438dd9f'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shared.season': {
            'Meta': {'ordering': "['year']", 'object_name': 'Season', 'db_table': "'season'"},
            'id': ('django.db.models.fields.CharField', [], {'default': "'a0b65fe2-be61-4c73-8bd6-3a69f33378d5'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shared.teacher': {
            'Meta': {'ordering': "['first_name', 'middle_name', 'last_name']", 'object_name': 'Teacher', 'db_table': "'teacher'"},
            'firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teachers'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['shared.Firm']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'b21c1b57-0168-479b-8bd0-225e96043e39'", 'max_length': '36', 'primary_key': 'True'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['defences']