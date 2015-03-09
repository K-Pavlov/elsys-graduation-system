# -*- coding: utf-8 -*- 
from datetime import datetime
 
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from shared.forms import BootstrapAuthenticationForm

admin.autodiscover()
urlpatterns = patterns('',
    url('', include('defences.urls')),
    url('', include('division.urls')),
    url('', include('reviewing.urls')),
    url('', include('shared.urls')),
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
    # Django auth urls
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # Python social app django urls
    url('', include('social.apps.django_app.urls', namespace='social')),
    # Django admin urls 
    url(r'^admin/', admin.site.urls),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
