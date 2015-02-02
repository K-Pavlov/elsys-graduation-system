# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Season'
        db.create_table(u'graduation_system_app_season', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16070976805048947172', max_length=36, primary_key=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('is_active', self.gf('django.db.models.fields.NullBooleanField')(default=False, null=True, blank=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Season'])

        # Adding model 'Firm'
        db.create_table(u'graduation_system_app_firm', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16070976800753979876', max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graduation_system_app', ['Firm'])

        # Adding model 'Teacher'
        db.create_table(u'graduation_system_app_teacher', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16071148599445819876', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('firm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Firm'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Teacher'])

        # Adding model 'Mentor'
        db.create_table(u'graduation_system_app_mentor', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16071062704394867172', max_length=36, primary_key=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Teacher'], blank=True, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Season'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Mentor'])

        # Adding model 'Referee'
        db.create_table(u'graduation_system_app_referee', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16070719094126285284', max_length=36, primary_key=True)),
            ('referal', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Teacher'], blank=True, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='referees', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Season'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Referee'])

        # Adding model 'Topic'
        db.create_table(u'graduation_system_app_topic', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16071105649772859876', max_length=36, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Mentor'], blank=True, null=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Referee'], blank=True, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='topics', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Season'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Topic'])

        # Adding model 'Comission'
        db.create_table(u'graduation_system_app_comission', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16071019750426939876', max_length=36, primary_key=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('head_of_comission', self.gf('django.db.models.fields.related.OneToOneField')(related_name='head_of_comission', unique=True, on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Teacher'], blank=True, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comissions', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Season'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Comission'])

        # Adding M2M table for field members_of_comission on 'Comission'
        m2m_table_name = db.shorten_name(u'graduation_system_app_comission_members_of_comission')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comission', models.ForeignKey(orm['graduation_system_app.comission'], null=False)),
            ('teacher', models.ForeignKey(orm['graduation_system_app.teacher'], null=False))
        ))
        db.create_unique(m2m_table_name, ['comission_id', 'teacher_id'])

        # Adding model 'Specialization'
        db.create_table(u'graduation_system_app_specialization', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16070762052389179876', max_length=36, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graduation_system_app', ['Specialization'])

        # Adding model 'ClassLetter'
        db.create_table(u'graduation_system_app_classletter', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16071019746131972580', max_length=36, primary_key=True)),
            ('letter', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graduation_system_app', ['ClassLetter'])

        # Adding model 'Student'
        db.create_table(u'graduation_system_app_student', (
            ('id', self.gf('django.db.models.fields.CharField')(default='16070805002062139876', max_length=36, primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('grade', self.gf('django.db.models.fields.FloatField')(default=2.0, blank=True)),
            ('class_letter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.ClassLetter'], blank=True, null=True)),
            ('specialization', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Specialization'], blank=True, null=True)),
            ('topic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Topic'], blank=True, null=True)),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Mentor'], blank=True, null=True)),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Season'], blank=True, null=True)),
            ('comission', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Comission'], blank=True, null=True)),
            ('referee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', on_delete=models.SET_NULL, default='', to=orm['graduation_system_app.Referee'], blank=True, null=True)),
        ))
        db.send_create_signal('graduation_system_app', ['Student'])


    def backwards(self, orm):
        # Deleting model 'Season'
        db.delete_table(u'graduation_system_app_season')

        # Deleting model 'Firm'
        db.delete_table(u'graduation_system_app_firm')

        # Deleting model 'Teacher'
        db.delete_table(u'graduation_system_app_teacher')

        # Deleting model 'Mentor'
        db.delete_table(u'graduation_system_app_mentor')

        # Deleting model 'Referee'
        db.delete_table(u'graduation_system_app_referee')

        # Deleting model 'Topic'
        db.delete_table(u'graduation_system_app_topic')

        # Deleting model 'Comission'
        db.delete_table(u'graduation_system_app_comission')

        # Removing M2M table for field members_of_comission on 'Comission'
        db.delete_table(db.shorten_name(u'graduation_system_app_comission_members_of_comission'))

        # Deleting model 'Specialization'
        db.delete_table(u'graduation_system_app_specialization')

        # Deleting model 'ClassLetter'
        db.delete_table(u'graduation_system_app_classletter')

        # Deleting model 'Student'
        db.delete_table(u'graduation_system_app_student')


    models = {
        'graduation_system_app.classletter': {
            'Meta': {'object_name': 'ClassLetter'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072952477120205284'", 'max_length': '36', 'primary_key': 'True'}),
            'letter': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.comission': {
            'Meta': {'object_name': 'Comission'},
            'head_of_comission': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'head_of_comission'", 'unique': 'True', 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072952481415172580'", 'max_length': '36', 'primary_key': 'True'}),
            'members_of_comission': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'members_of_comission'", 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comissions'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        'graduation_system_app.firm': {
            'Meta': {'object_name': 'Firm'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072909531742212580'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072995426793165284'", 'max_length': '36', 'primary_key': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.referee': {
            'Meta': {'object_name': 'Referee'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072737741640307172'", 'max_length': '36', 'primary_key': 'True'}),
            'referal': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'referees'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Teacher']", 'blank': 'True', 'null': 'True'})
        },
        'graduation_system_app.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072909536037179876'", 'max_length': '36', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'graduation_system_app.specialization': {
            'Meta': {'object_name': 'Specialization'},
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072780691313267172'", 'max_length': '36', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graduation_system_app.student': {
            'Meta': {'object_name': 'Student'},
            'class_letter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.ClassLetter']", 'blank': 'True', 'null': 'True'}),
            'comission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Comission']", 'blank': 'True', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'grade': ('django.db.models.fields.FloatField', [], {'default': '2.0', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'16072823636691259876'", 'max_length': '36', 'primary_key': 'True'}),
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
            'id': ('django.db.models.fields.CharField', [], {'default': "'16073081330434052580'", 'max_length': '36', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'graduation_system_app.topic': {
            'Meta': {'object_name': 'Topic'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'default': "'16073038385056059876'", 'max_length': '36', 'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Mentor']", 'blank': 'True', 'null': 'True'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Referee']", 'blank': 'True', 'null': 'True'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'topics'", 'on_delete': 'models.SET_NULL', 'default': "''", 'to': "orm['graduation_system_app.Season']", 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['graduation_system_app']