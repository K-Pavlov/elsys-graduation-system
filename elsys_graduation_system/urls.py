# -*- coding: utf-8 -*-

from datetime import datetime

from django.contrib import admin
from django.conf.urls import patterns, url

from graduation_system_app.forms.login import BootstrapAuthenticationForm
from graduation_system_app.views import home, students, topics, mentors

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.index, name='home'),
    url(r'^students/$', students.all, name='all_students'),
    url(r'^students/create/$', students.create, name='create_students'),
    url(r'^students/edit/(?P<id>\d+)/$', students.edit, name='edit_student'),
    url(r'^topics/$', topics.all, name='all_topics'),
    url(r'^topics/create/$', topics.create, name='create_topic'),
    url(r'^topics/edit/(?P<id>\d+)/$', topics.edit, name='edit_topic'),
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/create/$', mentors.create, name='create_mentor'),
    url(r'^mentors/edit/(?P<id>\d+)/$', mentors.edit, name='edit_mentor'),
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
