# -*- coding: utf-8 -*-
 
from datetime import datetime
 
from django.contrib import admin
from django.conf.urls import patterns, url
 
from graduation_system_app.forms.login import BootstrapAuthenticationForm
from graduation_system_app.views import home, students, topics, mentors, seasons, referees
 
admin.autodiscover()
 
urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.index, name='home'),
    url(r'^students/$', students.all, name='all_students'),
    url(r'^students/create/$', students.create, name='create_students'),
    url(r'^students/edit/(?P<id>\d+)/$', students.edit, name='edit_student'),
    url(r'^students/delete/(?P<id>\d+)/$', students.delete, name='delete_student'),
    url(r'^students/upload/$', students.upload_csv, name='upload_students'),
    url(r'^topics/$', topics.all, name='all_topics'),
    url(r'^topics/create/$', topics.create, name='create_topic'),
    url(r'^topics/edit/(?P<id>\d+)/$', topics.edit, name='edit_topic'),
    url(r'^topics/delete/(?P<id>\d+)/$', topics.delete, name='delete_topic'),
    url(r'^topics/upload/$', topics.upload_csv, name='upload_topics'),
    url(r'^seasons/$', seasons.all, name='all_seasons'),
    url(r'^seasons/create/$', seasons.create, name='create_season'),
    url(r'^seasons/edit/(?P<id>\d+)/$', seasons.edit, name='edit_season'),
    url(r'^seasons/delete/(?P<id>\d+)/$', seasons.delete, name='delete_season'),
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/create/$', mentors.create, name='create_mentor'),
    url(r'^mentors/edit/(?P<id>\d+)/$', mentors.edit, name='edit_mentor'),
    url(r'^mentors/delete/(?P<id>\d+)/$', mentors.delete, name='delete_mentor'),
    url(r'^mentors/upload/$', mentors.upload_csv, name='upload_mentors'),
    url(r'^referees/$', referees.all, name='all_referees'),
    url(r'^referees/create/$', referees.create, name='create_referee'),
    url(r'^referees/edit/(?P<id>\d+)/$', referees.edit, name='edit_referee'),
    url(r'^referees/delete/(?P<id>\d+)/$', referees.delete, name='delete_referee'),
    url(r'^referees/upload/$', referees.upload_csv, name='upload_referees'),
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
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    url(r'^admin/', admin.site.urls),
)