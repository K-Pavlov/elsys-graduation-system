# -*- coding: utf-8 -*-
 
from datetime import datetime
 
from django.contrib import admin
from django.conf.urls import patterns, url, include
 
from graduation_system_app.forms.login import BootstrapAuthenticationForm
from graduation_system_app.views import home, students, topics, mentors, seasons, referees, specializations, class_letters, teachers, comissions
 
admin.autodiscover()
 
urlpatterns = patterns('',
    # Students
    url(r'^$', home.index, name='home'),
    url(r'^students/$', students.all, name='all_students'),
    url(r'^students/create/$', students.create, name='create_students'),
    url(r'^students/edit/(?P<id>\d+)/$', students.edit, name='edit_student'),
    url(r'^students/delete/(?P<id>\d+)/$', students.delete, name='delete_student'),
    url(r'^students/upload/$', students.upload_csv, name='upload_students'),
    url(r'^students/generate_protocol/$', students.generate_protocol, name='generate_individual_protocol'),
    # Topics
    url(r'^topics/$', topics.all, name='all_topics'),
    url(r'^topics/create/$', topics.create, name='create_topic'),
    url(r'^topics/edit/(?P<id>\d+)/$', topics.edit, name='edit_topic'),
    url(r'^topics/delete/(?P<id>\d+)/$', topics.delete, name='delete_topic'),
    url(r'^topics/upload/$', topics.upload_csv, name='upload_topics'),
    # Seasons
    url(r'^seasons/$', seasons.all, name='all_seasons'),
    url(r'^seasons/create/$', seasons.create, name='create_season'),
    url(r'^seasons/edit/(?P<id>\d+)/$', seasons.edit, name='edit_season'),
    url(r'^seasons/delete/(?P<id>\d+)/$', seasons.delete, name='delete_season'),
    url(r'^seasons/change/$', seasons.change, name='change_season'),
    # Mentors
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/create/$', mentors.create, name='create_mentor'),
    url(r'^mentors/edit/(?P<id>\d+)/$', mentors.edit, name='edit_mentor'),
    url(r'^mentors/delete/(?P<id>\d+)/$', mentors.delete, name='delete_mentor'),
    url(r'^mentors/upload/$', mentors.upload_csv, name='upload_mentors'),
    # Referees
    url(r'^referees/$', referees.all, name='all_referees'),
    url(r'^referees/create/$', referees.create, name='create_referee'),
    url(r'^referees/edit/(?P<id>\d+)/$', referees.edit, name='edit_referee'),
    url(r'^referees/delete/(?P<id>\d+)/$', referees.delete, name='delete_referee'),
    url(r'^referees/upload/$', referees.upload_csv, name='upload_referees'),
    url(r'^referees/refereal_upload/$', referees.upload_referal, name='upload_referal'),
    # Class letters
    url(r'^class_letters/$', class_letters.all, name='all_class_letters'),
    url(r'^class_letters/create/$', class_letters.create, name='create_class_letter'),
    url(r'^class_letters/edit/(?P<id>\d+)/$', class_letters.edit, name='edit_class_letter'),
    url(r'^class_letters/delete/(?P<id>\d+)/$', class_letters.delete, name='delete_class_letter'),
    # Specializations
    url(r'^specializations/$', specializations.all, name='all_specializations'),
    url(r'^specializations/create/$', specializations.create, name='create_specialization'),
    url(r'^specializations/edit/(?P<id>\d+)/$', specializations.edit, name='edit_specialization'),
    url(r'^specializations/delete/(?P<id>\d+)/$', specializations.delete, name='delete_specialization'),
    # Teachers
    url(r'^teachers/$', teachers.all, name='all_teachers'),
    url(r'^teachers/create/$', teachers.create, name='create_teacher'),
    url(r'^teachers/edit/(?P<id>\d+)/$', teachers.edit, name='edit_teacher'),
    url(r'^teachers/delete/(?P<id>\d+)/$', teachers.delete, name='delete_teacher'),
    # Comissions
    url(r'^comissions/$', comissions.all, name='all_comissions'),
    url(r'^comissions/create/$', comissions.create, name='create_comission'),
    url(r'^comissions/edit/(?P<id>\d+)/$', comissions.edit, name='edit_comission'),
    url(r'^comissions/delete/(?P<id>\d+)/$', comissions.delete, name='delete_comission'),
    url(r'^comissions/upload/$', comissions.upload_csv, name='upload_comissions'),
    # Google auth and normal login
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': u'Влизане в системата',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')), 
    url(r'^admin/', admin.site.urls),
)
