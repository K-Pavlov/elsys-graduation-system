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
    url(r'^topics/$', topics.all, name='all_topics'),
    url(r'^mentors/$', mentors.all, name='all_mentors'),
    url(r'^mentors/edit/(?P<id>\d+)/$', metors.edit, name='edit_mentors'),
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
